#!/usr/bin/env python3
"""Fail-closed permanent-ID validation for the complete tree and PR additions."""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
from chat_utils import FILENAME_PATTERN, extract_id_occurrences, extract_ids  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
FILE_RE = re.compile(r"^([A-Z]+)-(\d{4})-.+\.[A-Za-z0-9]+$")
PERMANENT_ID_RE = re.compile(r"^([A-Z]+)-(\d{4})$")


def load_prefix_config(root=REPO_ROOT):
    data = json.loads((root / ".github/type-prefixes.json").read_text())
    return data["folders"], data.get("shared_files", {})


def load_prefix_map(root=REPO_ROOT):
    return load_prefix_config(root)[0]


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}
    result = {}
    for line in lines[1:end]:
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def safe_repo_target(root, value):
    target = PurePosixPath(value)
    if target.is_absolute() or ".." in target.parts:
        return None
    resolved = (root / Path(*target.parts)).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        return None
    return resolved


def load_reservations(root, prefix_map, shared_prefix_map=None):
    path = root / ".github/id-reservations.json"
    errors, reserved = [], {}
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [(path.relative_to(root).as_posix(), f"Invalid reservation ledger: {exc}")]
    valid_prefixes = set(prefix_map.values()) | set((shared_prefix_map or {}).values())
    if not isinstance(data, dict) or not isinstance(data.get("reservations"), list):
        return {}, [(path.relative_to(root).as_posix(), "Reservation ledger must contain a reservations array.")]
    for index, row in enumerate(data["reservations"]):
        label = f".github/id-reservations.json row {index + 1}"
        if not isinstance(row, dict) or set(("prefix", "numbers", "requested_by", "reserved_at")) - set(row):
            errors.append((label, "Malformed reservation row."))
            continue
        prefix, numbers = row["prefix"], row["numbers"]
        if prefix not in valid_prefixes or not isinstance(numbers, list) or not numbers:
            errors.append((label, "Invalid reservation prefix or empty numbers."))
            continue
        for number in numbers:
            if not isinstance(number, int) or not 1 <= number <= 9999:
                errors.append((label, f"Invalid four-digit reservation number: {number!r}"))
                continue
            permanent_id = f"{prefix}-{number:04d}"
            if permanent_id in reserved:
                errors.append((label, f"Duplicate reservation: {permanent_id}"))
            else:
                reserved[permanent_id] = label
    return reserved, errors


def load_deleted_ids(root, prefix_map):
    path = root / ".github/deleted-ids.json"
    if not path.exists():
        return set(), []
    errors, deleted = [], set()
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return set(), [(path.relative_to(root).as_posix(), f"Invalid deletion ledger: {exc}")]
    if data.get("schema_version") != 1 or not isinstance(data.get("deletions"), list):
        return set(), [(path.relative_to(root).as_posix(), "Deletion ledger must use schema_version 1 and contain a deletions array.")]
    valid_prefixes = set(prefix_map.values())
    for index, row in enumerate(data["deletions"]):
        label = f".github/deleted-ids.json row {index + 1}"
        required = {"id", "deleted_on", "authorized_by", "reason", "replacement"}
        if not isinstance(row, dict) or required - set(row):
            errors.append((label, "Malformed deletion row."))
            continue
        permanent_id = row["id"]
        match = PERMANENT_ID_RE.fullmatch(permanent_id) if isinstance(permanent_id, str) else None
        if not match or match.group(1) not in valid_prefixes or not 1 <= int(match.group(2)) <= 9999:
            errors.append((label, f"Invalid governed record ID: {permanent_id!r}"))
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(row["deleted_on"])):
            errors.append((label, "deleted_on must use YYYY-MM-DD."))
        if not isinstance(row["authorized_by"], str) or not row["authorized_by"].strip():
            errors.append((label, "authorized_by must identify the human authorizer."))
        if not isinstance(row["reason"], str) or not row["reason"].strip():
            errors.append((label, "reason must explain why hard deletion was authorised."))
        replacement = row["replacement"]
        if replacement is not None and not isinstance(replacement, str):
            errors.append((label, "replacement must be a permanent ID string or null."))
        if permanent_id in deleted:
            errors.append((label, f"Duplicate deletion tombstone: {permanent_id}"))
        deleted.add(permanent_id)
    return deleted, errors


