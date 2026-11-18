#!/usr/bin/env python3
"""
Generates one index.md per type folder, per 00-LIBRARY-RULES.md §9. A
generated view, never a source of truth - an entry's own frontmatter is
always authoritative; if this ever disagrees with an entry, the entry
wins. Rebuilt whole from live frontmatter on every run.

Chats excluded (no per-entry frontmatter). Artifacts' raw files
excluded (no frontmatter) - only companion records are listed.
"""
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from library_scan import collect_entries, load_prefix_map  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]


def render(folder: str, entries: dict) -> str:
    lines = [
        f"# {folder} — Index",
        "",
        "Generated view, per 00-LIBRARY-RULES.md §9. Never hand-edit — an entry's "
        "own frontmatter is always authoritative; this file is rebuilt whole from "
        "it on every run. If this file and an entry's own frontmatter ever "
        "disagree, the entry wins.",
        "",
        "| ID | Title | Status | Links |",
        "|---|---|---|---|",
    ]
    for entry_id in sorted(entries.keys()):
        fm = entries[entry_id]["fm"]
        title = fm.get("title") or ""
        status = fm.get("status") or ""
        links = fm.get("links") or []
        links_str = ", ".join(links) if isinstance(links, list) and links else "—"
        lines.append(f"| {entry_id} | {title} | {status} | {links_str} |")
    lines.append("")
    return "\n".join(lines)


def main():
    prefix_map = load_prefix_map()
    all_entries = collect_entries()
    changed_any = False

    for folder in prefix_map:
        folder_path = REPO_ROOT / folder
        if not folder_path.exists():
            continue  # nothing to index if the folder doesn't exist

        folder_entries = {
            eid: data for eid, data in all_entries.items() if data["folder"] == folder
        }
        output_path = folder_path / "index.md"
        content = render(folder, folder_entries)

        changed = True
        if output_path.exists():
            changed = output_path.read_text() != content
        output_path.write_text(content)

        print(f"{folder}/index.md: {len(folder_entries)} entrie(s), "
              f"{'changed' if changed else 'unchanged'}.")
        changed_any = changed_any or changed

    # Remove obsolete generated indexes when a folder leaves the prefix map.
    for entry in REPO_ROOT.iterdir():
        if not entry.is_dir() or entry.name.startswith(".") or entry.name == ".git":
            continue
        if entry.name in prefix_map:
            continue
        stale_index = entry / "index.md"
        if stale_index.exists():
            stale_index.unlink()
            print(f"Removed orphaned {entry.name}/index.md (folder no longer governed).")
            changed_any = True

    import os
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write(f"changed={'true' if changed_any else 'false'}\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
