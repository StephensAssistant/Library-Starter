#!/usr/bin/env python3
"""Read-only candidate route assessment. Inputs are operator evidence, not authority.

This selects a qualified route; it never authenticates, writes or dispatches.
Actual exact-head run/status/artifact verification remains PLAY-0056's gate.
"""
import argparse
import json
from pathlib import Path
import re

GATE = "github.event_name == 'workflow_dispatch' || contains(github.event.head_commit.message, '[daily-commit]')"
BOUNDARY = "${{ steps.boundary.outputs.author_base }}"
SOURCE = "${{ github.event_name == 'workflow_dispatch' && inputs.candidate_sha || github.sha }}"
SHA = re.compile(r"[0-9a-f]{40}")
REQUIRED = ("current_authority", "current_admission", "actor_access", "main_unchanged",
            "expected_staging", "scope_preserved", "shared_bounds", "guarded_source_write",
            "source_readback", "runs_read", "artifacts_read", "statuses_read", "draft_pr_read")
REQUEST_CHECKS = {"source_changed_since_base", "relevant_correction", "author_base_provenance",
                  "first_request_for_source", "failed_tree_excluded", "receipt_provenance"}
REQUEST_FIELDS = {"source_sha", "source_tree", "base_tree", "repair_commit_sha", "main_sha",
                  "failed_trees", "prior_requests"}
REQUEST_PUSH_FIELDS = {"mode", "callable", "access", "evidence", "trigger_observed", "post_child_only",
                       "expected_parent", "required_author_base", "explicit_author_base",
                       "parent_from_verified_child", "candidate_sha", "planned_commit_verified",
                       "planned_commit_parent", "candidate_message", "planned_commit_tree",
                       "meaningful_source", "request", "request_checks"}


def nonzero_sha(value):
    return isinstance(value, str) and SHA.fullmatch(value) is not None and value != "0" * 40


def validation_request_error(info, data, phase):
    """Check supplied request evidence, never authenticate its truth or publish it."""
    if set(info) - REQUEST_PUSH_FIELDS:
        return "validation request has unsupported push fields"
    for key in ("callable", "trigger_observed", "post_child_only", "explicit_author_base",
                "parent_from_verified_child", "planned_commit_verified", "meaningful_source"):
        if key in info and not isinstance(info[key], bool):
            return "validation request boolean malformed: " + key
    checks = info.get("request_checks")
    if not isinstance(checks, dict) or set(checks) != REQUEST_CHECKS:
        return "validation request needs exactly the six request checks"
    for key in REQUEST_CHECKS:
        proof = checks[key]
        if (not isinstance(proof, dict) or set(proof) != {"verified", "evidence"}
                or proof["verified"] is not True or not isinstance(proof["evidence"], str)
                or not proof["evidence"].strip()):
            return "missing anchored validation request proof: " + key
    request = info.get("request")
    if not isinstance(request, dict) or set(request) != REQUEST_FIELDS:
        return "validation request fields malformed"
    for key in ("source_sha", "source_tree", "base_tree", "repair_commit_sha", "main_sha"):
        if not nonzero_sha(request[key]):
            return "validation request SHA malformed: " + key
    failed = request["failed_trees"]
    if (not isinstance(failed, list) or not all(nonzero_sha(value) for value in failed)
            or len(failed) != len(set(failed))):
        return "validation request failed tree evidence malformed"
    if not isinstance(request["prior_requests"], list) or request["prior_requests"]:
        return "validation request is not the first request for this source"
    if request["source_sha"] != data.get("staging_sha") or request["main_sha"] != data.get("main_sha"):
        return "validation request does not bind current staging and main"
    if request["source_tree"] == request["base_tree"] or request["source_tree"] in failed:
        return "validation request source is unchanged or a previously failed tree"
    if phase == "validate" and info.get("planned_commit_tree") != request["source_tree"]:
        return "validation request commit must preserve the verified corrected source tree"
    if "planned_commit_tree" in info and not nonzero_sha(info["planned_commit_tree"]):
        return "validation request planned tree malformed"
    return None


def strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key: " + key)
            result[key] = value
        return result
    def constant(value):
        raise ValueError("nonfinite JSON value: " + value)
    return json.loads(text, object_pairs_hook=pairs, parse_constant=constant)


