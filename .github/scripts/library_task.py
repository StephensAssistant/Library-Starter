#!/usr/bin/env python3
"""Read-only, task-specific Library entry contract; never validates a candidate."""
import argparse
import json
from pathlib import Path
import re
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import schema_rules
from frontmatter_utils import parse_frontmatter

ROOT = SCRIPT_DIR.parents[1]
WORK_FOLDERS = {"Projects", "Tickets"}


def local_file(root, value, required=True):
    """Return a repository-relative file, rejecting traversal and escapes."""
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"unsafe repository path: {value}")
    target = root / path
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes repository: {value}") from exc
    if not target.is_file():
        if required:
            raise ValueError(f"required file missing: {value}")
        return None
    return path.as_posix()


def task_contract(folder, action, record=None, root=ROOT):
    root = Path(root)
    folders = schema_rules.load_folder_map()
    if folder not in set(folders) | {"Chats"}:
        raise ValueError(f"unsupported governed folder: {folder}")
    if action not in {"create", "update", "close"}:
        raise ValueError(f"unsupported action: {action}")
    if action == "close" and folder not in WORK_FOLDERS:
        raise ValueError("close supports Projects and Tickets only")
    if action != "create" and not record:
        raise ValueError("update and close require --record")
    if action == "create" and record:
        raise ValueError("create does not accept --record; search before reserving an ID")
    control = local_file(root, "AGENTS.md")
    reads = [control, local_file(root, f"{folder}/README.md")]
    guides = {"create": ["_HOW-TO-CREATE.md", "_TEMPLATE.md"], "close": ["_HOW-TO-CLOSE.md"], "update": []}
    for name in guides[action]:
        existing = local_file(root, f"{folder}/{name}", required=False)
        if existing:
            reads.append(existing)
    rules_path = local_file(root, ".github/OPERATING-RULES.md")
    sections = ["folder-entry-gate", "file-formats", "filing-and-ids", "metadata-and-discovery", "session-discipline"]
    if folder in WORK_FOLDERS:
        sections.append("work-evidence-and-completion")
    if folder == "Artifacts":
        sections.append("relationships-and-healing")
    if folder in {"Skills", "Playbooks", "AIHats", "Workflows"}:
        sections.extend(["playbook-skill-and-context", "hat-routing"])
    headings = {
        re.sub(r"[^\w -]", "", heading.strip().lower()).replace(" ", "-")
        for heading in re.findall(r"(?m)^#{1,6}\s+(.+)$", (root / rules_path).read_text())
    }
    if set(sections) - headings:
        raise ValueError("missing operating-rule sections: " + ", ".join(sorted(set(sections) - headings)))
    result = {
        "folder": folder, "action": action, "read": reads,
        "execution_control": f"{control}#minimum-necessary-action-control",
        "rules_sections": [f"{rules_path}#{section}" for section in sections],
        "validation": "NOT RUN: this contract supplies requirements, not a passing receipt",
        "identity": "Search for an existing canonical record first; reserve each required prefix through the serialized Reserve permanent IDs workflow on staging" if action == "create" else "Reuse existing IDs; no new reservation for this record",
        "checkpoint": "PLAY-0056: authorized staged candidate and exact-SHA validation",
        "merge": "PLAY-0055: separate explicit merge authorization required",
    }
    if folder in folders:
        schema_name = folders[folder]
        local_file(root, f".github/frontmatter-rules/{schema_name}")
        rules = schema_rules.load_rules(schema_name)
        result["schema"] = f".github/frontmatter-rules/{schema_name}"
        result["requirements"] = {
            key: value for key, value in rules.items()
            if key == "required" or key.startswith("operating_fields") or key.endswith("_enum")
        }
    else:
        result["format"] = "Daily Chat blocks governed by Chats/README.md; no per-entry frontmatter"
    entry_id = None
    if record:
        relative = local_file(root, record)
        resolved = (root / relative).resolve()
        try:
            resolved.relative_to((root / folder).resolve())
        except ValueError as exc:
            raise ValueError("record must belong to the selected folder") from exc
        if Path(relative).parts[0] != folder or resolved.suffix != ".md" or resolved.name in {"README.md", "index.md"} or resolved.name.startswith("_"):
            raise ValueError("record must be a Markdown record in the selected folder")
        reads.append(relative)
        if folder != "Chats":
            metadata = parse_frontmatter(resolved.read_text())
            entry_id = metadata.get("id") if metadata else None
            if not isinstance(entry_id, str) or not re.fullmatch(r"(?:PROJ|TICK|KNOW|PERS|DEC|ART|PLAY|SKILL|HAT|FLOW|TRAN)-\d{4}", entry_id):
                raise ValueError("record has no valid stable ID")
            result["existing_id"] = entry_id
    if folder in WORK_FOLDERS:
        plan_path = f"Planning/{entry_id}.md" if entry_id else None
        existing_plan = local_file(root, plan_path, required=False) if plan_path else None
        if existing_plan:
            reads.append(local_file(root, "Planning/README.md"))
            reads.append(existing_plan)
        result["plan"] = {
            "path": existing_plan,
            "action": "Update the existing companion" if existing_plan else "Use an inline Work plan checklist; a separate linked plan is optional for substantial work",
            "authority": "Parent owns status and next action; verify reciprocal Parent and Live plan pointers using Planning/README.md",
        }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", required=True)
    parser.add_argument("--action", choices=("create", "update", "close"), required=True)
    parser.add_argument("--record")
    args = parser.parse_args(argv)
    try:
        result = task_contract(args.folder, args.action, args.record)
    except (OSError, ValueError, KeyError) as exc:
        print(f"LIBRARY TASK FAIL: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
