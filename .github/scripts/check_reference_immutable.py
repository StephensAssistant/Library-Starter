#!/usr/bin/env python3
"""Reject edits, moves, or deletions of admitted Reference files.

Reference is append-only: add a versioned snapshot instead of changing prior
evidence. README.md remains editable because it documents the operating rules.
"""
import subprocess
from pathlib import Path


def reference_change_failures(rows):
    """Classify git name-status rows; only additions and README edits are valid."""
    failures = []
    for row in rows:
        parts = row.split("\t")
        status = parts[0]
        paths = parts[1:]
        governed = [path for path in paths if path.startswith("Reference/") and path != "Reference/README.md"]
        if governed and status != "A":
            failures.append(f"{status}: {' -> '.join(governed)}; Reference files are immutable after admission")
    return failures


def reference_mutation_failures(repo_root, base_ref):
    """Read the current transaction from git and apply the append-only rule."""
    reference_root = Path(repo_root) / "Reference"
    symlinks = [
        path.relative_to(repo_root).as_posix()
        for path in reference_root.rglob("*")
        if path.is_symlink()
    ] if reference_root.exists() else []
    failures = [f"{path}: symbolic links are not valid Reference evidence" for path in symlinks]
    if not base_ref:
        return failures
    result = subprocess.run(
        ["git", "diff", "--name-status", "-M", base_ref, "HEAD", "--", "Reference/"],
        cwd=Path(repo_root),
        capture_output=True,
        text=True,
    )
    if result.returncode:
        failures.append(f"could not compare Reference against {base_ref}: {result.stderr.strip()}")
        return failures
    return failures + reference_change_failures(result.stdout.splitlines())
