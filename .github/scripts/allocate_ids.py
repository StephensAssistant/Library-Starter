#!/usr/bin/env python3
"""Allocate serialized permanent-ID reservations."""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from chat_utils import extract_ids  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RESERVATIONS = ROOT / ".github/id-reservations.json"


def used_ids(root, prefix, config):
    folder_mapping = config["folders"]
    shared_mapping = config.get("shared_files", {})
    folders = [folder for folder, value in folder_mapping.items() if value == prefix]
    shared_folders = [folder for folder, value in shared_mapping.items() if value == prefix]

    if len(folders) + len(shared_folders) != 1:
        raise ValueError(f"unknown or ambiguous prefix: {prefix}")

    used = set()
    if shared_folders:
        if prefix != "CHAT":
            raise ValueError(f"unsupported shared-file prefix: {prefix}")
        for path in (root / shared_folders[0]).glob("*.md"):
            if path.name != "README.md":
                used.update(extract_ids(path.read_text()))
        return used

    pattern = re.compile(rf"^{re.escape(prefix)}-(\d{{4}})-")
    for path in (root / folders[0]).rglob(f"{prefix}-*"):
        match = pattern.match(path.name)
        if match:
            used.add(int(match.group(1)))
    return used


def allocate_batch(root, requests, requested_by):
    if not isinstance(requests, list) or not requests:
        raise ValueError("requests must be a non-empty list")

    config = json.loads((root / ".github/type-prefixes.json").read_text())
    data = json.loads((root / ".github/id-reservations.json").read_text())
    if not isinstance(data.get("reservations"), list):
        raise ValueError("reservation ledger is malformed")

    normalized = []
    seen = set()
    total = 0
    for request in requests:
        if not isinstance(request, dict):
            raise ValueError("each request must be an object")
        prefix = request.get("prefix")
        count = request.get("count")
        if not isinstance(prefix, str) or not re.fullmatch(r"[A-Z]+", prefix):
            raise ValueError("request prefix must contain uppercase letters")
        if prefix in seen:
            raise ValueError(f"duplicate permanent-ID prefix: {prefix}")
        if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= 50:
            raise ValueError("count must be 1..50")
        used = used_ids(root, prefix, config)
        for row in data["reservations"]:
            if row.get("prefix") == prefix:
                numbers = row.get("numbers")
                if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
                    raise ValueError("reservation ledger contains malformed numbers")
                used.update(numbers)
        normalized.append((prefix, count, used))
        seen.add(prefix)
        total += count

    if total > 50:
        raise ValueError("total count must be 1..50")

    reserved_at = datetime.now(timezone.utc).isoformat()
    allocated = []
    for prefix, count, used in normalized:
        start = max(used, default=0) + 1
        numbers = list(range(start, start + count))
        if numbers[-1] > 9999:
            raise ValueError(f"{prefix} four-digit namespace exhausted")
        data["reservations"].append({
            "prefix": prefix, "numbers": numbers, "requested_by": requested_by,
            "reserved_at": reserved_at
        })
        allocated.extend(f"{prefix}-{number:04d}" for number in numbers)

    (root / ".github/id-reservations.json").write_text(json.dumps(data, indent=2) + "\n")
    return allocated


def allocate(root, prefix, count, requested_by):
    """Backward-compatible single-prefix wrapper."""
    return allocate_batch(root, [{"prefix": prefix, "count": count}], requested_by)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("request")
    parser.add_argument("count", nargs="?", type=int)
    parser.add_argument("--requested-by", required=True)
    args = parser.parse_args()
    try:
        if args.count is None:
            payload = json.loads(args.request)
            requests = payload.get("requests") if isinstance(payload, dict) else payload
            ids = allocate_batch(ROOT, requests, args.requested_by)
        else:
            ids = allocate(ROOT, args.request.upper(), args.count, args.requested_by)
        print(",".join(ids))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc))


if __name__ == "__main__":
    main()
