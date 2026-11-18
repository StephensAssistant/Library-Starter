#!/usr/bin/env python3
"""Validate new daily-file Chat IDs against sequence and reservation receipts."""
import subprocess
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
from chat_utils import extract_id_occurrences, extract_ids, FILENAME_PATTERN  # noqa: E402
from check_ids import load_prefix_config, load_reservations  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]


def ids_at_ref(ref: str, path_str: str):
    result = subprocess.run(
        ["git", "show", f"{ref}:{path_str}"],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode != 0:
        return set()
    return set() if is_support_document(path_str, result.stdout) else extract_ids(result.stdout)


def existing_ids_repo_wide(base_ref: str):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", f"origin/{base_ref}", "--", "Chats"],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode != 0:
        return set()
    ids = set()
    for line in result.stdout.splitlines():
        if Path(line).name == "README.md":
            continue
        ids |= ids_at_ref(f"origin/{base_ref}", line)
    return ids


def changed_chat_files(base_ref: str):
    subprocess.run(["git", "fetch", "origin", base_ref, "--depth=1000"], check=True)
    out = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", f"origin/{base_ref}...HEAD"],
        capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout
    return [
        line for line in out.splitlines()
        if line.startswith("Chats/") and Path(line).name != "README.md"
        and not is_support_document(REPO_ROOT / line)
    ]


def missing_reservation_ids(new_ids, reserved):
    return sorted(number for number in new_ids if f"CHAT-{number:04d}" not in reserved)


def duplicate_heading_ids(content):
    counts = Counter(extract_id_occurrences(content))
    return sorted(number for number, count in counts.items() if count > 1)


def main():
    if len(sys.argv) != 2:
        print("usage: check_chat_ids.py <base_ref>", file=sys.stderr)
        return 2
    base_ref = sys.argv[1]
    changed = changed_chat_files(base_ref)
    failed = False

    prefix_map, shared_prefix_map = load_prefix_config()
    reserved, reservation_errors = load_reservations(REPO_ROOT, prefix_map, shared_prefix_map)
    for path, message in reservation_errors:
        print(f"::error file={path}::{message}")
        failed = True

    for path_str in changed:
        filename = Path(path_str).name
        if not FILENAME_PATTERN.match(filename):
            print(f"::error file={path_str}::Chat filename must match YYYY-MM-DD.md, per the daily-file convention.")
            failed = True

    existing = existing_ids_repo_wide(base_ref)
    new_ids = set()

    for path_str in changed:
        before = ids_at_ref(f"origin/{base_ref}", path_str)
        full_path = REPO_ROOT / path_str
        content = full_path.read_text() if full_path.exists() else ""
        duplicate_headings = duplicate_heading_ids(content)
        if duplicate_headings:
            print(f"::error file={path_str}::Duplicate CHAT heading id(s) {duplicate_headings} in the same daily file.")
            failed = True
        after = extract_ids(content)
        new_in_this_file = after - before

        dupes = new_in_this_file & existing
        if dupes:
            print(f"::error file={path_str}::CHAT id(s) {sorted(dupes)} already exist elsewhere in Chats/ - IDs are never reused.")
            failed = True
            new_in_this_file -= dupes

        new_ids |= new_in_this_file

    missing = missing_reservation_ids(new_ids, reserved)
    if missing:
        print(f"::error::New CHAT IDs {[f'CHAT-{n:04d}' for n in missing]} have no serialized reservation receipt.")
        failed = True

    if new_ids:
        current_max = max(existing) if existing else 0
        expected = sorted(new_ids)
        want = current_max + 1
        for got in expected:
            if got != want:
                print(f"::error::New CHAT ids are {[f'CHAT-{i:04d}' for i in sorted(new_ids)]}, but the next expected id after the current max (CHAT-{current_max:04d}) is CHAT-{want:04d}. IDs must be taken in sequence.")
                failed = True
                break
            want += 1

    if not failed:
        print("Chat IDs and reservation receipts clean.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
