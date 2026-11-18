#!/usr/bin/env python3
"""Run the complete pre-commit regression and release-control simulation."""
import argparse
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github/workflows"
DEFAULT_RULESET = ROOT / ".github/main-ruleset-contract.json"
DEFER_UNTIL_RECONCILED = {"test_check_live_surface.py", "test_check_session_pack.py"}


class PreflightError(ValueError):
    pass


def load_workflow(path):
    try:
        import yaml
    except ImportError as exc:
        raise PreflightError("PyYAML is required for release preflight") from exc

    class WorkflowLoader(yaml.SafeLoader):
        pass

    for first, resolvers in list(WorkflowLoader.yaml_implicit_resolvers.items()):
        WorkflowLoader.yaml_implicit_resolvers[first] = [
            (tag, regexp)
            for tag, regexp in resolvers
            if tag != "tag:yaml.org,2002:bool"
        ]
    try:
        data = yaml.load(path.read_text(), Loader=WorkflowLoader)
    except yaml.YAMLError as exc:
        raise PreflightError(f"invalid workflow YAML in {path.name}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("jobs"), dict):
        raise PreflightError(f"workflow has no jobs mapping: {path.name}")
    return data


def triggers(workflow):
    value = workflow.get("on", {})
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return set(value)
    if isinstance(value, dict):
        return set(value)
    return set()


def ruleset_requirements(data):
    if data.get("enforcement") != "active":
        raise PreflightError("main ruleset is not active")
    if data.get("bypass_actors"):
        raise PreflightError("main ruleset contains bypass actors")
    if data.get("current_user_can_bypass") not in (None, "never"):
        raise PreflightError("current actor can bypass the main ruleset")

    rules = {rule.get("type"): rule for rule in data.get("rules", [])}
    for required in ("deletion", "non_fast_forward", "pull_request", "required_status_checks"):
        if required not in rules:
            raise PreflightError(f"main ruleset is missing {required}")
    merge_methods = rules["pull_request"].get("parameters", {}).get("allowed_merge_methods")
    if merge_methods != ["squash"]:
        raise PreflightError("main ruleset must allow squash merge only")
    parameters = rules["required_status_checks"].get("parameters", {})
    if parameters.get("strict_required_status_checks_policy") is not True:
        raise PreflightError("main ruleset must require the current main base")
    contexts = parameters.get("required_status_checks", [])
    if any(row.get("context") == "candidate-ready" and row.get("integration_id") != 15368 for row in contexts):
        raise PreflightError("candidate-ready must be bound to GitHub Actions")
    names = {row.get("context") for row in contexts if isinstance(row, dict)}
    if not names or None in names:
        raise PreflightError("main ruleset has malformed required status contexts")
    return names


def simulate_controls(root, ruleset_data):
    required = ruleset_requirements(ruleset_data)
    workflows = {
        path.name: load_workflow(path)
        for path in sorted((root / ".github/workflows").glob("*.y*ml"))
    }
    automatic_pr = sorted(name for name, workflow in workflows.items() if "pull_request" in triggers(workflow))
    if automatic_pr:
        raise PreflightError("PR-time workflow fan-out remains: " + ", ".join(automatic_pr))

    support = (root / ".github/scripts/candidate_contexts.js").read_text()
    match = re.search(r"const CANDIDATE_STATUS_CONTEXTS = Object\.freeze\(\[(.*?)\]\);", support, re.S)
    if not match:
        raise PreflightError("candidate status context declaration is missing")
    candidate = set(re.findall(r'"([^"]+)"', match.group(1)))
    if required != {"candidate-ready"} or candidate:
        raise PreflightError("candidate status publisher does not cover exactly the final ruleset context")

    reconciler = workflows.get("build-derived-views.yml")
    if reconciler is None:
        raise PreflightError("missing consolidated reconciler")
    reconciler_triggers = triggers(reconciler)
    if "push" not in reconciler_triggers or "pull_request" in reconciler_triggers:
        raise PreflightError("reconciler must run on staging pushes, not PR events")
    concurrency = reconciler.get("concurrency", {})
    if str(concurrency.get("cancel-in-progress")).lower() != "true":
        raise PreflightError("reconciler must cancel obsolete same-event runs")
    group = str(concurrency.get("group", ""))
    if "${{ github.ref_name }}" not in group:
        raise PreflightError("reconciler concurrency must serialize each branch")
    reconciler_source = (root / ".github/workflows/build-derived-views.yml").read_text()
    for fragment in ("contents: write", "statuses: write", "createCommitStatus", "CANDIDATE_STATUS_CONTEXTS", "CANDIDATE_ATTESTATION_CONTEXT", "final_candidate_checks.py main --scratch-candidate", "final_candidate_checks.py main --confirm", "check_code_review.py", "fixed_point_output", "library-reconcile-bot", 'git push origin "HEAD:$TARGET_BRANCH"'):
        if fragment not in reconciler_source:
            raise PreflightError(f"reconciler lacks exact-SHA candidate control: {fragment}")
    candidate_source = (root / ".github/scripts/final_candidate_checks.py").read_text()
    for fragment in ('"validate_repo_state.py"', '"auto_heal_links.py", "--check"',
                     '"origin/staging"', '"main changed during validation"'):
        if fragment not in candidate_source:
            raise PreflightError(f"candidate validator lacks integrity control: {fragment}")

    if "merge-gate.yml" in workflows or "main-guard.yml" in workflows:
        raise PreflightError("retired custom merge/recovery workflows must not remain active")
    return {
        "required_contexts": sorted(required),
        "candidate_contexts": sorted(candidate),
        "receipt_contexts": [],
        "merge_mode": "native protected squash; explicit lease refresh",
        "cancellation": "one cancellable staging pipeline per branch; PR creation starts no test fan-out",
    }


def run(command):
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def select_tests(suite, phase):
    """Partition the complete suite; discovery failures must never be omitted."""
    if phase not in {"all", "source", "reconciled"}:
        raise PreflightError(f"unknown test phase: {phase}")
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from select_tests(item, phase)
        else:
            module = item.id().split(".")[0]
            deferred = f"{module}.py" in DEFER_UNTIL_RECONCILED
            if (phase == "all" or module == "unittest"
                    or deferred == (phase == "reconciled")):
                yield item


def run_test_suite(phase="all"):
    discovered = unittest.defaultTestLoader.discover(
        str(ROOT / ".github/tests"), pattern="test_*.py"
    )
    result = unittest.TextTestRunner(verbosity=1).run(
        unittest.TestSuite(select_tests(discovered, phase))
    )
    if not result.wasSuccessful():
        raise PreflightError(f"{phase}-phase Python tests failed")
    js_tests = sorted(str(path.relative_to(ROOT)) for path in (ROOT / ".github/tests").glob("test_*.js"))
    if js_tests and phase != "reconciled":
        run(["node", "--test", *js_tests])


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ruleset-json", type=Path, default=DEFAULT_RULESET)
    parser.add_argument("--controls-only", action="store_true")
    phase = parser.add_mutually_exclusive_group()
    phase.add_argument("--source-only", action="store_true")
    phase.add_argument("--reconciled-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = simulate_controls(ROOT, json.loads(args.ruleset_json.read_text()))
        print(json.dumps(result, indent=2))
        if not args.controls_only:
            selected_phase = "source" if args.source_only else "reconciled" if args.reconciled_only else "all"
            run_test_suite(phase=selected_phase)
    except (OSError, json.JSONDecodeError, PreflightError, subprocess.CalledProcessError) as exc:
        print(f"PRE-FLIGHT FAIL: {exc}", file=sys.stderr)
        return 1
    print("PRE-FLIGHT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