def scan_tree(root, prefix_map, strict_paths=None):
    by_id, frontmatter_ids, stored_at = defaultdict(list), defaultdict(list), defaultdict(list)
    errors = []
    for folder, expected_prefix in prefix_map.items():
        base = root / folder
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.name in ("README.md", "index.md") or is_support_document(path):
                continue
            rel = path.relative_to(root).as_posix()
            strict = strict_paths is None or rel in strict_paths
            match = FILE_RE.match(path.name)
            if not match:
                errors.append((rel, "Filename does not match <PREFIX>-<NNNN>-<slug>.<ext>."))
                continue
            prefix, number = match.groups()
            if prefix != expected_prefix:
                errors.append((rel, f"Prefix '{prefix}' does not match folder '{folder}' (expected '{expected_prefix}')."))
                continue
            permanent_id = f"{prefix}-{number}"
            by_id[permanent_id].append(rel)
            if path.suffix.lower() == ".md":
                fm = frontmatter(path.read_text(encoding="utf-8"))
                if fm.get("id"):
                    frontmatter_ids[fm["id"]].append(rel)
                    if strict and fm["id"] != permanent_id:
                        errors.append((rel, f"Frontmatter id {fm['id']} does not match filename id {permanent_id}."))
                if fm.get("stored_at"):
                    target = safe_repo_target(root, fm["stored_at"])
                    if target is None:
                        if strict:
                            errors.append((rel, f"stored_at is not a safe repo-relative path: {fm['stored_at']}"))
                    else:
                        target_rel = target.relative_to(root.resolve()).as_posix()
                        stored_at[target_rel].append(rel)
                        if strict and not target.is_file():
                            errors.append((rel, f"stored_at target does not exist: {target_rel}"))
    for permanent_id, paths in sorted(by_id.items()):
        if len(paths) > 1:
            errors.append((paths[0], f"Duplicate permanent ID {permanent_id}: {', '.join(paths)}"))
    for permanent_id, paths in sorted(frontmatter_ids.items()):
        if len(paths) > 1:
            errors.append((paths[0], f"Duplicate frontmatter id {permanent_id}: {', '.join(paths)}"))
    for target, paths in sorted(stored_at.items()):
        if len(paths) > 1 and (strict_paths is None or any(path in strict_paths for path in paths)):
            errors.append((paths[0], f"Multiple companions claim stored_at {target}: {', '.join(paths)}"))
    return by_id, errors


def scan_shared_tree(root, shared_prefix_map):
    by_id, errors = defaultdict(list), []
    for folder, prefix in shared_prefix_map.items():
        if prefix != "CHAT":
            errors.append((".github/type-prefixes.json", f"Unsupported shared-file prefix: {prefix}"))
            continue
        base = root / folder
        if not base.exists():
            continue
        for path in base.glob("*.md"):
            if path.name in ("README.md", "index.md") or is_support_document(path):
                continue
            rel = path.relative_to(root).as_posix()
            if not FILENAME_PATTERN.fullmatch(path.name):
                errors.append((rel, "Shared Chat filename must match YYYY-MM-DD.md."))
                continue
            for number in extract_id_occurrences(path.read_text(encoding="utf-8")):
                by_id[f"{prefix}-{number:04d}"].append(rel)
    for permanent_id, paths in sorted(by_id.items()):
        if len(paths) > 1:
            errors.append((paths[0], f"Duplicate permanent ID {permanent_id}: {', '.join(paths)}"))
    return by_id, errors


