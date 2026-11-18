#!/usr/bin/env python3
"""Infer required Hat seats from changed paths and verify effective gates exist.

No hand-authored matrix is required. Deterministic routing is evidenced by the
repository gates that implement each inferred seat.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from code_review_scope import is_reviewable_code  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

ROUTES = {
    "HAT-0001": "candidate-ready",
    "HAT-0007": "candidate-ready",
    "HAT-0020": "candidate-ready",
    "HAT-0015": "candidate-ready",
}


def run(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=True).stdout


def changed_files(base):
    local = base.startswith("HEAD") or bool(re.fullmatch(r"[0-9a-f]{7,40}", base))
    ref = base if local else f"origin/{base}"
    if not local:
        run("git", "fetch", "origin", base, "--depth=1000")
    out = run("git", "diff", "--name-only", f"{ref}...HEAD")
    return [path for path in out.splitlines() if path]


def infer(paths):
    hats = {"HAT-0001", "HAT-0007"} if paths else set()
    if any(path.startswith(("Tickets/", "Projects/", "Planning/")) for path in paths):
        hats.add("HAT-0020")
    if any(is_reviewable_code(path) for path in paths):
        hats.add("HAT-0015")
    return hats


def required_gate_contexts():
    text = (ROOT / ".github/scripts/candidate_contexts.js").read_text(errors="ignore")
    contexts = set()
    for name in ("CANDIDATE_STATUS_CONTEXTS",):
        block = re.search(rf"{name}\s*=\s*Object\.freeze\(\[(.*?)\]\)", text, re.S)
        if block:
            contexts.update(re.findall(r'"([^"]+)"', block.group(1)))
    attestation = re.search(r'CANDIDATE_ATTESTATION_CONTEXT\s*=\s*"([^"]+)"', text)
    if attestation:
        contexts.add(attestation.group(1))
    return contexts


def findings(paths):
    expected = infer(paths)
    required = required_gate_contexts()
    rows = []
    for hat in sorted(expected):
        gate = ROUTES[hat]
        if gate is not None and gate not in required:
            rows.append(f"{hat} inferred but effective gate '{gate}' is not published by the candidate pipeline")
    return expected, rows


def main():
    if len(sys.argv) != 2:
        print("usage: check_hat_routing.py <base_ref>", file=sys.stderr)
        return 2
    paths = changed_files(sys.argv[1])
    hats, rows = findings(paths)
    print("Inferred Hat routing: " + (", ".join(sorted(hats)) if hats else "none"))
    for hat in sorted(hats):
        print(f"- {hat} -> {ROUTES[hat] or 'independent review summarized in the PR or task'}")
    if rows:
        for row in rows:
            print(f"::error::{row}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
