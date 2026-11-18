#!/usr/bin/env python3
"""
Shared frontmatter rule-loading and validation logic, used by both
check_schema.py (scoped changes) and validate_repo_state.py (complete
candidate state). Kept as one module so the two
checks can never silently diverge on what counts as valid.
"""
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
RULES_DIR = REPO_ROOT / ".github" / "frontmatter-rules"


def load_rules(name: str) -> dict:
    data = json.loads((RULES_DIR / name).read_text())
    if data.get("extends") == "base":
        base = json.loads((RULES_DIR / "base.json").read_text())
        merged = dict(base)
        merged.update({k: v for k, v in data.items() if k != "extends"})
        return merged
    return data


def load_folder_map() -> dict:
    return json.loads((RULES_DIR / "folder-map.json").read_text())["folders"]


def validate_entry_frontmatter(fm: dict, rules: dict) -> list:
    """Returns a list of violation strings (empty if clean) for one
    entry's frontmatter against its type's rules."""
    violations = []

    for field in rules.get("required", []):
        value = fm.get(field, "__MISSING__")
        if value == "__MISSING__":
            violations.append(f"missing required field '{field}'.")
        elif value is None and field != "links":
            violations.append(f"required field '{field}' is null.")
        elif field == "tags" and value == []:
            violations.append(
                "'tags' is present but empty. Per §4b, tags are mandatory — "
                "unlike 'links', which may legitimately be empty for a new "
                "entry with no relations yet."
            )

    status = fm.get("status")
    status_enum = rules.get("status_enum")
    if status_enum and status not in status_enum:
        violations.append(f"status '{status}' is not one of {status_enum}.")

    work_state = fm.get("work_state")
    work_state_enum = rules.get("work_state_enum")
    if work_state_enum and work_state is not None and work_state not in work_state_enum:
        violations.append(f"work_state '{work_state}' is not one of {work_state_enum}.")

    priority = fm.get("priority")
    priority_enum = rules.get("priority_enum")
    if priority_enum and priority is not None and priority not in priority_enum:
        violations.append(f"priority '{priority}' is not one of {priority_enum}.")

    effort = fm.get("effort")
    effort_enum = rules.get("effort_enum")
    if effort_enum and effort is not None and effort not in effort_enum:
        violations.append(f"effort '{effort}' is not one of {effort_enum}.")

    work_class = fm.get("work_class")
    work_class_enum = rules.get("work_class_enum")
    if work_class_enum and work_class is not None and work_class not in work_class_enum:
        violations.append(f"work_class '{work_class}' is not one of {work_class_enum}.")

    transcript_status = fm.get("transcript_status")
    transcript_status_enum = rules.get("transcript_status_enum")
    if transcript_status_enum and transcript_status not in transcript_status_enum:
        violations.append(
            f"transcript_status '{transcript_status}' is not one of {transcript_status_enum}."
        )

    link_review_status = fm.get("link_review_status")
    link_review_status_enum = rules.get("link_review_status_enum")
    if link_review_status_enum and link_review_status not in link_review_status_enum:
        violations.append(
            f"link_review_status '{link_review_status}' is not one of {link_review_status_enum}."
        )

    op = rules.get("operating_fields_when_status_in")
    if op and status in op["statuses"]:
        for field in op["fields"]:
            if field not in fm:
                violations.append(
                    f"status '{status}' requires operating field '{field}' "
                    f"(present, even if null) — per §4."
                )

    return violations
