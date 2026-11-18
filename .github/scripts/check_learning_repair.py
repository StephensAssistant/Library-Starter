#!/usr/bin/env python3
"""Require a concise learning disposition when a push repairs a failed candidate."""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIELDS = (
    "LEARNING-EVENT",
    "LEARNING-PATTERN",
    "LEARNING-CAUSE",
    "LEARNING-PREVENTION",
    "LEARNING-DISPOSITION",
    "LEARNING-REF",
)
DISPOSITIONS = {"captured", "already-covered", "task-local", "n/a"}
EVENTS = {
    "guidance-missed", "guidance-failed", "guidance-conflict", "integrity-failure",
    "routing-ambiguous", "cross-context-pattern", "task-local", "insufficient-evidence",
}


class LearningRepairError(ValueError):
    pass


def parse_receipt(message):
    values = {}
    for field in FIELDS:
        matches = re.findall(rf"(?mi)^{re.escape(field)}:\s*(\S.*)$", message)
        if len(matches) != 1:
            raise LearningRepairError(f"repair commit requires exactly one {field} field")
        values[field] = matches[0].strip()
    if values["LEARNING-DISPOSITION"] not in DISPOSITIONS:
        raise LearningRepairError("unsupported LEARNING-DISPOSITION")
    if values["LEARNING-EVENT"] not in EVENTS:
        raise LearningRepairError("unsupported LEARNING-EVENT")
    for field in ("LEARNING-PATTERN", "LEARNING-CAUSE", "LEARNING-PREVENTION"):
        if len(values[field]) < 8:
            raise LearningRepairError(f"{field} must contain specific evidence")
    return values


def owner_is_changed(reference, changed_paths, contents):
    if reference in changed_paths:
        return True
    if not re.fullmatch(r"(?:PLAY|SKILL|KNOW)-\d{4}", reference):
        return False
    marker = re.compile(rf"(?m)^id:\s*{re.escape(reference)}\s*$")
    return any(marker.search(contents.get(path, "")) for path in changed_paths)


def validate_receipt(message, changed_paths, contents):
    receipt = parse_receipt(message)
    disposition = receipt["LEARNING-DISPOSITION"]
    if disposition == "captured" and not owner_is_changed(
        receipt["LEARNING-REF"], changed_paths, contents
    ):
        raise LearningRepairError(
            "captured learning requires the named canonical owner in the authored diff"
        )
    if disposition != "captured" and len(receipt["LEARNING-REF"]) < 8:
        raise LearningRepairError("no-change learning requires a specific LEARNING-REF reason")
    return receipt


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--required", choices=("true", "false"), required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--failure-run", default="")
    args = parser.parse_args(argv)
    if args.required == "false":
        print("No immediately preceding failed candidate requires a learning receipt.")
        return 0
    try:
        message = git("log", "-1", "--format=%B", "HEAD")
        changed_paths = set(git("diff", "--name-only", f"{args.base}...HEAD").splitlines())
        contents = {
            path: (ROOT / path).read_text(errors="ignore")
            for path in changed_paths
            if (ROOT / path).is_file()
        }
        receipt = validate_receipt(message, changed_paths, contents)
    except (LearningRepairError, OSError, subprocess.CalledProcessError) as exc:
        print(f"LEARNING REPAIR FAIL: {exc}")
        return 1
    print(
        "Learning repair captured: "
        f"{receipt['LEARNING-EVENT']} -> {receipt['LEARNING-DISPOSITION']} "
        f"({receipt['LEARNING-REF']}); prior run: {args.failure_run or 'recorded by workflow'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
