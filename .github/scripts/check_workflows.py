#!/usr/bin/env python3
"""Validate Library workflow contracts. This is an admission check, not an executor."""
import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

from frontmatter_utils import parse_frontmatter
from record_paths import is_support_document

ROOT = Path(__file__).resolve().parents[2]
BLOCK = re.compile(r"(?ms)^```workflow-json\n(.*?)\n```[ \t]*(?=\n|$)")
VISUAL_START = "<!-- workflow-visual:start -->"
VISUAL_END = "<!-- workflow-visual:end -->"
VISUAL_BLOCK = re.compile(r"(?ms)^<!-- workflow-visual:start -->\n```mermaid\n.*?\n```\n<!-- workflow-visual:end -->[ \t]*(?=\n|$)")
ID = re.compile(r"(?:FLOW|PLAY|SKILL|HAT)-\d{4}")
POLICIES = ("AGENTS.md", "Workflows/README.md", "Workflows/_HOW-TO-CREATE.md",
            ".github/frontmatter-rules/workflow.json", ".github/scripts/check_workflows.py",
            ".github/scripts/frontmatter_utils.py", ".github/scripts/record_paths.py",
            ".github/workflow-resources.json")
ROOT_KEYS = {"schema_version", "purpose", "trigger", "scope", "non_goals", "inputs", "outputs",
             "authority", "completion", "persistence", "risks", "grill_me", "entry",
             "max_transitions", "failure_handling", "steps", "coverage", "dependencies", "pins", "policy_pins", "resource_pins", "tests", "gaps", "review"}
COMMON = {"id", "kind", "playbook", "owner", "actor_access", "scope", "prerequisites", "inputs", "outputs",
          "allowed_effects", "success_check", "recovery", "max_attempts", "controls"}
EXTRA = {"playbook": {"uses", "capabilities", "next", "failure"},
         "workflow": {"uses", "capabilities", "next", "failure", "return_policy", "budget_policy"},
         "decision": {"branches", "failure"}, "wait": {"resume_when", "timeout", "next", "failure"},
         "terminal": {"outcome"}}
RECOVERY_TARGET = "failed_step_continuation"
CANCELLATION_POLICY = "immediate_stop_acknowledgement"
RECOVERY_REFS = {"playbook": "PLAY-0069", "director": "HAT-0023", "coordinator": "HAT-0001"}
RECOVERY_TEXT = {"error_tracking", "repair_loop", "handback", "continuation", "child_return", "limits", "awaiting_steve"}
HANDOFF_KEYS = {"question", "why_needed", "investigated_options", "recommendation", "owner",
                "preserved_effects", "remaining_limits", "next_entry", "cancellation"}
