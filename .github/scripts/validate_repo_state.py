#!/usr/bin/env python3
"""Validate candidate repository integrity, including history against its base.

Shares schema, ID, Chat, planning and relationship validation with scoped checks.
When a base is supplied, also protects Reference evidence and deletion history.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
from schema_rules import load_rules, load_folder_map, validate_entry_frontmatter  # noqa: E402
from frontmatter_utils import parse_frontmatter  # noqa: E402
from chat_utils import extract_ids as extract_chat_ids, FILENAME_PATTERN as CHAT_FILENAME_PATTERN  # noqa: E402
from check_reference_immutable import reference_mutation_failures  # noqa: E402
from check_ids import load_deleted_ids  # noqa: E402
from check_planning_integrity import history_ref  # noqa: E402
from check_policy_integrity import fm_and_body, validate_sources  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]


def load_json(name):
    return json.loads((REPO_ROOT / ".github" / name).read_text())


def changed_paths(base_ref):
    if not base_ref:
        return set()
    proc = subprocess.run(
        ["git", "diff", "--name-only", f"{history_ref(base_ref)}...HEAD"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"unable to compare against {base_ref}")
    return {path for path in proc.stdout.splitlines() if path}


def navigation_failures(entries, chats, raw_owners):
    """Validate every inbound edge, including unchanged sources after deletion."""
    known = set(entries) | set(chats) | set(raw_owners)
    relationships = {key: value["fm"].get("links", []) for key, value in entries.items()}
    relationships.update(chats)
    failures = []
    for source, targets in relationships.items():
        if not isinstance(targets, (list, set)):
            failures.append(f"{source}: links must be an array")
            continue
        for target in targets:
            if not isinstance(target, str) or target not in known:
                failures.append(f"{source}: relationship target does not exist: {target}")
    return failures


def live_raw_owners(entries, raw_owners, root):
    """Resolve raw targets from the candidate index, including unmaterialised blobs."""
    from check_ids import safe_repo_target
    tracked = None
    result = subprocess.run(
        ["git", "ls-files", "--stage", "-z"], cwd=root, capture_output=True, text=True,
    )
    if result.returncode == 0:
        tracked = set()
        for row in result.stdout.split("\0"):
            if not row:
                continue
            metadata, path = row.split("\t", 1)
            mode, _blob, stage = metadata.split()
            if stage != "0":
                raise ValueError("Candidate index contains unresolved merge stages")
            if mode in {"100644", "100755"} and safe_repo_target(root, path) is not None:
                tracked.add(path)
    live = {}
    if tracked is not None:
        for path in tracked:
            if not path.startswith("Artifacts/"):
                continue
            match = re.fullmatch(r"(ART-\d{4})-.+\.[A-Za-z0-9]+", Path(path).name)
            if match:
                raw_id = match.group(1)
                live[raw_id] = raw_owners.get(raw_id, raw_id)
    for raw_id, owner in raw_owners.items():
        target = safe_repo_target(root, entries[owner]["fm"].get("stored_at", ""))
        if target is None:
            continue
        relative = target.relative_to(root).as_posix()
        if (tracked is not None and relative in tracked) or (tracked is None and target.is_file()):
            live[raw_id] = owner
    return live


def main():
    from check_workflows import check_repository
    workflow_errors = check_repository(REPO_ROOT)
    if workflow_errors:
        for error in workflow_errors:
            print(f"::error::{error}")
        sys.exit(1)
    allowed_folders = set(load_json("allowed-top-level-folders.json")["folders"])
    prefix_map = load_json("type-prefixes.json")["folders"]

    violations = []
    reference_base = sys.argv[1] if len(sys.argv) == 2 else None
    candidate_paths = changed_paths(reference_base)
    deleted_ids, deletion_errors = load_deleted_ids(REPO_ROOT, prefix_map)
    violations.extend(f"Deleted IDs: {path}: {message}" for path, message in deletion_errors)

    from check_no_bypass_deletion import deletion_failures
    violations.extend(deletion_failures(REPO_ROOT, history_ref(reference_base) if reference_base else None))

    # 1. Every top-level directory must be on the allow-list (§1a)
    for entry in REPO_ROOT.iterdir():
        if not entry.is_dir():
            continue
        if entry.name.startswith(".") or entry.name == ".git":
            continue
        if entry.name not in allowed_folders:
            violations.append(
                f"Top-level folder '{entry.name}' is not on the approved list "
                f"(.github/allowed-top-level-folders.json). Per §1a, a new folder "
                f"is never created unilaterally."
            )


    # 1c. Admitted Reference snapshots are append-only evidence.
    violations.extend(
        f"Reference: {failure}"
        for failure in reference_mutation_failures(REPO_ROOT, reference_base)
    )

    # 2. Every ID inside a mapped folder must match its prefix and form a
    #    contiguous run from 1, with no duplicates (§2)
    for folder, prefix in prefix_map.items():
        folder_path = REPO_ROOT / folder
        if not folder_path.exists():
            continue

        pattern = re.compile(rf"^([A-Z]+)-(\d{{4}})-.+\.[A-Za-z0-9]+$")
        ids_seen = []

        for entry in folder_path.iterdir():
            if entry.name in ("README.md", "index.md") or is_support_document(entry):
                continue
            m = pattern.match(entry.name)
            if not m:
                violations.append(
                    f"{folder}/{entry.name}: filename does not match "
                    f"<PREFIX>-<NNNN>-<slug>.<ext>."
                )
                continue
            file_prefix, id_num_str = m.group(1), m.group(2)
            if file_prefix != prefix:
                violations.append(
                    f"{folder}/{entry.name}: prefix '{file_prefix}' does not match "
                    f"folder '{folder}' (expected '{prefix}')."
                )
                continue
            ids_seen.append(int(id_num_str))

        dupes = {i for i in ids_seen if ids_seen.count(i) > 1}
        if dupes:
            violations.append(
                f"{folder}: duplicate ID number(s) {sorted(dupes)} — IDs are never reused."
            )

        deleted_numbers = {
            int(permanent_id.split("-", 1)[1])
            for permanent_id in deleted_ids
            if permanent_id.startswith(f"{prefix}-")
        }
        live_ids = {f"{prefix}-{number:04d}" for number in ids_seen}
        collisions = sorted(live_ids.intersection(deleted_ids))
        if collisions:
            violations.append(
                f"{folder}: deleted ID(s) still have live governed records: {collisions}."
            )
        unique_sorted = sorted(set(ids_seen) | deleted_numbers)
        expected = 1
        for num in unique_sorted:
            if num != expected:
                violations.append(
                    f"{folder}: ID sequence has a gap — found {prefix}-{num:04d} but "
                    f"expected {prefix}-{expected:04d} next. IDs must be represented "
                    f"by either one live record or one explicit deletion tombstone."
                )
                break
            expected += 1

    # 3. Every entry's frontmatter must validate against its type's schema
    #    (§4/§4b) - re-uses the exact same rule logic check_schema.py uses
    #    on PR diffs, applied here to every current entry unconditionally.
    folder_map = load_folder_map()
    for folder, rules_file in folder_map.items():
        folder_path = REPO_ROOT / folder
        if not folder_path.exists():
            continue
        rules = load_rules(rules_file)
        for entry in folder_path.iterdir():
            if entry.name in ("README.md", "index.md") or not entry.is_file() or is_support_document(entry):
                continue
            content = entry.read_text(errors="ignore")
            fm = parse_frontmatter(content)
            if fm is None:
                if folder == "Artifacts":
                    continue  # raw Artifact file, no frontmatter by design (§4a)
                violations.append(f"{folder}/{entry.name}: no frontmatter block found.")
                continue
            for v in validate_entry_frontmatter(fm, rules):
                violations.append(f"{folder}/{entry.name}: {v}")
            relative_path = f"{folder}/{entry.name}"
            if relative_path in candidate_paths:
                frontmatter_text, _ = fm_and_body(content)
                validate_sources(frontmatter_text, relative_path, violations)

    # 4. Chat IDs must be sequential with no gaps or duplicates, and every
    #    Chats file must follow the YYYY-MM-DD.md convention (§4/§6) -
    #    re-uses the same extraction logic check_chat_ids.py uses on diffs.
    chats_dir = REPO_ROOT / "Chats"
    if chats_dir.exists():
        all_chat_ids = []
        for entry in chats_dir.iterdir():
            if entry.name == "README.md" or not entry.is_file() or is_support_document(entry):
                continue
            if not CHAT_FILENAME_PATTERN.match(entry.name):
                violations.append(
                    f"Chats/{entry.name}: filename does not match YYYY-MM-DD.md."
                )
                continue
            all_chat_ids.extend(extract_chat_ids(entry.read_text(errors="ignore")))

        dupes = {i for i in all_chat_ids if all_chat_ids.count(i) > 1}
        if dupes:
            violations.append(f"Chats: duplicate CHAT id(s) {sorted(dupes)}.")

        unique_sorted = sorted(set(all_chat_ids))
        expected = 1
        for num in unique_sorted:
            if num != expected:
                violations.append(
                    f"Chats: CHAT id sequence has a gap — found CHAT-{num:04d} but "
                    f"expected CHAT-{expected:04d} next."
                )
                break
            expected += 1

    # 5. Planning companions must resolve to one authoritative parent and
    #    contain the reciprocal path pointer required by Planning/README.md.
    from check_planning_integrity import main as validate_planning
    if validate_planning() != 0:
        violations.append("Planning companion integrity is invalid.")

    # 6. Relationship evidence must reconcile with live reciprocal links and
    #    recompute cleanly under the versioned deterministic scoring model.
    from relationship_confidence import validate_repository
    from library_scan import collect_entries
    from auto_heal_links import load_chat_links, raw_artifact_owners
    entries = collect_entries()
    raw_owners = live_raw_owners(entries, raw_artifact_owners(entries), REPO_ROOT)
    violations.extend(navigation_failures(entries, load_chat_links(), raw_owners))
    confidence_base = sys.argv[1] if len(sys.argv) == 2 else None
    if validate_repository(confidence_base) != 0:
        violations.append("Relationship confidence ledger is invalid or inconsistent.")

    if violations:
        print("REPO STATE VIOLATIONS FOUND:")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)

    print("Repo state clean.")
    sys.exit(0)


if __name__ == "__main__":
    main()
