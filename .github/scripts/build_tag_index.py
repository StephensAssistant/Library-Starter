#!/usr/bin/env python3
"""
Generates Catalog/TAG-INDEX.md — a reverse index of tag -> entry IDs,
per 00-LIBRARY-RULES.md §4c. This is a generated view, not a source of
truth: an entry's own tags field is always authoritative (§4c, §9's
same principle applied to every other folder index). This file is
rebuilt whole every run from live frontmatter, never hand-edited.

Chats excluded, consistent with every other script - no per-entry
frontmatter. Artifacts' raw files excluded - only the companion
record (which has frontmatter) contributes tags.

Idempotent: run it twice on unchanged content and the output is
byte-identical, so the calling workflow can diff before committing
and skip a no-op commit.
"""
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from library_scan import collect_entries  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]
OUTPUT_PATH = REPO_ROOT / "Catalog" / "TAG-INDEX.md"


def collect_tags():
    """Returns {tag: sorted list of entry IDs}."""
    index = {}
    for entry_id, data in collect_entries().items():
        tags = data["fm"].get("tags") or []
        if not isinstance(tags, list):
            continue
        for tag in tags:
            index.setdefault(tag, set()).add(entry_id)
    return {tag: sorted(ids) for tag, ids in index.items()}


def render(index: dict) -> str:
    lines = [
        "# Tag Index",
        "",
        "Generated view, per 00-LIBRARY-RULES.md §4c. Never hand-edit — an entry's own "
        "`tags:` field is always authoritative; this file is rebuilt whole from it on "
        "every run. If this file and an entry's own tags ever disagree, the entry wins.",
        "",
        "| Tag | Entries |",
        "|---|---|",
    ]
    for tag in sorted(index.keys()):
        ids = ", ".join(index[tag])
        lines.append(f"| {tag} | {ids} |")
    lines.append("")  # trailing newline
    return "\n".join(lines)


def main():
    index = collect_tags()
    content = render(index)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    changed = True
    if OUTPUT_PATH.exists():
        changed = OUTPUT_PATH.read_text() != content

    OUTPUT_PATH.write_text(content)

    print(f"Tag Index: {len(index)} tag(s), {'changed' if changed else 'unchanged'}.")

    # Communicate to the calling workflow via GITHUB_OUTPUT, not the exit
    # code - a nonzero exit here would be misread as a CI failure.
    import os
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