def resolve_author_base(event_name, payload, explicit_base=None):
    """Resolve one exact boundary, preserving dispatch and legacy push inputs."""
    if not isinstance(payload, dict):
        raise ValueError("event payload must be an object")
    if event_name == "workflow_dispatch":
        value = explicit_base
    elif event_name == "push":
        head = payload.get("head_commit")
        if not isinstance(head, dict):
            raise ValueError("push head_commit must be an object")
        message = head.get("message", "")
        if not isinstance(message, str) or "[daily-commit]" not in message:
            raise ValueError("push is not eligible for candidate validation")
        lines = [line for line in message.splitlines() if line.lstrip().lower().startswith("candidate-author-base")]
        if lines:
            if len(lines) != 1 or not re.fullmatch(r"Candidate-Author-Base: [0-9a-f]{40}", lines[0]):
                raise ValueError("require one exact Candidate-Author-Base trailer")
            value = lines[0].split(": ", 1)[1]
        else:
            value = payload.get("before")
    else:
        raise ValueError("unsupported candidate event")
    if not isinstance(value, str) or not SHA.fullmatch(value) or value == "0" * 40:
        raise ValueError("author_base must be a nonzero lowercase commit SHA")
    return value


def trigger_contract(root):
    """Refuse unsupported native wiring rather than guess a changed expression."""
    import yaml
    path = Path(root) / ".github/workflows/build-derived-views.yml"
    try:
        spec = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    except yaml.YAMLError as exc:
        raise ValueError("malformed native workflow YAML") from exc
    events = spec["on"]
    job = spec["jobs"]["reconcile-library"]
    inputs = events["workflow_dispatch"]["inputs"]
    if (events["push"]["branches"] != ["staging"] or job["if"].strip() != GATE
            or any(inputs[key]["required"] != "true" or inputs[key]["type"] != "string"
                   for key in ("candidate_sha", "author_base"))
            or job["env"]["EXPECTED_CANDIDATE_SHA"] != SOURCE):
        raise ValueError("unsupported native candidate trigger/input wiring")
    boundary_steps = [step for step in job["steps"] if "AUTHOR_BASE" in step.get("env", {})]
    if not boundary_steps or any(step["env"]["AUTHOR_BASE"] != BOUNDARY for step in boundary_steps):
        raise ValueError("unsupported native author boundary wiring")
    resolver = next((step for step in job["steps"] if step.get("id") == "boundary"), {})
    if "candidate_entry.py" not in resolver.get("run", "") or "--resolve-author-base" not in resolver.get("run", ""):
        raise ValueError("missing native boundary resolver")
    learning = next((i for i, step in enumerate(job["steps"]) if step.get("id") == "learning"), None)
    if learning is None or job["steps"].index(resolver) >= learning:
        raise ValueError("boundary must resolve before learning checks")
    return {"dispatch": "workflow_dispatch", "push": "[daily-commit]", "push_author_base": "explicit trailer or event.before"}


