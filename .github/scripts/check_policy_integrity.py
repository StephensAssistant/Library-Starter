#!/usr/bin/env python3
"""Git-native enforcement for semantic Library policies not covered elsewhere."""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_paths import is_support_document

ROOT = Path(__file__).resolve().parents[2]
FINDINGS = ROOT / "policy_findings.json"
RETIRED = ("Catalog/INDEX.md", "Catalog/CONTROL-CENTRE.md", "Tickets/BOARD.md", "00-LIBRARY-RULES.md")
RELATIONSHIPS = {"same_as", "broader_than", "narrower_than", "related_to", "defined_by", "source_for"}
BRANCH_POLICY_MARKERS = (
    "Entry to PLAY-0056, its candidate validation and its GitHub Actions requires one of three evidenced routes:",
    "explicit current-conversation request to run an already-approved governed workflow whose admitted executable steps actually declare PLAY-0056",
    "children inherit that grant without another per-Playbook exception question",
    "A workflow definition, source-edit request, approval, score or historical invocation supplies no operational authority.",
    "Workflow authority never grants PLAY-0055/merge, main writes, external sends, deployment or new schedules",
    "an enclosing workflow, nested call or recovery controller shares this cumulative candidate-repair cap and cannot reset it",
    "specifically names both the Commit Ready Playbook (PLAY-0059) and PLAY-0056",
    "A standalone current-conversation request does not authorize an additional or unscheduled PLAY-0056 run unless the Library owner explicitly states that it is a one-off exception;",
    "GitHub may represent that write as a mechanical commit, but it does not authorize or invoke PLAY-0059, PLAY-0056, PLAY-0055, candidate validation or GitHub Actions.",
    "Each authorized scheduled run is separate, single-use authority for the `staging` batch resolved when that run begins",
    "an enabled schedule he explicitly created or approved that specifically names the Merge Playbook (PLAY-0055)",
    "adding or changing an authorized Playbook requires the Library owner's explicit approval",
    "All authorised source writes and mechanical commits must target `staging`.",
    "`main` is read-only to AIs.",
    "Never trust a tool's default branch: every write must name its target branch explicitly.",
    "If `staging` does not exist and the Library owner has authorised an update, create `staging` from the current `main` head before writing",
    "temporary reconciliation branch whose only destination is `staging`",
    "Each invocation is single-use for that runtime batch",
    "A failed validation attempt does not end the authorised invocation while an evidenced, in-scope correction remains possible.",
    "The same invocation permits at most three changed-input repair attempts",
    "Never retry unchanged input.",
    "Stop on unrelated staging movement, changed main, missing authority/access/evidence, out-of-scope findings, or an exhausted repair budget",
)
CHAT_README_REQUIRED_MARKERS = (
    "Links are directional provenance, not reciprocal",
    "`auto-heal-links` deliberately does not touch",
    "Do not add frontmatter or reciprocal links",
)
CHAT_README_FORBIDDEN_MARKERS = (
    "the reciprocal side is added for you",
    "includes Chat blocks in its reciprocal closure",
    "the reciprocal side is healed automatically",
)


def run(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=True).stdout


def mapped_folders():
    return set(json.loads((ROOT / ".github/frontmatter-rules/folder-map.json").read_text())["folders"])


def changed(base):
    local_ref = base.startswith("HEAD") or bool(re.fullmatch(r"[0-9a-f]{7,40}", base))
    ref = base if local_ref else f"origin/{base}"
    if not local_ref:
        run("git", "fetch", "origin", base, "--depth=1000")
    out = run("git", "diff", "--name-status", f"{ref}...HEAD")
    return [(parts[0], parts[-1]) for line in out.splitlines() if (parts := line.split("\t"))]


def fm_and_body(text):
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    return (text[3:end], text[end + 4:]) if end >= 0 else ("", text)


def field(frontmatter, name):
    m = re.search(rf"(?m)^{re.escape(name)}:\s*(.*?)\s*$", frontmatter)
    return m.group(1).strip("\"'") if m else ""


def normalized_body(body):
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    return re.sub(r"\W+", " ", body.lower()).strip()


def base_body_hashes(base, folders):
    ref = base if base.startswith("HEAD") or re.fullmatch(r"[0-9a-f]{7,40}", base) else f"origin/{base}"
    hashes = {}
    for folder in folders:
        listing = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", folder], cwd=ROOT, capture_output=True, text=True).stdout
        for path in listing.splitlines():
            if not path.endswith(".md") or Path(path).name in ("README.md", "index.md"):
                continue
            shown = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=ROOT, capture_output=True, text=True)
            if shown.returncode:
                continue
            if is_support_document(path, shown.stdout):
                continue
            _, body = fm_and_body(shown.stdout)
            norm = normalized_body(body)
            if len(norm) >= 120:
                hashes.setdefault(hashlib.sha256(norm.encode()).hexdigest(), []).append(path)
    return hashes