INSTRUCTION_TYPES = {"workflow", "playbook", "skill", "aihat"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def object_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_contract(text):
    matches = list(BLOCK.finditer(text))
    if len(matches) != 1:
        raise ValueError("require exactly one workflow-json block")
    data = json.loads(matches[0][1], object_pairs_hook=object_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    if not isinstance(data, dict):
        raise ValueError("workflow contract must be an object")
    return data



def visual_label(value):
    """Quote data as Mermaid label text, never diagram syntax."""
    text = str(value).replace("\r", " ").replace("\n", " ")
    return text.replace("&", "#38;").replace('"', "#quot;").replace("<", "#60;").replace(">", "#62;").replace("|", "#124;")


def render_visual(spec):
    """Derive the declared graph and shared recovery obligations, not runtime proof.

    The conditional continuation is the root handler's admission obligation; it
    never grants permission, resets budgets, or asserts that repair will succeed.
    Review and hash metadata are intentionally absent to avoid fingerprint cycles.
    """
    rows = [row for row in spec.get("steps", []) if isinstance(row, dict)]
    lines = [VISUAL_START, "```mermaid", "flowchart TD"]
    lines.append('    E_start["Entry · global max_transitions: ' + visual_label(spec.get("max_transitions", "missing")) + '"]')
    entry = spec.get("entry")
    if isinstance(entry, str) and re.fullmatch(r"[a-z][a-z0-9_]*", entry):
        lines.append('    E_start --> S_' + entry)
    for row in rows:
        key, kind = row.get("id", "invalid"), row.get("kind", "invalid")
        if not isinstance(key, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", key):
            continue  # The contract validator rejects malformed identifiers.
        label = key + " · " + str(kind) + " · max_attempts: " + str(row.get("max_attempts", "missing"))
        if kind in {"playbook", "workflow"}:
            label += " · " + str(row.get("uses", "missing"))
        if kind == "workflow":
            label += " · completed child only; shared budgets"
        if kind == "wait":
            label += " · resume: " + str(row.get("resume_when", "missing")) + " · timeout: " + str(row.get("timeout", "missing"))
        if kind == "terminal":
            label = key + " · " + str(row.get("outcome", "missing")) + " · max_attempts: " + str(row.get("max_attempts", "missing"))
            lines.append('    S_' + key + '(["' + visual_label(label) + '"])')
        elif kind == "decision":
            lines.append('    S_' + key + '{"' + visual_label(label) + '"}')
        else:
            lines.append('    S_' + key + '["' + visual_label(label) + '"]')
    # A small top-down shared service makes error ownership and verified handback
    # visible without pretending that source admission executes these instructions.
    recovery = [
        ('R_issue', 'PLAY-0069 · record error and evidence'),
        ('R_director', 'HAT-0023 · investigate and design recovery'),
        ('R_head', 'HAT-0001 · assign the repair'),
        ('R_repair', 'Repair, test, independently review and record lesson'),
        ('R_handback', 'Hand verified repair back to executing AI'),
        ('R_gate', 'Qualified handback and continuation eligible? Reconcile effects; preserve limits')]
    for key, label in recovery:
        shape = '{"' + label + '"}' if key == "R_gate" else '["' + label + '"]'
        lines.append('    ' + key + shape)
    lines.extend([
        '    R_issue --> R_director',
        '    R_director --> R_head',
        '    R_head -->|"Permitted repair available"| R_repair',
        '    R_head -->|"Investigated; no permitted repair, access, input or remaining limit"| R_gate',
        '    R_repair -->|"Repair independently qualified"| R_handback',
        '    R_repair -->|"Unqualified; further investigation permitted within shared limits"| R_issue',
        '    R_repair -->|"Unqualified; no further permitted repair or investigation"| R_gate',
        '    R_handback --> R_gate'])
    # Cancellation is a global user interrupt, not an error requiring repair.
    awaiting = [row.get("id") for row in rows if row.get("kind") == "terminal" and row.get("outcome") == "awaiting_steve"]
    lines.extend([
        '    C_cancel["Global interrupt · Library owner cancels during any active state or recovery"]',
        '    C_ack["Immediately stop effects, preserve evidence and limits, acknowledge cancellation; no automatic retry"]',
        '    C_cancel --> C_ack'])
    if len(awaiting) == 1 and isinstance(awaiting[0], str) and re.fullmatch(r"[a-z][a-z0-9_]*", awaiting[0]):
        lines.append('    C_ack -->|"Library owner owns the next decision; preserve cancellation instruction"| S_' + awaiting[0])
    routes = set()
    for row in rows:
        key, kind = row.get("id"), row.get("kind")
        if not isinstance(key, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", key) or kind == "terminal":
            continue
        if kind == "decision":
            branches = row.get("branches", [])
            links = [(branch.get("when"), branch.get("to")) for branch in branches if isinstance(branch, dict)] if isinstance(branches, list) else []
        else:
            label = "Completed child" if kind == "workflow" else "Resume condition met" if kind == "wait" else "Success"
            links = [(label, row.get("next"))]
        for label, target in links:
            if isinstance(target, str) and re.fullmatch(r"[a-z][a-z0-9_]*", target):
                lines.append('    S_' + key + ' -->|"' + visual_label(label) + '"| S_' + target)
        failure_label = "Failure or noncompleted child; shared recovery first" if kind == "workflow" else "Failure or timeout; shared recovery first" if kind == "wait" else "Failure; shared recovery first"
        lines.append('    S_' + key + ' -->|"' + failure_label + '"| R_issue')
        lines.append('    R_gate -->|"Origin ' + key + ': verified qualified handback; same active component; only within existing authority and remaining bounds"| S_' + key)
        target = row.get("failure")
        if isinstance(target, str) and re.fullmatch(r"[a-z][a-z0-9_]*", target):
            routes.add((key, target))
    for key, target in sorted(routes):
        lines.append('    R_gate -->|"Unresolved ' + key + ': declared failure route after investigation"| S_' + target)
    lines.extend(["```", VISUAL_END])
    return "\n".join(lines)


def visual_errors(text, spec):
    matches = list(VISUAL_BLOCK.finditer(text))
    if (text.count(VISUAL_START) != 1 or text.count(VISUAL_END) != 1 or len(matches) != 1
            or len(re.findall(r"(?m)^```mermaid[ \t]*$", text)) != 1):
        return ["require exactly one generated workflow visual region with one Mermaid block"]
    if matches[0].group(0) != render_visual(spec):
        return ["workflow visual is stale or tampered; regenerate from the exact contract"]
    return []


def fingerprint(text, contract):
    """Bind review to prose, metadata and contract; exclude only the review receipt."""
    unsigned = {key: value for key, value in contract.items() if key != "review"}
    encoded = json.dumps(unsigned, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    match = BLOCK.search(text)
    return digest((text[:match.start(1)] + encoded + text[match.end(1):]).encode("utf-8"))


def canonical_repo_parts(value):
    """Return canonical repository-relative POSIX path parts."""
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    parts = value.split("/")
    if any(not part or part in {".", ".."} for part in parts):
        return None
    if re.match(r"^[A-Za-z]:", parts[0]):
        return None
    path = PurePosixPath(*parts)
    if path.is_absolute() or path.as_posix() != value:
        return None
    return parts


def safe_file(root, value):
    parts = canonical_repo_parts(value)
    if parts is None:
        return None
    target = root.joinpath(*parts)
    try:
        target.resolve().relative_to(root.resolve())
    except (ValueError, OSError):
        return None
    return target if (target.is_file() and not any(
        root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))) else None


def resource_errors(spec, identity, root):
    """A reviewed finite registry owns the exact native/control-resource union."""
    target = safe_file(root, ".github/workflow-resources.json")
    try:
        registry = json.loads(target.read_text(encoding="utf-8"), object_pairs_hook=object_pairs) if target else None
    except (ValueError, OSError):
        registry = None
    version = registry.get("schema_version") if isinstance(registry, dict) else None
    keys = {"schema_version", "workflows"} | ({"native_fixture_sources"} if version == 2 else set())
    if (not isinstance(registry, dict) or set(registry) != keys
            or version not in (1, 2) or isinstance(version, bool)
            or not isinstance(registry.get("workflows"), dict)):
        return ["resource registry malformed or absent"]
    flows = registry["workflows"]
    native = registry.get("native_fixture_sources", [])
    if (not isinstance(native, list) or not all(isinstance(key, str) for key in native)
            or len(native) != len(set(native))):
        return ["native fixture sources must be a unique string list"]
    for key in native:
        # A reviewed executable test source is control code, not an operational
        # Artifact output. Explicit declaration never exempts its exact hash.
        if (not re.fullmatch(r"Artifacts/ART-\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*\.(?:js|py)", key)
                or safe_file(root, key) is None
                or not any(isinstance(paths, list) and key in paths for paths in flows.values())):
            return ["native fixture source must be canonical executable Artifact code used by a workflow: " + key]
    if any(not re.fullmatch(r"FLOW-\d{4}", str(key)) for key in flows):
        return ["resource registry has a malformed workflow identity"]
    if identity not in flows:
        return ["resource registry lacks workflow: " + identity]
    paths = flows[identity]
    if (not isinstance(paths, list) or not all(isinstance(key, str) for key in paths)
            or len(paths) != len(set(paths))):
        return ["resource registry paths must be a unique string list"]
    pins = spec.get("resource_pins")
    if not isinstance(pins, dict):
        return ["resource_pins must be a hash map"]
    errors = []
    if set(pins) != set(paths):
        errors.append("resource_pins must exactly cover this workflow's registered resources")
    for key in paths:
        path = safe_file(root, key)
        parts = Path(key).parts
        support = (path is not None and len(parts) == 2
                   and ((path.name == "README.md" and not parse_frontmatter(path.read_text(encoding="utf-8")))
                        or is_support_document(path)))
        mutable = ((key.startswith(("Tickets/", "Projects/", "Planning/", "People/", "Chats/", "Artifacts/", "Catalog/"))
                    and not support and key not in native)
                   or key in {".github/id-reservations.json", ".github/deleted-ids.json"})
        if mutable or key in POLICIES or path is None:
            errors.append("resource must be a canonical immutable control, not policy or mutable run input: " + key)
        elif pins.get(key) != digest(path.read_bytes()):
            errors.append("stale resource pin: " + key)
    return errors


def text_value(value):
    return isinstance(value, str) and bool(value.strip()) and not re.search(r"<[^>]+>|\bTODO\b", value)


def strings(value, nonempty=True):
    return isinstance(value, list) and (bool(value) or not nonempty) and all(text_value(x) for x in value)


def integer(value, low, high):
    return isinstance(value, int) and not isinstance(value, bool) and low <= value <= high


def collect(root):
    mapping = json.loads((root / ".github/type-prefixes.json").read_text())["folders"]
    entries = {}
    for folder in mapping:
        for path in sorted((root / folder).glob("*.md")):
            if path.name in {"README.md", "index.md"} or is_support_document(path):
                continue
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if fm and fm.get("id"):
                if fm["id"] in entries:
                    raise ValueError("duplicate record: " + fm["id"])
                entries[fm["id"]] = {"path": path, "text": text, "fm": fm}
    return entries


def instruction_closure(seeds, entries, manifest):
    """Declared executable dependencies; navigation links do not imply execution."""
    if not isinstance(manifest, dict):
        raise ValueError("dependencies must be an explicit ID-to-ID-list map")
    for key, values in manifest.items():
        if (not ID.fullmatch(str(key)) or not isinstance(values, list)
                or len(set(str(x) for x in values)) != len(values)
                or not all(ID.fullmatch(str(x)) for x in values)):
            raise ValueError("malformed executable dependencies: " + str(key))
    result, queue = set(), list(seeds)
    while queue:
        key = queue.pop()
        if key in result:
            continue
        if key not in entries:
            raise ValueError("missing dependency: " + str(key))
        if key not in manifest:
            raise ValueError("missing dependency declaration: " + str(key))
        row = entries[key]
        if row["fm"].get("type") not in INSTRUCTION_TYPES:
            raise ValueError("dependency is not an instruction record: " + key)
        result.add(key)
        queue.extend(manifest[key])
        if row["fm"].get("type") == "workflow":
            nested = load_contract(row["text"])
            required = {"SKILL-0318", *RECOVERY_REFS.values()}
            for step in nested.get("steps", []):
                if not isinstance(step, dict):
                    raise ValueError("malformed nested workflow step: " + key)
                required.add(step.get("owner"))
                required.add(step.get("playbook"))
                if step.get("kind") in {"playbook", "workflow"}:
                    required.add(step.get("uses"))
                    required.update(step.get("capabilities", []))
            if not required.issubset(set(manifest[key])):
                raise ValueError("nested workflow dependencies omitted: " + key)
            for dependency, values in nested.get("dependencies", {}).items():
                if dependency not in manifest or set(manifest[dependency]) != set(values):
                    raise ValueError("nested dependency manifest disagrees: " + dependency)
    if set(manifest) != result:
        raise ValueError("dependency declarations must exactly cover reachable dependencies")
    return result


def support_coverage(spec, steps, entries, root, approved, closure):
    """Check declared requirement coverage; non-author review establishes adequacy."""
    errors, seeds = [], set()
    coverage = spec.get("coverage")
    if not isinstance(coverage, dict):
        return ["coverage must map Playbook IDs to requirement evidence"], seeds
    playbooks = {key for key in closure if entries[key]["fm"].get("type") == "playbook"}
    if set(coverage) - playbooks or (approved and set(coverage) != playbooks):
        errors.append("Playbook coverage must match every directly or transitively executed Playbook")
    covered = set()
    owner_covered = set()
    dependencies = spec.get("dependencies")
    def called_from(key, target):
        starts = {steps[key]["playbook"], RECOVERY_REFS["playbook"]}
        if steps[key].get("kind") in {"playbook", "workflow"}:
            starts.add(steps[key]["uses"])
        seen, queue = set(), list(starts)
        while queue:
            current = queue.pop()
            if current == target:
                return True
            if current not in seen:
                seen.add(current)
                queue.extend(dependencies.get(current, []))
        return False
    for playbook, requirements in coverage.items():
        if playbook not in playbooks:
            continue
        if not isinstance(requirements, list) or not requirements:
            errors.append(playbook + ": supporting Skill requirements must be nonempty")
            continue
        for row in requirements:
            if (not isinstance(row, dict) or set(row) != {"requirement", "steps", "skills", "status", "evidence"}
                    or not text_value(row.get("requirement"))
                    or not isinstance(row.get("steps"), list) or not row["steps"]
                    or not all(isinstance(key, str) and key in steps and called_from(key, playbook) for key in row["steps"])
                    or not isinstance(row.get("skills"), list)
                    or not all(re.fullmatch(r"SKILL-\d{4}", str(key)) for key in row["skills"])
                    or row.get("status") not in {"verified", "gap"}):
                errors.append(playbook + ": malformed supporting Skill coverage")
                continue
            covered.update(row["steps"])
            owner_covered.update(key for key in row["steps"] if steps[key]["playbook"] == playbook)
            seeds.update(row["skills"])
            dependencies = spec.get("dependencies")
            declared = dependencies.get(playbook, []) if isinstance(dependencies, dict) else []
            if not set(row["skills"]).issubset(set(declared)):
                errors.append(playbook + ": supporting Skills must be declared Playbook dependencies")
            for key in row["skills"]:
                if key not in entries or entries[key]["fm"].get("type") != "skill":
                    errors.append(playbook + ": supporting Skill unavailable or wrong type: " + key)
                elif approved or row["status"] == "verified":
                    if entries[key]["fm"].get("status") != "current":
                        errors.append(playbook + ": supporting Skill is superseded: " + key)
                    play_links = entries[playbook]["fm"].get("links", [])
                    skill_links = entries[key]["fm"].get("links", [])
                    if not isinstance(play_links, list) or not isinstance(skill_links, list) or key not in play_links or playbook not in skill_links:
                        errors.append(playbook + ": supporting Skill association must be canonical and reciprocal: " + key)
            if row["status"] == "verified" and (not row["skills"] or not evidence(row["evidence"], root)):
                errors.append(playbook + ": verified support requires Skills and current hashed evidence")
            if approved and (row["status"] != "verified" or not row["skills"]):
                errors.append(playbook + ": supporting Skills incomplete; resolve gap before approval")
    if approved and (covered != set(steps) or owner_covered != set(steps)):
        errors.append("supporting Skill coverage must include every step/control state")
    return errors, seeds


def validate(path, entries, root, require_approved=False):
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text) or {}
    errors = []
    def fail(message):
        errors.append(message)
    try:
        spec = load_contract(text)
    except (ValueError, TypeError) as exc:
        return [str(exc)]
    errors.extend(visual_errors(text, spec))
    if set(spec) != ROOT_KEYS:
        fail("contract keys differ: " + str(sorted(set(spec) ^ ROOT_KEYS)))
    if spec.get("schema_version") != 1 or isinstance(spec.get("schema_version"), bool):
        fail("schema_version must be 1")
    for key in ("purpose", "trigger", "scope", "authority", "completion", "persistence", "entry"):
        if not text_value(spec.get(key)):
            fail(key + " must be explicit text without placeholders")
    for key in ("non_goals", "inputs", "outputs", "risks"):
        if not strings(spec.get(key)):
            fail(key + " must be a nonempty text list")
    if spec.get("grill_me") != "SKILL-0318":
        fail("grill_me must name SKILL-0318")
    if not integer(spec.get("max_transitions"), 1, 10000):
        fail("max_transitions must bound a run (1..10000)")
    handling = spec.get("failure_handling")
    if (not isinstance(handling, dict) or set(handling) != set(RECOVERY_REFS) | RECOVERY_TEXT | {"continuation_target", "cancellation_policy"}
            or handling.get("continuation_target") != RECOVERY_TARGET
            or handling.get("cancellation_policy") != CANCELLATION_POLICY
            or any(handling.get(key) != value for key, value in RECOVERY_REFS.items())
            or any(not text_value(handling.get(key)) for key in RECOVERY_TEXT)):
        fail("failure_handling must bind PLAY-0069, HAT-0023 and HAT-0001 with explicit recovery, handback, child-return, limits, failed_step_continuation, immediate cancellation acknowledgement and Library owner escalation instructions")
    state = fm.get("review_status")
    if state not in {"draft", "needs_review", "approved"}:
        fail("review_status must be draft, needs_review or approved")
    approved = state == "approved" and fm.get("status") == "current"
    if require_approved and not approved:
        fail("workflow is not current and approved")
    if fm.get("type") != "workflow" or not re.fullmatch(r"FLOW-\d{4}", str(fm.get("id"))):
        fail("workflow must have a concrete FLOW identity and type workflow")
    if not text_value(fm.get("owner")) or not strings(fm.get("trigger_phrases")):
        fail("owner and trigger_phrases are required")
    rows = spec.get("steps")
    if not isinstance(rows, list) or not rows:
        return errors + ["steps must be a nonempty list"]
    steps, edges, seeds = {}, {}, {"SKILL-0318", *RECOVERY_REFS.values()}
    for row in rows:
        if not isinstance(row, dict):
            fail("each step must be an object")
            continue
        key, kind = row.get("id"), row.get("kind")
        if not isinstance(key, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", key) or key in steps:
            fail("step IDs must be unique lowercase names")
            continue
        steps[key] = row
        if kind not in EXTRA:
            fail(key + ": unknown step kind")
            continue
        extra = EXTRA[kind] | ({"handoff"} if kind == "terminal" and row.get("outcome") == "awaiting_steve" else set())
        if set(row) != COMMON | extra:
            fail(key + ": missing or unknown step fields")
        for field in ("actor_access", "scope", "success_check", "recovery"):
            if not text_value(row.get(field)):
                fail(key + ": missing " + field)
        for field in ("prerequisites", "inputs", "outputs", "allowed_effects"):
            if not strings(row.get(field)):
                fail(key + ": missing " + field)
        if not re.fullmatch(r"HAT-\d{4}", str(row.get("owner"))):
            fail(key + ": owner must be a Hat ID")
        else:
            seeds.add(row["owner"])
        playbook = row.get("playbook")
        if not isinstance(playbook, str) or not re.fullmatch(r"PLAY-\d{4}", playbook):
            fail(key + ": every step/control state must name its governing Playbook")
        elif playbook not in entries or entries[playbook]["fm"].get("type") != "playbook":
            fail(key + ": governing Playbook unavailable or wrong type: " + playbook)
        else:
            seeds.add(playbook)
        if kind == "playbook" and row.get("uses") != playbook:
            fail(key + ": executable step must use its governing Playbook")
        if not integer(row.get("max_attempts"), 1, 3):
            fail(key + ": max_attempts must be 1..3; retries require changed evidence/input")
        controls = row.get("controls")
        if not isinstance(controls, list) or not controls:
            fail(key + ": controls required")
        else:
            for control in controls:
                if (not isinstance(control, dict) or set(control) != {"requirement", "mode", "evidence", "critical"}
                        or not text_value(control.get("requirement"))
                        or control.get("mode") not in {"enforced", "instruction", "unverified"}
                        or not text_value(control.get("evidence"))
                        or not isinstance(control.get("critical"), bool)):
                    fail(key + ": malformed control")
                elif approved and control["critical"] and control["mode"] == "unverified":
                    fail(key + ": critical control remains unverified")
        targets = []
        if kind in {"playbook", "workflow"}:
            prefix = "PLAY" if kind == "playbook" else "FLOW"
            if not re.fullmatch(prefix + r"-\d{4}", str(row.get("uses"))):
                fail(key + ": uses must name the matching record type")
            else:
                seeds.add(row["uses"])
                if row["uses"] in entries and entries[row["uses"]]["fm"].get("type") != kind:
                    fail(key + ": referenced record has the wrong type")
            capabilities = row.get("capabilities")
            if not isinstance(capabilities, list) or not all(ID.fullmatch(str(x)) for x in capabilities):
                fail(key + ": capabilities must be an ID list")
            else:
                seeds.update(capabilities)
        if kind == "workflow":
            if row.get("return_policy") != "completed_only" or row.get("budget_policy") != "shared":
                fail(key + ": subprocess must return completed_only with shared budgets")
        if kind == "decision":
            branches = row.get("branches")
            if (not isinstance(branches, list) or len(branches) < 2
                    or any(not isinstance(b, dict) or set(b) != {"when", "to"}
                           or not text_value(b.get("when")) for b in branches)):
                fail(key + ": decision needs explicit branches including one otherwise")
            else:
                if sum(b["when"] == "otherwise" for b in branches) != 1:
                    fail(key + ": decision requires exactly one otherwise branch")
                targets.extend(b["to"] for b in branches)
        elif kind == "terminal":
            if row.get("outcome") not in {"completed", "awaiting_steve"}:
                fail(key + ": invalid terminal outcome; only completed or awaiting_steve is permitted")
            if row.get("outcome") == "awaiting_steve":
                handoff = row.get("handoff")
                if (not isinstance(handoff, dict) or set(handoff) != HANDOFF_KEYS
                        or any(not text_value(handoff.get(field)) for field in HANDOFF_KEYS)
                        or handoff.get("owner") != "Library owner"):
                    fail(key + ": awaiting_steve requires the complete actionable Library owner-owned handoff contract")
        else:
            targets.append(row.get("next"))
        if kind != "terminal":
            targets.append(row.get("failure"))
        if kind == "wait":
            if not text_value(row.get("resume_when")) or not text_value(row.get("timeout")):
                fail(key + ": wait needs evidence-based resume and bounded timeout")
        if any(not isinstance(target, str) for target in targets):
            fail(key + ": transition targets must be state IDs")
        edges[key] = [x for x in targets if isinstance(x, str)]
    if errors:
        return errors
    for key, targets in edges.items():
        if any(target not in steps for target in targets):
            fail(key + ": dangling transition")
    if spec["entry"] not in steps:
        fail("entry state missing")
    if errors:
        return errors
    reachable, pending = set(), [spec["entry"]]
    while pending:
        key = pending.pop()
        if key not in reachable:
            reachable.add(key)
            pending.extend(edges[key])
    if reachable != set(steps):
        fail("unreachable states: " + str(sorted(set(steps) - reachable)))
    terminals = [row for row in steps.values() if row["kind"] == "terminal"]
    if len(terminals) != 2 or {row.get("outcome") for row in terminals} != {"completed", "awaiting_steve"}:
        fail("exactly two terminal nodes are required: one completed and one awaiting_steve")
    for key, row in steps.items():
        # The contract requires the operator to invoke shared recovery first;
        # this checker validates that declaration, not runtime interception.
        target = steps.get(row.get("failure")) if row["kind"] != "terminal" else None
        if target and target["kind"] == "terminal" and target.get("outcome") == "completed":
            fail(key + ": failure cannot transition directly to completed; invoke shared recovery before routing")
    can_exit = {key for key, row in steps.items() if row["kind"] == "terminal"}
    while True:
        expanded = can_exit | {key for key, targets in edges.items() if any(t in can_exit for t in targets)}
        if expanded == can_exit:
            break
        can_exit = expanded
    if can_exit != set(steps):
        fail("states with no terminal path")
    # A global transition budget applies even to cycles spanning several states.
    coverage = spec.get("coverage")
    if isinstance(coverage, dict):
        for requirements in coverage.values():
            if isinstance(requirements, list):
                for requirement in requirements:
                    if isinstance(requirement, dict) and isinstance(requirement.get("skills"), list):
                        seeds.update(key for key in requirement["skills"]
                                     if isinstance(key, str) and re.fullmatch(r"SKILL-\d{4}", key))
    try:
        closure = instruction_closure(seeds, entries, spec.get("dependencies"))
    except ValueError as exc:
        return errors + [str(exc)]
    coverage_errors, skill_seeds = support_coverage(spec, steps, entries, root, approved, closure)
    errors.extend(coverage_errors)
    seeds.update(skill_seeds)
    links = fm.get("links")
    if not isinstance(links, list) or not seeds.issubset(set(links)):
        fail("frontmatter links must include all direct instruction references")
    gaps = spec.get("gaps")
    if not isinstance(gaps, list) or (approved and gaps):
        fail("gaps must be a list, empty for approval")
    for key in ("pins", "policy_pins", "resource_pins"):
        if not isinstance(spec.get(key), dict):
            fail(key + " must be a hash map")
    if errors or not approved:
        return errors
    if not text_value(fm.get("author")):
        fail("approval needs the author's identity")
    pins = spec.get("pins", {})
    if set(pins) != closure:
        fail("pins must cover exactly the transitive instruction dependency set")
    for key in closure:
        row = entries[key]
        if row["fm"].get("status") != "current":
            fail("dependency is superseded: " + key)
        if row["fm"].get("type") == "workflow" and row["fm"].get("review_status") != "approved":
            fail("nested workflow is not approved: " + key)
        if pins.get(key) != digest(row["path"].read_bytes()):
            fail("stale dependency pin: " + key)
    policies = spec.get("policy_pins", {})
    if not set(POLICIES).issubset(policies):
        fail("policy_pins must cover the required policy/checker files")
    # Extra context binds current canonical instructions without declaring them
    # executable. Completeness still needs independent semantic review.
    kinds = {"aihat": ("AIHats", "HAT"), "playbook": ("Playbooks", "PLAY"),
             "skill": ("Skills", "SKILL")}
    context = {}
    for row in entries.values():
        folder, prefix = kinds.get(row["fm"].get("type"), (None, None))
        identity = str(row["fm"].get("id", ""))
        relative = row["path"].relative_to(root)
        if (folder and re.fullmatch(prefix + r"-\d{4}", identity)
                and relative.parent.as_posix() == folder
                and re.fullmatch(re.escape(identity) + r"-[a-z0-9]+(?:-[a-z0-9]+)*\.md", relative.name)):
            context[relative.as_posix()] = row
    for key in set(POLICIES) | set(policies):
        target = safe_file(root, key)
        if key not in POLICIES:
            row = context.get(key)
            if target is None or row is None or row["fm"].get("status") != "current":
                fail("policy context must be a current canonical Hat, Playbook or Skill: " + key)
        if target is None or policies.get(key) != digest(target.read_bytes()):
            fail("stale or absent policy pin: " + key)
    errors.extend(resource_errors(spec, fm["id"], root))
    tests = spec.get("tests")
    if not isinstance(tests, list) or {t.get("kind") for t in tests if isinstance(t, dict)} != {"normal", "failure", "boundary"}:
        fail("normal, failure and boundary test evidence required")
    elif any(not evidence(row, root) for row in tests):
        fail("test evidence must be a current hashed repository file with PASS result")
    review = spec.get("review")
    if not isinstance(review, dict) or set(review) != {"reviewer", "verdict", "definition_sha256", "scores", "evidence"}:
        return errors + ["independent review receipt malformed"]
    if not text_value(review["reviewer"]) or review["reviewer"].strip().casefold() == str(fm.get("author", "")).strip().casefold():
        fail("independent reviewer must differ from author")
    if review["verdict"] != "PASS" or review["definition_sha256"] != fingerprint(text, spec):
        fail("review must PASS the exact current definition")
    scores = review["scores"]
    maxima = {"requirements": 30, "evidence": 30, "feasibility": 20, "verification": 20}
    if (not isinstance(scores, dict) or set(scores) != set(maxima)
            or any(not integer(scores[k], 0, maxima[k]) for k in maxima)
            or sum(scores.values()) < 95):
        fail("review rubric must be valid and total at least 95; it grants no authority")
    if not evidence(review["evidence"], root):
        fail("review evidence missing or stale")
    return errors


def evidence(row, root):
    if not isinstance(row, dict) or not {"path", "sha256", "result"}.issubset(row) or row["result"] != "PASS":
        return False
    target = safe_file(root, row["path"])
    if target is None:
        return False
    parts = target.relative_to(root).parts
    mutable_folders = set(json.loads((root / ".github/type-prefixes.json").read_text())["folders"])
    mutable_folders.update({"Tickets", "Projects", "Planning", "People", "Chats", "Artifacts"})
    support = (len(parts) == 2 and ((target.name == "README.md" and not parse_frontmatter(target.read_text(encoding="utf-8")))
                                   or is_support_document(target)))
    if parts[0] in mutable_folders and not support:
        return False
    return row["sha256"] == digest(target.read_bytes())


def planned_write_errors(root, entries, identity, writes):
    """Read-only preflight: planned effects cannot overwrite their own controls/proof."""
    if not writes:
        return []
    if not identity or identity not in entries:
        return ["planned writes require a current admitted workflow identity"]
    frozen, seen, queue = set(), set(), [identity]
    try:
        while queue:
            key = queue.pop()
            if key in seen:
                continue
            seen.add(key)
            row = entries[key]
            frozen.add(row["path"].relative_to(root).as_posix())
            spec = load_contract(row["text"])
            frozen.update(spec["policy_pins"])
            frozen.update(spec["resource_pins"])
            for component in spec["pins"]:
                target = entries[component]
                frozen.add(target["path"].relative_to(root).as_posix())
                if target["fm"].get("type") == "workflow":
                    queue.append(component)
            proof = list(spec["tests"]) + [spec.get("review", {}).get("evidence", {})]
            proof += [coverage.get("evidence", {}) for rows in spec["coverage"].values() for coverage in rows]
            frozen.update(value["path"] for value in proof if isinstance(value, dict) and isinstance(value.get("path"), str))
    except (KeyError, TypeError, ValueError):
        return ["cannot establish complete frozen control/evidence set"]
    errors = []
    for value in writes:
        parts = canonical_repo_parts(value)
        if parts is None:
            errors.append("unsafe planned write path: " + str(value))
            continue
        target = root.joinpath(*parts)
        try:
            target.resolve().relative_to(root.resolve())
            safe = (not target.is_dir()
                    and not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1)))
        except (ValueError, OSError):
            safe = False
        if not safe:
            errors.append("unsafe planned write path: " + value)
        elif value in frozen:
            errors.append("planned write overlaps frozen workflow control or qualification evidence: " + value)
    return errors


def check_repository(root=ROOT, require_id=None, planned_writes=None):
    entries = collect(root)
    errors, calls = [], {}
    for key, row in entries.items():
        if row["fm"].get("type") != "workflow":
            continue
        relative = row["path"].relative_to(root).as_posix()
        errors.extend(relative + ": " + error for error in validate(
            row["path"], entries, root, require_id == key))
        try:
            spec = load_contract(row["text"])
            calls[key] = [step["uses"] for step in spec.get("steps", [])
                          if isinstance(step, dict) and step.get("kind") == "workflow" and isinstance(step.get("uses"), str)]
        except (ValueError, TypeError):
            continue
    if require_id and (require_id not in entries or entries[require_id]["fm"].get("type") != "workflow"):
        errors.append("requested workflow not found: " + require_id)
    visited, active = set(), set()
    def visit(key):
        if key in active:
            errors.append("recursive workflow calls: " + key)
            return
        if key in visited:
            return
        active.add(key)
        for target in calls.get(key, []):
            visit(target)
        active.remove(key)
        visited.add(key)
    for key in calls:
        visit(key)
    errors.extend(planned_write_errors(root, entries, require_id, planned_writes))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--require-approved", metavar="FLOW_ID")
    parser.add_argument("--planned-write", action="append", default=[], metavar="CANONICAL_PATH")
    args = parser.parse_args(argv)
    try:
        errors = check_repository(args.root, args.require_approved, args.planned_write)
    except (ValueError, OSError, TypeError, KeyError) as exc:
        errors = [str(exc)]
    for error in errors:
        print("WORKFLOW FAIL: " + error)
    if not errors:
        print("Workflow source contracts clean; no execution or independent factual certification implied.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