def git_lines(args, root=REPO_ROOT):
    result = subprocess.run(args, cwd=root, capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return [line for line in result.stdout.splitlines() if line.strip()]


def fetch_base(base_ref, root=REPO_ROOT):
    subprocess.run(["git", "fetch", "origin", f"+refs/heads/{base_ref}:refs/remotes/origin/{base_ref}", "--depth=1000"], cwd=root, check=True)
    lines = git_lines(["git", "rev-parse", f"origin/{base_ref}^{{commit}}"], root)
    if len(lines) != 1 or not re.fullmatch(r"[0-9a-f]{40}", lines[0]):
        raise RuntimeError(f"Unable to resolve immutable origin/{base_ref} commit")
    return lines[0]


def existing_ids_for_folder(folder, prefix, base_sha):
    pattern = re.compile(rf"^{re.escape(prefix)}-(\d{{4}})-.+\.[A-Za-z0-9]+$")
    ids = set()
    for line in git_lines(["git", "ls-tree", "-r", "--name-only", base_sha, "--", folder]):
        match = pattern.match(Path(line).name)
        if match and Path(line).name not in ("README.md", "index.md"):
            ids.add(int(match.group(1)))
    return ids


def existing_ids_for_shared_folder(folder, prefix, base_sha):
    if prefix != "CHAT":
        raise RuntimeError(f"Unsupported shared-file prefix: {prefix}")
    ids = set()
    for line in git_lines(["git", "ls-tree", "-r", "--name-only", base_sha, "--", folder]):
        if Path(line).name in ("README.md", "index.md"):
            continue
        text = subprocess.run(
            ["git", "show", f"{base_sha}:{line}"], cwd=REPO_ROOT,
            capture_output=True, text=True, encoding="utf-8",
        )
        if text.returncode:
            raise RuntimeError(text.stderr.strip() or f"Unable to read {line} at base")
        if not is_support_document(line, text.stdout):
            ids.update(extract_ids(text.stdout))
    return ids


def deleted_ids_at_commit(base_sha, root=REPO_ROOT):
    result = subprocess.run(
        ["git", "show", f"{base_sha}:.github/deleted-ids.json"], cwd=root,
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode:
        return set()
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid base deletion ledger: {exc}") from exc
    return {row["id"] for row in data.get("deletions", []) if isinstance(row, dict) and isinstance(row.get("id"), str)}


def reservation_ids_at_commit(base_sha, root=REPO_ROOT):
    result = subprocess.run(
        ["git", "show", f"{base_sha}:.github/id-reservations.json"], cwd=root,
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode:
        raise RuntimeError("Unable to read base reservation ledger")
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid base reservation ledger: {exc}") from exc
    ids = set()
    for row in data.get("reservations", []):
        if not isinstance(row, dict) or not isinstance(row.get("prefix"), str) or not isinstance(row.get("numbers"), list):
            continue
        ids.update(f"{row['prefix']}-{number:04d}" for number in row["numbers"] if isinstance(number, int))
    return ids


def changed_files(base_sha):
    return git_lines(["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base_sha}...HEAD"])


def orphan_reservation_errors(reserved, all_tree_ids):
    return [
        (label, f"Orphan reservation {permanent_id}; reservations may merge only with their consuming file.")
        for permanent_id, label in reserved.items()
        if permanent_id not in all_tree_ids
    ]


def account_deleted_ids(existing, deleted_ids, base_deleted_ids, reserved, base_reserved=None):
    base_reserved = base_reserved or set()
    candidate_tombstones, errors = defaultdict(list), []
    for permanent_id in sorted(deleted_ids.intersection(base_deleted_ids)):
        prefix, number_text = permanent_id.split("-", 1)
        existing.setdefault(prefix, set()).add(int(number_text))
        if permanent_id in base_reserved and permanent_id not in reserved:
            errors.append((".github/id-reservations.json",
                           f"Retired ID {permanent_id} lost its permanent reservation receipt."))
    next_id = {prefix: max(numbers, default=0) + 1 for prefix, numbers in existing.items()}
    for permanent_id in sorted(deleted_ids):
        if permanent_id in base_deleted_ids:
            continue
        prefix, number_text = permanent_id.split("-", 1)
        number = int(number_text)
        if number not in existing.setdefault(prefix, set()):
            candidate_tombstones[prefix].append(number)
            if permanent_id not in reserved:
                errors.append((".github/deleted-ids.json",
                               f"New retired ID {permanent_id} has no serialized reservation receipt."))
        existing[prefix].add(number)
    return next_id, candidate_tombstones, errors


def allocation_contiguity_errors(new_ids, next_id):
    errors = []
    for prefix, ids in new_ids.items():
        if not ids:
            continue
        want = next_id.get(prefix, 1)
        for got in sorted(set(ids)):
            if got != want:
                errors.append((".github/id-reservations.json",
                               f"New {prefix} IDs are {sorted(ids)}; expected contiguous allocation beginning {prefix}-{want:04d}."))
                break
            want += 1
    return errors


def main():
    if len(sys.argv) != 2:
        print("usage: check_ids.py <base_ref>", file=sys.stderr)
        return 2
    base_ref = sys.argv[1]
    prefix_map, shared_prefix_map = load_prefix_config()
    reserved, errors = load_reservations(REPO_ROOT, prefix_map, shared_prefix_map)
    deleted_ids, deleted_errors = load_deleted_ids(REPO_ROOT, prefix_map)
    errors.extend(deleted_errors)

    try:
        base_sha = fetch_base(base_ref)
        existing = {prefix: existing_ids_for_folder(folder, prefix, base_sha)
                    for folder, prefix in prefix_map.items()}
        existing.update({prefix: existing_ids_for_shared_folder(folder, prefix, base_sha)
                         for folder, prefix in shared_prefix_map.items()})
        base_deleted_ids = deleted_ids_at_commit(base_sha)
        base_reserved = reservation_ids_at_commit(base_sha)
        next_id, candidate_tombstones, tombstone_errors = account_deleted_ids(
            existing, deleted_ids, base_deleted_ids, reserved, base_reserved)
        errors.extend(tombstone_errors)
        changed = changed_files(base_sha)
        added = git_lines(["git", "diff", "--name-only", "--diff-filter=A", f"{base_sha}...HEAD"])
        by_id, tree_errors = scan_tree(REPO_ROOT, prefix_map, set(changed))
        shared_by_id, shared_errors = scan_shared_tree(REPO_ROOT, shared_prefix_map)
        errors.extend(tree_errors)
        errors.extend(shared_errors)
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"::error::Unable to establish base IDs: {exc}")
        return 1

    new_ids = {prefix: [] for prefix in set(prefix_map.values()) | set(shared_prefix_map.values())}
    for path_str in added:
        path = Path(path_str)
        if len(path.parts) < 2 or path.parts[0] not in prefix_map or path.name in ("README.md", "index.md"):
            continue
        match = FILE_RE.match(path.name)
        if match and match.group(1) == prefix_map[path.parts[0]]:
            permanent_id = f"{match.group(1)}-{match.group(2)}"
            new_ids[match.group(1)].append(int(match.group(2)))
            if permanent_id not in reserved:
                errors.append((path_str, f"New ID {permanent_id} has no serialized reservation receipt."))

    for permanent_id, paths in shared_by_id.items():
        prefix, number_text = permanent_id.split("-", 1)
        number = int(number_text)
        if number not in existing[prefix]:
            new_ids[prefix].append(number)
            if permanent_id not in reserved:
                errors.append((paths[0], f"New ID {permanent_id} has no serialized reservation receipt."))

    for prefix, ids in candidate_tombstones.items():
        new_ids.setdefault(prefix, []).extend(ids)

    errors.extend(allocation_contiguity_errors(new_ids, next_id))

    all_tree_ids = set(by_id) | set(shared_by_id)
    for permanent_id in sorted(deleted_ids.intersection(all_tree_ids)):
        errors.append((".github/deleted-ids.json", f"Deleted ID {permanent_id} still has a live governed record."))
    errors.extend(orphan_reservation_errors(reserved, all_tree_ids | deleted_ids))

    for path, message in errors:
        print(f"::error file={path}::{message}")
    if not errors:
        print("Full-tree IDs, reservations, frontmatter IDs, stored_at ownership, and shared-file IDs clean.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
