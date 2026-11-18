#!/usr/bin/env python3
"""Validate SESSION-PACK authority markers and canonical-source freshness."""
import hashlib
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "Catalog/SESSION-PACK.md"
BOARD = ROOT / "Catalog/BOARD.md"
AGENTS = ROOT / "AGENTS.md"


def sha256(path):
    # Canonical text hashes survive Git checkout line-ending conversion.
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def metadata(text, name):
    match = re.search(rf"(?m)^- {re.escape(name)}: `([^`]+)`$", text)
    return match.group(1) if match else ""


def git_ok(*args):
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    ).returncode == 0


def findings():
    rows = []
    if not PACK.exists():
        return ["Catalog/SESSION-PACK.md is missing"]
    text = PACK.read_text()
    required = (
        "Generated bootstrap only",
        "not a source of truth",
        "Catalog/BOARD.md` is the canonical live derived work view",
        "build_status: `PASS`",
    )
    for needle in required:
        if needle not in text:
            rows.append(f"SESSION-PACK missing authority/fail-closed marker: {needle}")
    constitution = sha256(AGENTS)
    board = sha256(BOARD)
    fingerprint = hashlib.sha256((constitution + board).encode()).hexdigest()
    if metadata(text, "constitution_sha256") != constitution:
        rows.append("SESSION-PACK constitution hash is stale")
    if metadata(text, "board_sha256") != board:
        rows.append("SESSION-PACK Board hash is stale")
    if metadata(text, "source_fingerprint") != fingerprint:
        rows.append("SESSION-PACK canonical source fingerprint is stale")
    source_commit = metadata(text, "source_commit")
    attested_source = os.environ.get("SESSION_PACK_ATTESTED_SOURCE_COMMIT", "").lower()
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        rows.append("SESSION-PACK source commit is not a full 40-character SHA")
    elif source_commit.lower() != attested_source:
        if not git_ok("cat-file", "-e", f"{source_commit}^{{commit}}"):
            rows.append("SESSION-PACK source commit does not resolve to a repository commit")
        elif not git_ok("merge-base", "--is-ancestor", source_commit, "HEAD"):
            rows.append("SESSION-PACK source commit is not an ancestor of the validated candidate")
    return rows


def main():
    rows = findings()
    if rows:
        for row in rows:
            print(f"::error::{row}")
        return 1
    print("SESSION-PACK freshness clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
