#!/usr/bin/env python3
"""Require permanent tombstones for deleted IDs and preserve historical Chats."""
import json
import re
import subprocess
import sys
from pathlib import Path

from chat_utils import extract_ids
from check_ids import load_deleted_ids
from record_paths import is_support_document

REPO_ROOT = Path(__file__).resolve().parents[2]
LEDGER = ".github/deleted-ids.json"


def deletion_failures(root, base_ref):
    if not base_ref:
        return []
    root = Path(root)

    def git(*args):
        result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8")
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or "Unable to read deletion history")
        return result.stdout

    try:
        base_paths = git("ls-tree", "-r", "--name-only", base_ref).splitlines()
        base_map = json.loads(git("show", f"{base_ref}:.github/type-prefixes.json"))["folders"]
        current_map = json.loads((root / ".github/type-prefixes.json").read_text(encoding="utf-8"))["folders"]
        deleted, errors = load_deleted_ids(root, {**base_map, **current_map})
        failures = [f"{path}: {message}" for path, message in errors]
        old_rows = json.loads(git("show", f"{base_ref}:{LEDGER}"))["deletions"] if LEDGER in base_paths else []
        new_rows = json.loads((root / LEDGER).read_text(encoding="utf-8"))["deletions"] if (root / LEDGER).exists() else []
        if new_rows[:len(old_rows)] != old_rows:
            failures.append("Deletion ledger is append-only: existing tombstones cannot be removed, reordered or changed.")

        def governed_id(path):
            parts = Path(path).parts
            if len(parts) < 2 or parts[0] not in base_map:
                return None
            match = re.fullmatch(r"([A-Z]+-\d{4})-.+\.[A-Za-z0-9]+", parts[-1])
            return match.group(1) if match else None

        prior_ids = {value for path in base_paths if (value := governed_id(path))}
        live_ids = {value for folder in base_map for path in (root / folder).rglob("*")
                    if path.is_file() and (value := governed_id(path.relative_to(root)))}
        for permanent_id in sorted(prior_ids - live_ids - deleted):
            failures.append(f"Deleted governed ID {permanent_id} requires an authorized deletion tombstone.")

        prior_chats, live_chats = set(), set()
        for path in base_paths:
            if path.startswith("Chats/") and Path(path).suffix == ".md":
                content = git("show", f"{base_ref}:{path}")
                if not is_support_document(path, content):
                    prior_chats.update(extract_ids(content))
        for path in (root / "Chats").rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            if not is_support_document(path, content):
                live_chats.update(extract_ids(content))
        for number in sorted(prior_chats - live_chats):
            failures.append(f"Historical CHAT-{number:04d} cannot be removed.")
        return failures
    except (OSError, RuntimeError, ValueError, KeyError, TypeError) as exc:
        return [f"Unable to validate deletion history: {exc}"]


def main():
    from check_planning_integrity import history_ref
    if len(sys.argv) != 2:
        print("usage: check_no_bypass_deletion.py <base_ref>", file=sys.stderr)
        return 2
    failures = deletion_failures(REPO_ROOT, history_ref(sys.argv[1]))
    for failure in failures:
        print(f"::error::{failure}")
    return int(bool(failures))


if __name__ == "__main__":
    sys.exit(main())
