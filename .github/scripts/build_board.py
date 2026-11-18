#!/usr/bin/env python3
"""
Generates Catalog/BOARD.md as the sole live derived work view defined by
AGENTS.md and the destination Library's work-management rules. Project/Ticket records remain authoritative.

Scope, deliberately bounded:
  - Lanes apply only to Tickets and Projects (the two types with work_state).
  - Archived Tickets/Projects are excluded from the live lanes.
  - Broken-link detection reports links to IDs that do not exist.
  - Review-due reports entries whose review_on date has passed.

The Board is deterministic output and must never be hand-edited.
"""
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
from chat_utils import extract_ids  # noqa: E402
from library_scan import collect_entries  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]
OUTPUT_PATH = REPO_ROOT / "Catalog" / "BOARD.md"

ART_FROM_FILENAME_RE = re.compile(r"^ART-\d{4}(?=-|\.|$)")

LANE_ORDER = ["doing", "review", "waiting", "ready", "backlog"]
LANE_TITLES = {
    "doing": "Doing",
    "review": "Review",
    "waiting": "Waiting",
    "ready": "Ready",
    "backlog": "Backlog",
}


def render_lane_row(entry_id: str, fm: dict) -> str:
    title = fm.get("title") or ""
    priority = fm.get("priority") or "—"
    next_action = fm.get("next_action") or "—"
    return f"| {entry_id} | {title} | {priority} | {next_action} |"


def build_lanes(entries: dict):
    lanes = {lane: [] for lane in LANE_ORDER}
    done = []

    for entry_id, data in entries.items():
        if data["folder"] not in ("Tickets", "Projects"):
            continue
        fm = data["fm"]
        status = fm.get("status")
        work_state = fm.get("work_state")

        if status == "archived":
            continue
        if status == "done":
            done.append((entry_id, fm))
            continue
        if status in ("active", "blocked") and work_state in lanes:
            lanes[work_state].append((entry_id, fm))

    for lane in lanes:
        lanes[lane].sort(key=lambda pair: pair[0])
    done.sort(key=lambda pair: pair[0])
    return lanes, done


def collect_known_ids(entries: dict) -> set[str]:
    """Return every valid relationship target, including shared Chat entries
    and native Artifact files that deliberately have no frontmatter."""
    known = set(entries)
    artifacts_path = REPO_ROOT / "Artifacts"
    if artifacts_path.exists():
        for path in artifacts_path.iterdir():
            if not path.is_file():
                continue
            match = ART_FROM_FILENAME_RE.match(path.name)
            if match:
                known.add(match.group(0))

    chats_path = REPO_ROOT / "Chats"
    if chats_path.exists():
        for path in chats_path.glob("*.md"):
            if is_support_document(path):
                continue
            known.update(
                f"CHAT-{number:04d}"
                for number in extract_ids(path.read_text(errors="ignore"))
            )
    return known


def find_broken_links(entries: dict):
    known_ids = collect_known_ids(entries)
    broken = []
    for entry_id, data in entries.items():
        links = data["fm"].get("links")
        if not isinstance(links, list):
            continue
        for target in links:
            if target not in known_ids:
                broken.append((entry_id, target))
    return sorted(broken)


def utc_today(now=None):
    """Return the calendar date at UTC, independent of the runner's local TZ."""
    return (now or datetime.now(timezone.utc)).astimezone(timezone.utc).date()


def find_review_due(entries: dict, today=None):
    today = today or utc_today()
    due = []
    for entry_id, data in entries.items():
        fm = data["fm"]
        if fm.get("status") not in {"active", "blocked"}:
            continue
        review_on = fm.get("review_on")
        if not review_on:
            continue
        try:
            review_date = date.fromisoformat(review_on)
        except (ValueError, TypeError):
            continue
        if review_date <= today:
            due.append((entry_id, review_on))
    due.sort(key=lambda pair: pair[1])
    return due


def render(entries: dict) -> str:
    lanes, done = build_lanes(entries)
    broken_links = find_broken_links(entries)
    review_due = find_review_due(entries)

    lines = [
        "# Board",
        "",
        "Canonical live derived work view under AGENTS.md. "
        "Never hand-edit — Project/Ticket status and work_state are authoritative; "
        "this file is rebuilt from them by governed automation.",
        "",
    ]

    for lane in LANE_ORDER:
        items = lanes[lane]
        lines.append(f"## {LANE_TITLES[lane]} ({len(items)})")
        lines.append("")
        if items:
            lines.append("| ID | Title | Priority | Next action |")
            lines.append("|---|---|---|---|")
            for entry_id, fm in items:
                lines.append(render_lane_row(entry_id, fm))
        lines.append("")

    lines.append(f"## Done, recent ({len(done)})")
    lines.append("")
    if done:
        lines.append("| ID | Title | Priority | Next action |")
        lines.append("|---|---|---|---|")
        for entry_id, fm in done:
            lines.append(render_lane_row(entry_id, fm))
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"## Broken links ({len(broken_links)})")
    lines.append("")
    if broken_links:
        for source_id, target_id in broken_links:
            lines.append(f"- `{source_id}` links to `{target_id}`, which does not exist.")
    else:
        lines.append("None found.")
    lines.append("")

    lines.append(f"## Review due ({len(review_due)})")
    lines.append("")
    if review_due:
        for entry_id, review_on in review_due:
            lines.append(f"- `{entry_id}` — review_on {review_on} is due or overdue.")
    else:
        lines.append("None found.")
    lines.append("")

    return "\n".join(lines)


def main():
    entries = collect_entries()
    content = render(entries)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    changed = True
    if OUTPUT_PATH.exists():
        changed = OUTPUT_PATH.read_text() != content
    OUTPUT_PATH.write_text(content)

    print(f"Board: {'changed' if changed else 'unchanged'}.")

    import os
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
