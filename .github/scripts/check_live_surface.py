#!/usr/bin/env python3
"""Fail closed when retired work surfaces are reintroduced as live or BOARD is stale."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RETIRED_LIVE_SURFACES = ("Tickets/BOARD.md", "Catalog/CONTROL-CENTRE.md")
HISTORICAL_MARKERS = ("retired", "historical", "migration", "legacy", "superseded")


def run(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=True).stdout


def ref_for(base):
    if base.startswith("HEAD") or re.fullmatch(r"[0-9a-f]{7,40}", base):
        return base
    run("git", "fetch", "origin", base, "--depth=1000")
    return f"origin/{base}"


def added_lines(base):
    ref = ref_for(base)
    diff = run("git", "diff", "--unified=0", f"{ref}...HEAD", "--", "*.md")
    lines = []
    for line in diff.splitlines():
        if line.startswith("+++") or not line.startswith("+"):
            continue
        lines.append(line[1:])
    return lines


def is_historical(line):
    low = line.lower()
    return any(marker in low for marker in HISTORICAL_MARKERS)


def retired_live_assertions(lines):
    findings = []
    for line in lines:
        for surface in RETIRED_LIVE_SURFACES:
            if surface in line and not is_historical(line):
                findings.append(f"new unannotated retired live-surface reference: {surface}: {line.strip()}")
    return findings


def board_is_reproducible():
    board = ROOT / "Catalog/BOARD.md"
    original_bytes = board.read_bytes() if board.exists() else None
    original = board.read_text() if board.exists() else None
    try:
        subprocess.run(
            [sys.executable, str(ROOT / ".github/scripts/build_board.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        rebuilt = board.read_text() if board.exists() else None
        return original == rebuilt
    finally:
        if original is None:
            if board.exists():
                board.unlink()
        else:
            board.write_bytes(original_bytes)


def main():
    if len(sys.argv) != 2:
        print("usage: check_live_surface.py <base_ref>", file=sys.stderr)
        return 2
    findings = retired_live_assertions(added_lines(sys.argv[1]))
    if not board_is_reproducible():
        findings.append("Catalog/BOARD.md does not reproduce exactly from canonical source records")
    if findings:
        for finding in findings:
            print(f"::error::{finding}")
        return 1
    print("Canonical live-surface integrity clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
