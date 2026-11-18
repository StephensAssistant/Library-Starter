#!/usr/bin/env python3
"""Validate Planning companion documents against authoritative parent records."""
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_paths import is_support_document

ROOT = Path(__file__).resolve().parents[2]
PARENT_RE = re.compile(r"^(PROJ|TICK)-(\d{4})\.md$")
POINTER_RE = re.compile(r"(?m)^Live plan: Planning/((?:PROJ|TICK)-\d{4}\.md)\s*$")
DONE_RE = re.compile(r"(?m)^status:\s*done\s*$")
REQUIRED = ["Objective", "Work plan", "Next executable steps"]


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, text[end + 5:]


RELATIONSHIP_EVIDENCE_HEADING_RE = re.compile(r"^## Relationship evidence \(\d{4}-\d{2}-\d{2}\)\s*$")
RELATIONSHIP_EVIDENCE_LINE_RE = re.compile(r"^RELATIONSHIP-EVIDENCE:\s+")


def body_without_relationship_metadata(body):
    """Remove only machine-auditable relationship evidence metadata lines."""
    kept = []
    for line in body.splitlines():
        stripped = line.strip()
        if RELATIONSHIP_EVIDENCE_HEADING_RE.fullmatch(stripped):
            continue
        if RELATIONSHIP_EVIDENCE_LINE_RE.match(stripped):
            continue
        kept.append(line.rstrip())
    return "\n".join(kept).strip()


def relationship_metadata_only_change(before, after):
    """Return True only for non-material relationship/migration bookkeeping."""
    before_fm, before_body = split_frontmatter(before)
    after_fm, after_body = split_frontmatter(after)
    changed = {key for key in set(before_fm) | set(after_fm) if before_fm.get(key) != after_fm.get(key)}
    if not changed or not changed.issubset({"links", "updated", "migrated_links_pending"}):
        return False
    if "migrated_links_pending" in changed:
        if before_fm.get("migrated_links_pending") != "[]" or "migrated_links_pending" in after_fm:
            return False
    return body_without_relationship_metadata(before_body) == body_without_relationship_metadata(after_body)


def history_ref(base_ref):
    """Return a ref suitable for git diff/show without double-prefixing remotes."""
    if (
        base_ref.startswith(("HEAD", "origin/", "refs/"))
        or re.fullmatch(r"[0-9a-f]{7,40}(?:(?:\^[0-9]*)|(?:~[0-9]+))*", base_ref)
    ):
        return base_ref
    return f"origin/{base_ref}"


def parent_path(root, parent_id):
    folder = "Projects" if parent_id.startswith("PROJ-") else "Tickets"
    matches = list((root / folder).glob(f"{parent_id}-*.md"))
    return matches[0] if len(matches) == 1 else None


def changed_parent_ids(root, base_ref):
    """Return governed Projects/Tickets added or modified in this transaction.

    Changed work needs an inline checklist or a linked companion. Historical
    records are preserved without forcing a whole-corpus migration.
    """
    if not base_ref:
        return set()
    ref = history_ref(base_ref)
    proc = subprocess.run(
        ["git", "diff", "--name-status", "--diff-filter=AM", f"{ref}...HEAD", "--", "Projects", "Tickets"],
        cwd=root, capture_output=True, text=True, encoding="utf-8",
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"unable to compare against {ref}")
    ids = set()
    for row in proc.stdout.splitlines():
        status, path = row.split("\t", 1)
        if status == "M":
            previous = subprocess.run(
                ["git", "show", f"{ref}:{path}"], cwd=root,
                capture_output=True, text=True, encoding="utf-8",
            )
            current = root / path
            if previous.returncode == 0 and current.is_file() and relationship_metadata_only_change(previous.stdout, current.read_text(errors="ignore")):
                continue
        name = Path(path).name
        if name in {"README.md", "index.md"}:
            continue
        match = re.match(r"^((?:PROJ|TICK)-\d{4})-", name)
        if match:
            ids.add(match.group(1))
    return ids


def validate(root=ROOT, base_ref=None):
    planning = root / "Planning"
    errors = []
    touched_parents = changed_parent_ids(root, base_ref)
    plans_by_parent = defaultdict(list)
    for plan in planning.glob("*.md"):
        if plan.name == "README.md" or is_support_document(plan):
            continue
        m = PARENT_RE.match(plan.name)
        if not m:
            errors.append(f"{plan}: invalid filename; expected exactly PROJ-####.md or TICK-####.md")
            continue
        parent_id = f"{m.group(1)}-{m.group(2)}"
        plans_by_parent[parent_id].append(plan)
        text = plan.read_text(errors="ignore")
        if f"Parent: [[{parent_id}]]" not in text:
            errors.append(f"{plan}: missing exact Parent: [[{parent_id}]] marker")
        for section in REQUIRED:
            if f"## {section}" not in text:
                errors.append(f"{plan}: missing required section '## {section}'")
        parent = parent_path(root, parent_id)
        if not parent:
            errors.append(f"{plan}: parent {parent_id} not found uniquely")
            continue
        parent_text = parent.read_text(errors="ignore")
        pointer = f"Live plan: Planning/{plan.name}"
        if pointer not in parent_text:
            errors.append(f"{plan}: parent {parent.name} missing '{pointer}' backlink")
        if DONE_RE.search(parent_text) and "- [ ]" in text:
            errors.append(f"{plan}: parent {parent_id} is done but the live plan still contains open checklist items")
    for parent_id, plans in plans_by_parent.items():
        if len(plans) > 1:
            errors.append(f"Planning: parent {parent_id} has multiple plans: {', '.join(p.name for p in plans)}")
    for folder in ("Projects", "Tickets"):
        pdir = root / folder
        if not pdir.exists():
            continue
        for parent in pdir.glob("*.md"):
            if parent.name in {"README.md", "index.md"} or is_support_document(parent):
                continue
            parent_text = parent.read_text(errors="ignore")
            for match in POINTER_RE.finditer(parent_text):
                plan_name = match.group(1)
                parent_id = "-".join(parent.name.split("-", 2)[:2])
                if plan_name != f"{parent_id}.md":
                    errors.append(f"{parent}: Live plan pointer {plan_name} does not match parent {parent_id}")
                if not (planning / plan_name).exists():
                    errors.append(f"{parent}: points to missing Planning/{plan_name}")
    for parent_id in sorted(touched_parents):
        expected = planning / f"{parent_id}.md"
        parent = parent_path(root, parent_id)
        if not expected.exists():
            text = parent.read_text(errors="ignore") if parent else ""
            section = re.search(r"(?ms)^## Work plan\s*\n(.*?)(?=^## |\Z)", text)
            if not section or not re.search(r"(?m)^- \[[ xX]\] \S", section.group(1)):
                errors.append(f"{parent_id}: changed work requires an inline Work plan checklist or a linked Planning companion")
            elif DONE_RE.search(text) and re.search(r"(?m)^- \[ \] ", section.group(1)):
                errors.append(f"{parent_id}: done work still contains open inline checklist items")
        elif parent and f"Live plan: Planning/{parent_id}.md" not in parent.read_text(errors="ignore"):
            errors.append(f"{parent}: created or modified Project/Ticket is missing mandatory Live plan pointer")
    return errors


def main():
    base_ref = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        errors = validate(ROOT, base_ref)
    except RuntimeError as exc:
        print(f"::error::{exc}")
        return 1
    if errors:
        for error in errors:
            print(f"::error::{error}")
        return 1
    print("Planning integrity clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
