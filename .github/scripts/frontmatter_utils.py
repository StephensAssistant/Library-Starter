#!/usr/bin/env python3
"""
Shared frontmatter parsing, used by check_schema.py and build_tag_index.py
(and any future script that needs to read an entry's frontmatter). Kept
as one module deliberately - two copies of the same parser is exactly
the kind of duplication that drifts apart silently.
"""


def parse_frontmatter(content: str):
    """Minimal parser for our constrained frontmatter dialect: bare scalars
    and single-level flow lists ([a, b, c]). Returns a dict, or None if no
    frontmatter block is found."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    block = content[3:end]

    result = {}
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw_value = line.partition(":")
        key = key.strip()
        raw_value = raw_value.strip()

        if raw_value == "" or raw_value.lower() == "null" or raw_value == "~":
            result[key] = None
        elif raw_value.startswith("[") and raw_value.endswith("]"):
            inner = raw_value[1:-1].strip()
            if not inner:
                result[key] = []
            else:
                items = [i.strip().strip('"').strip("'") for i in inner.split(",")]
                result[key] = items
        else:
            result[key] = raw_value.strip('"').strip("'")

    return result
