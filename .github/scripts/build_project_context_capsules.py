#!/usr/bin/env python3
"""Build small, non-authoritative per-Project context capsules."""
import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECTS = ROOT / "Projects"
PLANS = ROOT / "Planning"
OUTPUT = ROOT / "Catalog" / "Project-Context"
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def scalar(value):
    value = value.strip()
    if value in {"null", "None", ""}:
        return ""
    return value.strip('"\'')


def frontmatter(text):
    match = FM.match(text)
    if not match:
        return {}
    result = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = scalar(value)
    return result


def section(text, heading):
    match = re.search(rf"(?ms)^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text)
    return match.group(1).strip() if match else ""


def compact(text, limit=900):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def render(project_path):
    project_text = project_path.read_text(errors="ignore")
    data = frontmatter(project_text)
    project_id = data.get("id", "")
    if not re.fullmatch(r"PROJ-\d{4}", project_id):
        raise ValueError(f"{project_path}: missing valid Project ID")
    plan_path = PLANS / f"{project_id}.md"
    plan_exists = plan_path.exists()
    plan_text = plan_path.read_text(errors="ignore") if plan_exists else ""
    source_hash = hashlib.sha256((project_text + "\0" + plan_text).encode()).hexdigest()
    current_focus = compact(section(plan_text, "Current focus")) or "Not recorded."
    next_steps = compact(section(plan_text, "Next executable steps")) or "Open the parent Project for current detail."
    values = {
        "status": data.get("status") or "unknown",
        "work_state": data.get("work_state") or "unknown",
        "priority": data.get("priority") or "unknown",
        "updated": data.get("updated") or "unknown",
        "next_action": compact(data.get("next_action", "")) or "None recorded.",
        "waiting_on": compact(data.get("waiting_on", "")) or "None.",
    }
    authority = f"`Projects/{project_path.name}`"
    if plan_exists:
        authority += f" and `Planning/{project_id}.md`"
    return f"""# {project_id} — context capsule

Generated retrieval aid — **not a source of truth**. Open {authority} before consequential action or mutation.

- title: {data.get('title', project_id)}
- status: {values['status']}
- work_state: {values['work_state']}
- priority: {values['priority']}
- updated: {values['updated']}
- plan_exists: {str(plan_exists).lower()}
- source_fingerprint: `{source_hash}`

## Current focus

{current_focus}

## Next action

{values['next_action']}

## Waiting on

{values['waiting_on']}

## Next executable steps

{next_steps}
"""


def expected():
    rows = {}
    for path in sorted(PROJECTS.glob("PROJ-*.md")):
        data = frontmatter(path.read_text(errors="ignore"))
        project_id = data.get("id")
        if project_id:
            rows[f"{project_id}.md"] = render(path)
    rows["README.md"] = """# Project Context Capsules

Generated, compact retrieval aids. Each capsule points to its authoritative Project and live plan; never use a capsule alone for consequential action, status mutation, or merge evidence.
"""
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    rows = expected()
    existing = {p.name: p.read_text() for p in OUTPUT.glob("*.md")} if OUTPUT.exists() else {}
    if args.check:
        if existing != rows:
            print("Project context capsules are stale.", file=sys.stderr)
            return 1
        print(f"Project context capsules current: {len(rows)-1}")
        return 0
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for path in OUTPUT.glob("*.md"):
        if path.name not in rows:
            path.unlink()
    for name, content in rows.items():
        path = OUTPUT / name
        if not path.exists() or path.read_text() != content:
            path.write_text(content)
    print(f"Project context capsules rebuilt: {len(rows)-1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
