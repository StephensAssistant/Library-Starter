#!/usr/bin/env python3
"""Run bounded validators for ordinary content-only changes.

Control-plane changes never reach this runner: validation_scope.py routes them
to the complete release preflight.
"""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STORED_AT = re.compile(r"^stored_at:\s*(\S+)\s*$", re.MULTILINE)
ARTIFACT_HASH = re.compile(
    r"Artifact SHA-256(?: of the raw stored UTF-8 bytes)?:\s*`([0-9a-f]{64})`",
    re.IGNORECASE,
)


def check_artifact_companion_hashes(paths):
    """Verify claims affected by this batch against raw checked-out file bytes."""
    changed = set(paths)
    artifacts = ROOT / "Artifacts"
    failures = []
    for companion in sorted(artifacts.glob("*.md")):
        text = companion.read_text(encoding="utf-8")
        stored_match = STORED_AT.search(text)
        hash_match = ARTIFACT_HASH.search(text)
        if not stored_match or not hash_match:
            continue
        stored = stored_match.group(1)
        relative = companion.relative_to(ROOT).as_posix()
        if relative not in changed and stored not in changed:
            continue
        target = ROOT / stored
        if not target.is_file():
            failures.append(f"{relative}: stored_at target is missing: {stored}")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        expected = hash_match.group(1).lower()
        if actual != expected:
            failures.append(
                f"{relative}: Artifact SHA-256 mismatch for {stored}; "
                f"expected {expected}, actual {actual}"
            )
    if failures:
        raise ValueError("artifact companion hash validation failed:\n" + "\n".join(failures))


def commands(base_branch, paths, phase="all"):
    rows = [
        [sys.executable, ".github/scripts/check_workflows.py"],
        [sys.executable, ".github/scripts/check_schema.py", base_branch],
        [sys.executable, ".github/scripts/check_ids.py", base_branch],
        [sys.executable, ".github/scripts/check_chat_ids.py", base_branch],
    ]
    if any(p.startswith(("Projects/", "Tickets/", "Planning/")) for p in paths):
        rows.append([sys.executable, ".github/scripts/check_planning_integrity.py", base_branch])
    if any(p.startswith("Reference/") for p in paths):
        rows.append([sys.executable, ".github/scripts/check_reference_immutable.py", base_branch])
    if any(p.startswith("Artifacts/") for p in paths):
        rows.extend([
            [sys.executable, ".github/scripts/check_embedded_scripts.py", base_branch],
            [sys.executable, ".github/scripts/check_artifact_duplicate_growth.py", base_branch],
        ])
    derived = [
        [sys.executable, ".github/scripts/auto_heal_links.py", "--check"],
        [sys.executable, ".github/scripts/relationship_confidence.py", "--base-ref", f"origin/{base_branch}"],
    ]
    return rows if phase == "source" else derived if phase == "reconciled" else rows + derived


def changed(base_ref):
    proc = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACDMRT", f"{base_ref}...HEAD"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    paths = set(proc.stdout.splitlines())
    # Scratch candidates may have freshly reconciled files outside HEAD.
    for command in (["git", "diff", "--name-only", "HEAD"],
                    ["git", "ls-files", "--others", "--exclude-standard"]):
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
        paths.update(result.stdout.splitlines())
    return sorted(p for p in paths if p)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="origin/main")
    parser.add_argument("--base-branch", default="main")
    phases = parser.add_mutually_exclusive_group()
    phases.add_argument("--source-only", action="store_true")
    phases.add_argument("--reconciled-only", action="store_true")
    args = parser.parse_args(argv)
    paths = changed(args.base_ref)
    phase = "source" if args.source_only else "reconciled" if args.reconciled_only else "all"
    if phase != "reconciled":
        check_artifact_companion_hashes(paths)
    for command in commands(args.base_branch, paths, phase):
        print("+", " ".join(command), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
    print(f"Changed-file validation passed for {len(paths)} paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
