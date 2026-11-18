#!/usr/bin/env python3
"""Generate an optional work overview from canonical Library state."""
import hashlib
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOARD = ROOT / "Catalog/BOARD.md"
AGENTS = ROOT / "AGENTS.md"
OUTPUT = ROOT / "Catalog/SESSION-PACK.md"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def sha256(path):
    # Canonical text hashes survive Git checkout line-ending conversion.
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def metadata(text, name):
    match = re.search(rf"(?m)^- {re.escape(name)}: `([^`]+)`$", text)
    return match.group(1) if match else ""


def extract_section(text, heading):
    match = re.search(rf"(?ms)^## {re.escape(heading)} \(\d+\)\n(.*?)(?=^## |\Z)", text)
    return match.group(0).rstrip() if match else f"## {heading} (0)\n"


def ready_high_priority(text):
    match = re.search(r"(?ms)^## Ready \(\d+\)\n(.*?)(?=^## |\Z)", text)
    if not match:
        return "## Ready — high priority\n\nNone."
    lines = match.group(1).splitlines()
    rows = [line for line in lines if line.startswith("|") and ("| high |" in line or "| Priority |" in line or "|---" in line)]
    if len(rows) <= 2:
        return "## Ready — high priority\n\nNone."
    return "## Ready — high priority\n\n" + "\n".join(rows)


def source_metadata(source_fingerprint):
    """Return stable provenance for canonical inputs, not unrelated repo churn.

    When Board + AGENTS are byte-identical to the inputs already recorded in the
    pack, preserve the existing source commit/time. A test, workflow or other
    non-canonical commit must not make the generated bootstrap look stale or
    force a no-content bot commit.
    """
    baseline = os.environ.get("SESSION_PACK_SOURCE_BASE", "HEAD")
    source_commit = git("rev-parse", "--verify", f"{baseline}^{{commit}}")
    git("merge-base", "--is-ancestor", source_commit, "HEAD")
    generated_at = git("show", "-s", "--format=%cI", source_commit)
    if not OUTPUT.exists():
        return source_commit, generated_at

    existing = OUTPUT.read_text()
    if metadata(existing, "source_fingerprint") != source_fingerprint:
        return source_commit, generated_at

    prior_commit = metadata(existing, "source_commit")
    prior_generated_at = metadata(existing, "generated_at")
    if prior_commit and prior_generated_at:
        try:
            git("merge-base", "--is-ancestor", prior_commit, source_commit)
        except subprocess.CalledProcessError:
            # An unresolved or non-ancestral source cannot survive regeneration.
            return source_commit, generated_at
        return prior_commit, prior_generated_at
    return source_commit, generated_at


def render():
    board_text = BOARD.read_text()
    constitution_sha = sha256(AGENTS)
    board_sha = sha256(BOARD)
    source_fingerprint = hashlib.sha256((constitution_sha + board_sha).encode()).hexdigest()
    source_commit, generated_at = source_metadata(source_fingerprint)
    sections = [extract_section(board_text, "Doing"), extract_section(board_text, "Review"), extract_section(board_text, "Waiting"), ready_high_priority(board_text)]
    section_text = "\n\n".join(sections)
    return f"""# Session Pack

Generated bootstrap only — **not a source of truth**. `Catalog/BOARD.md` is the canonical live derived work view; each Ticket/Project owns its outcome, acceptance, status, evidence and next action. This pack is optional. If stale, read the relevant source record directly; rebuild only when this overview is needed.

- generated_at: `{generated_at}`
- source_commit: `{source_commit}`
- source_commit_role: `ancestral baseline; source_fingerprint identifies actual canonical inputs`
- constitution_sha256: `{constitution_sha}`
- board_sha256: `{board_sha}`
- source_fingerprint: `{source_fingerprint}`
- build_status: `PASS`

## Start here

1. Read `AGENTS.md` once per task; it governs this overview and linked guidance, subject to current user instructions.
2. Open named work directly and follow only relationships relevant to the requested outcome. Use the items below or `Catalog/BOARD.md` when finding unnamed work or answering a portfolio question.
3. Use the Ticket/Project's inline `## Work plan` checklist; read an existing linked Planning companion when applicable. Substantial work may use a companion, but creating one is not a task-entry requirement.
4. Do the next authorized step, verify the applicable acceptance requirement and save meaningful state once. Stop at the requested outcome or a precise blocker.

{section_text}

## Authority and recovery

- Canonical live-state view: `Catalog/BOARD.md`.
- Canonical record detail: the Ticket/Project itself; a linked Planning companion is optional subordinate execution state.
- This file must be regenerated from canonical sources; never hand-edit it.
- For full ready/backlog inventory, open `Catalog/BOARD.md` rather than expanding this bootstrap.
"""


def main():
    content = render()
    old = OUTPUT.read_text() if OUTPUT.exists() else None
    if old == content:
        print("SESSION-PACK unchanged.")
        return 0
    OUTPUT.write_text(content)
    print("SESSION-PACK rebuilt.")
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as handle:
            handle.write("changed=true\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