def assess(data, root):
    """Validate explicit observed gate evidence. Unknown/malformed evidence blocks."""
    def blocked(reason, alternatives=None):
        return {"status": "blocked", "reason": reason, "alternatives": alternatives or [],
                "next": "Director-to-Head investigation under PLAY-0069; no terminal resume or inferred authority"}
    if not isinstance(data, dict):
        return blocked("input must be an operator evidence object")
    if data.get("terminal") is not False:
        return blocked("terminal or unknown invocation state")
    phase = data.get("phase")
    if not isinstance(phase, str) or phase not in {"entry", "validate"}:
        return blocked("phase must be entry or validate")
    for key in REQUIRED:
        proof = data.get("checks", {}).get(key) if isinstance(data.get("checks"), dict) else None
        if not isinstance(proof, dict) or proof.get("verified") is not True or not isinstance(proof.get("evidence"), str) or not proof["evidence"].strip():
            return blocked("missing current evidence: " + key)
    try:
        wiring = trigger_contract(root)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ImportError) as exc:
        return blocked("native trigger contract unverified: " + str(exc))
    if phase == "validate" and data.get("child_completed") is not True:
        return blocked("source-only child has not completed")
    alternatives = []
    for route in ("dispatch", "push"):
        info = data.get(route)
        if not isinstance(info, dict) or info.get("callable") is not True:
            alternatives.append({"route": route, "state": "unavailable", "reason": "callable capability absent or unverified"})
            continue
        if info.get("access") != "verified" or not isinstance(info.get("evidence"), str) or not info["evidence"].strip():
            alternatives.append({"route": route, "state": "unavailable", "reason": "permission denied" if info.get("access") == "denied" else "actor/access evidence unverified"})
            continue
        boundary = info.get("required_author_base")
        if not isinstance(boundary, str) or not SHA.fullmatch(boundary) or boundary == "0" * 40:
            alternatives.append({"route": route, "state": "unavailable", "reason": "correct required author boundary unverified"})
            continue
        if route == "push":
            push_mode = info.get("mode", "substantive_source")
            if not isinstance(push_mode, str) or push_mode not in {"substantive_source", "validation_request"}:
                alternatives.append({"route": route, "state": "unavailable", "reason": "unsupported push mode"})
                continue
            if (info.get("trigger_observed") is not True
                    or (push_mode == "substantive_source" and info.get("meaningful_source") is not True)):
                alternatives.append({"route": route, "state": "unavailable", "reason": "no justified meaningful post-child source or observed push-trigger primitive"})
                continue
            if push_mode == "validation_request":
                error = validation_request_error(info, data, phase)
                if error:
                    alternatives.append({"route": route, "state": "unavailable", "reason": error})
                    continue
            parent, boundary = info.get("expected_parent"), info.get("required_author_base")
            if not isinstance(boundary, str) or not SHA.fullmatch(boundary) or boundary == "0" * 40:
                alternatives.append({"route": route, "state": "unavailable", "reason": "correct required author boundary unverified"})
                continue
            if info.get("explicit_author_base") is not True and parent != boundary:
                alternatives.append({"route": route, "state": "unavailable", "reason": "event.before differs from required boundary and no explicit trailer is planned"})
                continue
            if phase == "entry" and parent is None and info.get("parent_from_verified_child") is not True:
                alternatives.append({"route": route, "state": "unavailable", "reason": "future parent derivation unverified"})
                continue
            if parent is not None and (not isinstance(parent, str) or not SHA.fullmatch(parent) or parent == "0" * 40):
                alternatives.append({"route": route, "state": "unavailable", "reason": "malformed expected parent"})
                continue
            if info.get("post_child_only") is not True:
                alternatives.append({"route": route, "state": "unavailable", "reason": "push could trigger before source-only child completion"})
                continue
        if phase == "validate":
            head, candidate, base = data.get("staging_sha"), info.get("candidate_sha"), info.get("required_author_base")
            if (not isinstance(head, str) or not SHA.fullmatch(head) or not isinstance(candidate, str) or not SHA.fullmatch(candidate)
                    or head == "0" * 40 or candidate == "0" * 40
                    or not isinstance(base, str) or not SHA.fullmatch(base) or base == "0" * 40 or base == candidate):
                alternatives.append({"route": route, "state": "unavailable", "reason": "exact current candidate SHA or author boundary unverified"})
                continue
            if route == "dispatch" and head != candidate:
                alternatives.append({"route": route, "state": "unavailable", "reason": "dispatch candidate is not current staging"})
                continue
            if route == "push" and (info.get("expected_parent") != head or info.get("planned_commit_verified") is not True
                                    or info.get("planned_commit_parent") != head or candidate == head):
                alternatives.append({"route": route, "state": "unavailable", "reason": "push needs current guarded parent and verified planned candidate commit"})
                continue
            if route == "push":
                message = info.get("candidate_message")
                try:
                    resolved = resolve_author_base("push", {"head_commit": {"message": message}, "before": head})
                    if resolved != base or (info.get("explicit_author_base") is True and "Candidate-Author-Base: " + base not in message.splitlines()):
                        raise ValueError("prepared message does not preserve the required author boundary")
                    if push_mode == "validation_request":
                        request_lines = [line for line in message.splitlines()
                                         if line.lstrip().lower().startswith("candidate-validation-request")]
                        canonical = "Candidate-Validation-Request: " + info["request"]["source_sha"]
                        if request_lines != [canonical] or "Candidate-Author-Base: " + base not in message.splitlines():
                            raise ValueError("require one canonical validation request and explicit author base trailer")
                except (ValueError, TypeError, AttributeError) as exc:
                    alternatives.append({"route": route, "state": "unavailable", "reason": "prepared push message invalid: " + str(exc)})
                    continue
        result = {"status": "qualified_route_plan" if phase == "entry" else "eligible_for_authorised_attempt", "route": route, "phase": phase,
                "trigger": wiring[route], "alternatives": alternatives,
                "limits": "Operator-supplied evidence checked; no live authentication/dispatch or candidate-ready implied. Recheck actual candidate inputs at validation, then require exact event/head executed job and final status/artifact. No merge."}
        if route == "push":
            result["push_mode"] = push_mode
        return result
    return blocked("no currently evidenced supported route", alternatives)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--resolve-author-base", action="store_true")
    parser.add_argument("--event", choices=("push", "workflow_dispatch"))
    parser.add_argument("--event-path", type=Path)
    parser.add_argument("--explicit-base")
    args = parser.parse_args()
    try:
        if args.resolve_author_base:
            if args.event_path is None or args.event is None:
                raise ValueError("boundary resolution requires event and event-path")
            print(resolve_author_base(args.event, strict_json(args.event_path.read_text(encoding="utf-8")), args.explicit_base))
            return 0
        if args.input is None:
            raise ValueError("route assessment requires --input")
        result = assess(strict_json(args.input.read_text(encoding="utf-8")), args.root)
    except (OSError, ValueError) as exc:
        result = {"status": "blocked", "reason": "unreadable input evidence: " + str(exc)}
    print(json.dumps(result, indent=2))
    return 0 if result["status"] in {"qualified_route_plan", "eligible_for_authorised_attempt"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
