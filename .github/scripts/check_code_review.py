#!/usr/bin/env python3
"""Require an exact-diff HAT-0015 receipt for authored code/configuration."""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from code_review_scope import is_reviewable_code  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SHA256 = re.compile(r"[0-9a-f]{64}")
FIELDS = (
    "CODE-REVIEW", "CODE-REVIEW-VERDICT", "CODE-REVIEW-AUTHOR",
    "CODE-REVIEW-REVIEWER", "CODE-REVIEW-DIFF-SHA256", "CODE-REVIEW-EVIDENCE",
)


def run(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=True).stdout


def history_ref(base):
    if base.startswith(("HEAD", "origin/", "refs/")) or re.fullmatch(r"[0-9a-f]{7,40}", base):
        return base
    return f"origin/{base}"


def reviewable_paths(base):
    ref = history_ref(base)
    rows = run("git", "diff", "--name-only", "--diff-filter=ACDMRT", f"{ref}...HEAD")
    return sorted(path for path in rows.splitlines() if is_reviewable_code(path))


def reviewable_diff_sha256(base, paths):
    ref = history_ref(base)
    patch = subprocess.run(
        ["git", "diff", "--binary", "--no-ext-diff", f"{ref}...HEAD", "--", *paths],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout
    return hashlib.sha256(patch).hexdigest()


def parse_receipt(message):
    values = {}
    for field in FIELDS:
        matches = re.findall(rf"(?mi)^{re.escape(field)}:\s*(.*?)\s*$", message)
        if len(matches) != 1:
            return None
        values[field] = matches[0].strip()
    return values


def receipt_failures(receipt, expected_digest):
    if receipt is None:
        return ["receipt is missing, incomplete, or contains duplicate fields"]
    failures = []
    if receipt["CODE-REVIEW"] != "HAT-0015":
        failures.append("CODE-REVIEW must be HAT-0015")
    if receipt["CODE-REVIEW-VERDICT"] != "PASS":
        failures.append("CODE-REVIEW-VERDICT must be PASS")
    author = receipt["CODE-REVIEW-AUTHOR"].casefold()
    reviewer = receipt["CODE-REVIEW-REVIEWER"].casefold()
    if not author or not reviewer or author == reviewer:
        failures.append("declared author and reviewer must be non-empty and different")
    digest = receipt["CODE-REVIEW-DIFF-SHA256"]
    if not SHA256.fullmatch(digest) or digest != expected_digest:
        failures.append("CODE-REVIEW-DIFF-SHA256 does not match the complete current reviewable diff")
    if len(receipt["CODE-REVIEW-EVIDENCE"]) < 30:
        failures.append("CODE-REVIEW-EVIDENCE must identify the inspected diff, risks, and tests")
    return failures


def commit_messages(base):
    ref = history_ref(base)
    raw = run("git", "log", "--format=%B%x00", f"{ref}..HEAD")
    return [message for message in raw.split("\x00") if message.strip()]


def validate(base):
    paths = reviewable_paths(base)
    if not paths:
        return [], []
    digest = reviewable_diff_sha256(base, paths)
    attempts = [parse_receipt(message) for message in commit_messages(base)]
    failures = []
    for receipt in attempts:
        current = receipt_failures(receipt, digest)
        if not current:
            return paths, []
        failures.extend(current)
    if not attempts:
        failures.append("no commit message is available for the authored batch")
    return paths, sorted(set(failures))


def main():
    if len(sys.argv) != 2:
        print("usage: check_code_review.py <author_base>", file=sys.stderr)
        return 2
    try:
        paths, failures = validate(sys.argv[1])
    except subprocess.CalledProcessError as exc:
        print(f"::error::Unable to evaluate code-review evidence: {exc}")
        return 1
    if not paths:
        print("No authored reviewable code/configuration changed; HAT-0015 receipt not required.")
        return 0
    if failures:
        print("::error::Mandatory HAT-0015 code-review gate failed.")
        for path in paths:
            print(f"::error file={path}::{path}")
        for failure in failures:
            print(f"::error::{failure}")
        return 1
    print(f"HAT-0015 review receipt accepted for {len(paths)} code/configuration file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
