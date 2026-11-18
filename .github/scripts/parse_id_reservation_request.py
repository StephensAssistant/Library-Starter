#!/usr/bin/env python3
"""Parse an AI-callable permanent-ID reservation issue title."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HEADER = re.compile(r"^\[ID-RESERVE\]\s+(.+)$")
ITEM = re.compile(r"^([A-Z]+)(?:\s+([1-9][0-9]*))?$")


def valid_prefixes(root=ROOT):
    data = json.loads((root / ".github/type-prefixes.json").read_text())
    prefixes = set(data["folders"].values())
    prefixes.update(data.get("shared_files", {}).values())
    return prefixes


def parse_request(title, prefixes):
    match = HEADER.fullmatch(title.strip())
    if not match:
        raise ValueError(
            "expected title '[ID-RESERVE] PREFIX [COUNT]' or "
            "'[ID-RESERVE] PREFIX [COUNT], PREFIX [COUNT]'"
        )

    requests = []
    seen = set()
    total = 0
    for raw_item in match.group(1).split(","):
        item = ITEM.fullmatch(raw_item.strip())
        if not item:
            raise ValueError(f"malformed permanent-ID request: {raw_item.strip()!r}")
        prefix = item.group(1)
        count = int(item.group(2) or "1")
        if prefix not in prefixes:
            raise ValueError(f"unknown permanent-ID prefix: {prefix}")
        if prefix in seen:
            raise ValueError(f"duplicate permanent-ID prefix: {prefix}")
        if not 1 <= count <= 50:
            raise ValueError("count must be 1..50")
        seen.add(prefix)
        total += count
        requests.append({"prefix": prefix, "count": count})

    if total > 50:
        raise ValueError("total count must be 1..50")
    return {"requests": requests}


def main():
    if len(sys.argv) != 2:
        print("usage: parse_id_reservation_request.py '<issue title>'", file=sys.stderr)
        return 2
    try:
        print(json.dumps(parse_request(sys.argv[1], valid_prefixes()), separators=(",", ":")))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