def text_at_ref(base, path):
    ref = base if base.startswith("HEAD") or re.fullmatch(r"[0-9a-f]{7,40}", base) else f"origin/{base}"
    shown = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return shown.stdout if shown.returncode == 0 else ""


def retired_debt_count(body, retired):
    return sum(
        line.count(retired)
        for line in body.splitlines()
        if retired in line and "retired" not in line.lower()
    )


def validate_sources(frontmatter, path, violations):
    if "canonical_sources:" not in frontmatter:
        return
    required = ("provider", "url", "relationship", "verified_on")
    block = frontmatter.split("canonical_sources:", 1)[1]
    missing = [key for key in required if not re.search(rf"\b{key}\s*[:=]", block)]
    if missing:
        violations.append(f"{path}: canonical_sources missing {', '.join(missing)}")
    for relation in re.findall(r"relationship\s*[:=]\s*[\"']?([a-z_]+)", block):
        if relation not in RELATIONSHIPS:
            violations.append(f"{path}: unsupported canonical_sources relationship '{relation}'")
    for url in re.findall(r"url\s*[:=]\s*[\"']?([^,\]\n\"']+)", block):
        if not re.match(r"https://", url.strip()):
            violations.append(f"{path}: canonical source URL must be HTTPS")



def receipt_from_environment():
    return os.environ.get("PR_BODY", "") or os.environ.get("COMMIT_BODY", "")












def validate_branch_constitution(text, violations):
    for marker in BRANCH_POLICY_MARKERS:
        if marker not in text:
            violations.append(f"AGENTS.md missing mandatory branch-policy clause: {marker}")


def validate_chat_readme_policy(text, violations):
    for marker in CHAT_README_REQUIRED_MARKERS:
        if marker not in text:
            violations.append(f"Chats/README.md missing directional-Chat policy clause: {marker}")
    for marker in CHAT_README_FORBIDDEN_MARKERS:
        if marker in text:
            violations.append(f"Chats/README.md contradicts directional-Chat policy: {marker}")


def receipt_value(receipt, field_name):
    match = re.search(rf"(?mi)^{re.escape(field_name)}:\s*(.+?)\s*$", receipt)
    return match.group(1).strip() if match else ""


def validate_pr_topology(head_ref, base_ref, receipt, violations):
    if base_ref == "main" and head_ref != "staging":
        violations.append("main release PR must use staging as its head branch")
    if head_ref.startswith("staging-reconcile") and base_ref != "staging":
        violations.append("temporary reconciliation branch may target staging only")


def is_newly_done(frontmatter, base_frontmatter, folder):
    return (
        folder in ("Projects", "Tickets")
        and field(frontmatter, "status") == "done"
        and field(base_frontmatter, "status") != "done"
    )


def main():
    if len(sys.argv) not in (2, 3):
        print("usage: check_policy_integrity.py <base_ref> [findings_path]", file=sys.stderr)
        return 2
    base = sys.argv[1]
    findings = Path(sys.argv[2]) if len(sys.argv) == 3 else FINDINGS
    pr_body = receipt_from_environment()
    folders = mapped_folders()
    changes = changed(base)
    base_hashes = base_body_hashes(base, folders)
    violations = []
    validate_branch_constitution((ROOT / "AGENTS.md").read_text(), violations)
    validate_chat_readme_policy((ROOT / "Chats/README.md").read_text(), violations)
    validate_pr_topology(
        os.environ.get("PR_HEAD_REF", ""),
        os.environ.get("PR_BASE_REF", ""),
        pr_body,
        violations,
    )

    for status, path in changes:
        p = Path(path)
        if status == "D" or len(p.parts) < 2 or p.parts[0] not in folders or p.name in ("README.md", "index.md") or p.suffix != ".md":
            continue
        text = (ROOT / path).read_text(errors="ignore")
        if is_support_document(path, text):
            continue
        frontmatter, body = fm_and_body(text)
        base_frontmatter, base_body = fm_and_body(text_at_ref(base, path))
        entry_id = field(frontmatter, "id") or p.stem.split("-", 2)[0]

        for retired in RETIRED:
            if retired_debt_count(body, retired) > retired_debt_count(base_body, retired):
                violations.append(f"{path}: unannotated reference to retired surface {retired}")

        validate_sources(frontmatter, path, violations)

        norm = normalized_body(body)
        if len(norm) >= 120:
            digest = hashlib.sha256(norm.encode()).hexdigest()
            for other in base_hashes.get(digest, []):
                if other != path:
                    violations.append(f"{path}: exact governed-body duplicate of {other}")

        newly_done = is_newly_done(frontmatter, base_frontmatter, p.parts[0])
        if newly_done:
            evidence = re.search(r"(?i)(evidence|validated|verification|test)", body)
            if not evidence:
                violations.append(f"{path}: done work requires validation evidence in the record body")

    if violations:
        findings.write_text(json.dumps(violations, indent=2))
        print("::error::Library policy-integrity violations found:")
        for violation in violations:
            print(f"::error::{violation}")
        return 1
    findings.write_text("[]\n")
    print("Library policy integrity clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
