#!/usr/bin/env python3
"""
Enforces 00-LIBRARY-RULES.md §3's Familiarity Check backstop: flags
likely-duplicate titles within the same type folder using word-overlap
similarity. Matches the old system's behaviour exactly - this NEVER
blocks or fails the check. It writes findings to a JSON file for a
separate workflow step to post as an informational PR comment.

"A genuinely related but distinct pair stays two entries; linking them
to each other silences the flag, same as any other cross-reference."
This script only flags - a human decides what it means.

Threshold (0.5, Jaccard over lowercase word tokens) is a starting
point, not calibrated against a real corpus yet - the old system's
threshold was "calibrated against real Library titles", which does
not exist for this repo yet since it's still empty. Flagged here so
it isn't mistaken for an authoritative number.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SIMILARITY_THRESHOLD = 0.5
FINDINGS_PATH = REPO_ROOT / "similarity_findings.json"


def load_prefix_map():
    data = json.loads((REPO_ROOT / ".github" / "type-prefixes.json").read_text())
    return data["folders"]


def extract_title(content: str) -> str | None:
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    frontmatter = content[3:end]
    for line in frontmatter.splitlines():
        line = line.strip()
        if line.startswith("title:"):
            value = line[len("title:"):].strip()
            return value.strip('"').strip("'")
    return None


def word_set(title: str):
    return set(re.findall(r"[a-z0-9]+", title.lower()))


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def existing_titles(folder: str, base_ref: str):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", f"origin/{base_ref}", "--", folder],
        capture_output=True, text=True,
    )
    titles = {}
    if result.returncode != 0:
        return titles
    for line in result.stdout.splitlines():
        filename = Path(line).name
        if filename in ("README.md", "index.md"):
            continue
        show = subprocess.run(
            ["git", "show", f"origin/{base_ref}:{line}"],
            capture_output=True, text=True,
        )
        if show.returncode != 0:
            continue
        title = extract_title(show.stdout)
        if title:
            titles[line] = title
    return titles


def added_files(base_ref: str):
    subprocess.run(["git", "fetch", "origin", base_ref, "--depth=1000"], check=True)
    out = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=A", f"origin/{base_ref}...HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout
    return [line for line in out.splitlines() if line.strip()]


def main():
    if len(sys.argv) != 2:
        print("usage: check_title_similarity.py <base_ref>", file=sys.stderr)
        sys.exit(2)
    base_ref = sys.argv[1]

    prefix_map = load_prefix_map()
    added = added_files(base_ref)
    findings = []

    for path_str in added:
        path = Path(path_str)
        if len(path.parts) < 2:
            continue
        folder = path.parts[0]
        filename = path.parts[-1]
        if folder not in prefix_map or filename in ("README.md", "index.md"):
            continue

        full_path = REPO_ROOT / path_str
        if not full_path.exists():
            continue
        new_title = extract_title(full_path.read_text())
        if not new_title:
            continue

        existing = existing_titles(folder, base_ref)
        new_words = word_set(new_title)

        for existing_path, existing_title in existing.items():
            score = jaccard(new_words, word_set(existing_title))
            if score >= SIMILARITY_THRESHOLD:
                findings.append({
                    "new_file": path_str,
                    "new_title": new_title,
                    "existing_file": existing_path,
                    "existing_title": existing_title,
                    "similarity": round(score, 2),
                })

    FINDINGS_PATH.write_text(json.dumps(findings, indent=2))

    if findings:
        print(f"Found {len(findings)} possible-duplicate title(s) — see similarity_findings.json. "
              f"This is informational only per §3 and never blocks.")
    else:
        print("No possible-duplicate titles found.")

    sys.exit(0)  # never fails - this is a flag, not a gate


if __name__ == "__main__":
    main()
