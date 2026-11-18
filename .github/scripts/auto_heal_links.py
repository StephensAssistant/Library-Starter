#!/usr/bin/env python3
"""Live reciprocal-edge auto-heal.

Drive migration is closed. This script no longer reads Catalog/MIGRATION-MAP.md.

1. Promote leftover migrated_links_pending values on frontmatter records only when
   the old ID is already live or listed in .github/migration-link-overrides.json.
2. Heal reciprocal edges across frontmatter records, including raw Artifact owners.
3. Treat daily Chat links as directional provenance: recognize their endpoints,
   remove proven reciprocal frontmatter backlinks, and never rewrite Chat blocks.
4. Leave only genuinely unmapped leftover old IDs pending.

Idempotent. --check reports debt without writing and exits non-zero.
"""
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
from library_scan import collect_entries  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]
ID_RE = re.compile(r"\b(?:PROJ|KNOW|PERS|DEC|TICK|CHAT|ART|PLAY|SKILL|HAT|FLOW|TRAN)-\d{4}\b")
CHECK = "--check" in sys.argv
OVERRIDES_PATH = REPO_ROOT / ".github" / "migration-link-overrides.json"


def load_overrides():
    if not OVERRIDES_PATH.exists():
        return {"global_aliases": {}, "source_overrides": {}}
    data = json.loads(OVERRIDES_PATH.read_text())
    return {
        "global_aliases": data.get("global_aliases", {}),
        "source_overrides": data.get("source_overrides", {}),
    }


def resolve_target(source_id, old_id, known, overrides):
    source_target = overrides["source_overrides"].get(source_id, {}).get(old_id)
    if source_target:
        return source_target
    alias_target = overrides["global_aliases"].get(old_id)
    if alias_target:
        return alias_target
    if old_id in known:
        return old_id
    return None


def render_list(values):
    return "[" + ", ".join(sorted(set(values))) + "]"


def rewrite_frontmatter(path, links, pending):
    lines = path.read_text().splitlines(keepends=True)
    bounds = [i for i, line in enumerate(lines) if line.strip() == "---"]
    if len(bounds) < 2:
        raise ValueError(f"{path}: missing frontmatter delimiters")
    start, end = bounds[0], bounds[1]
    link_index = pending_index = None
    for i in range(start + 1, end):
        if lines[i].startswith("links:"):
            link_index = i
        elif lines[i].startswith("migrated_links_pending:"):
            pending_index = i
    if link_index is None:
        raise ValueError(f"{path}: missing links field")
    newline = "\n" if lines[link_index].endswith("\n") else ""
    lines[link_index] = f"links: {render_list(links)}{newline}"
    if pending_index is not None:
        if pending:
            newline = "\n" if lines[pending_index].endswith("\n") else ""
            lines[pending_index] = f"migrated_links_pending: {render_list(pending)}{newline}"
        else:
            del lines[pending_index]
    elif pending:
        lines.insert(link_index + 1, f"migrated_links_pending: {render_list(pending)}\n")
    return "".join(lines)


def load_chat_links():
    """Return each live Chat's outbound provenance links."""
    chats = {}
    for path in sorted((REPO_ROOT / "Chats").glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()
        if is_support_document(path, text):
            continue
        for block in re.split(r"(?=^### CHAT-\d{4} — )", text, flags=re.M):
            heading = re.match(r"^### (CHAT-\d{4}) — ", block)
            if not heading:
                continue
            link_match = re.search(r"^Links:\s*\[([^\]]*)\]", block, flags=re.M)
            chats[heading.group(1)] = set(ID_RE.findall(link_match.group(1))) if link_match else set()
    return chats


def directional_chat_backlinks(graph, chat_links):
    """Classify removable mirrored backlinks and invalid record-origin Chat edges."""
    removals = defaultdict(set)
    invalid = []
    for source, targets in graph.items():
        if source.startswith("CHAT-"):
            continue
        for target in targets:
            if not target.startswith("CHAT-"):
                continue
            if source in chat_links.get(target, set()):
                removals[source].add(target)
            else:
                invalid.append((source, target))
    return removals, sorted(invalid)


def raw_artifact_owners(entries):
    """Map raw Artifact IDs to the companion record that owns their metadata and edges."""
    owners = {}
    for companion_id, data in entries.items():
        if data["folder"] != "Artifacts":
            continue
        stored_at = data["fm"].get("stored_at")
        if not isinstance(stored_at, str):
            continue
        match = ID_RE.search(Path(stored_at).name)
        if match and match.group(0) != companion_id:
            owners[match.group(0)] = companion_id
    return owners


def reciprocal_additions(graph, known, raw_owners):
    """Return missing reciprocal edges, excluding every directional Chat edge."""
    additions = defaultdict(set)
    for source, targets in graph.items():
        if source.startswith("CHAT-"):
            continue
        for target in targets:
            if target.startswith("CHAT-") or target not in known:
                continue
            reciprocal_target = raw_owners.get(target, target)
            if (
                not reciprocal_target.startswith("CHAT-")
                and reciprocal_target != source
                and source not in graph[reciprocal_target]
                and not any(
                    raw_owners.get(link) == source
                    for link in graph[reciprocal_target]
                )
            ):
                additions[reciprocal_target].add(source)
    return additions


def reciprocal_fixed_point(graph, known, raw_owners):
    """Return the healed graph without mutating the caller's graph."""
    healed = {eid: set(targets) for eid, targets in graph.items()}
    while True:
        additions = reciprocal_additions(healed, known, raw_owners)
        if not additions:
            return healed
        for eid, values in additions.items():
            healed[eid].update(values)


def main():
    overrides = load_overrides()
    entries = {
        eid: data for eid, data in collect_entries().items()
        if isinstance(data["fm"].get("links"), list)
    }
    chat_links = load_chat_links()
    chats = set(chat_links)
    raw_owners = raw_artifact_owners(entries)
    known = set(entries) | chats | set(raw_owners)
    changed_frontmatter = set()

    for eid, data in entries.items():
        pending = data["fm"].get("migrated_links_pending")
        if not isinstance(pending, list):
            continue
        links = set(data["fm"]["links"])
        remaining = []
        for old_id in pending:
            new_id = resolve_target(eid, old_id, known, overrides)
            if new_id in known:
                links.add(new_id)
            else:
                remaining.append(old_id)
        if links != set(data["fm"]["links"]) or remaining != pending:
            data["fm"]["links"] = sorted(links)
            data["fm"]["migrated_links_pending"] = remaining
            changed_frontmatter.add(eid)

    graph = {eid: set(data["fm"]["links"]) for eid, data in entries.items()}
    removals, invalid_chat_edges = directional_chat_backlinks(graph, chat_links)
    if invalid_chat_edges:
        for source, target in invalid_chat_edges:
            print(
                f"Invalid directional Chat edge: {source} links to {target}, "
                "but the Chat does not cite the record as outbound provenance."
            )
        return 1
    for eid, targets in removals.items():
        graph[eid].difference_update(targets)
        entries[eid]["fm"]["links"] = sorted(graph[eid])
        changed_frontmatter.add(eid)
    graph.update({raw_id: set() for raw_id in raw_owners})
    healed_graph = reciprocal_fixed_point(graph, known, raw_owners)
    for eid in entries:
        if healed_graph[eid] != graph[eid]:
            entries[eid]["fm"]["links"] = sorted(healed_graph[eid])
            changed_frontmatter.add(eid)

    changed_paths = set()
    for eid in sorted(changed_frontmatter):
        data = entries[eid]
        pending = data["fm"].get("migrated_links_pending", [])
        content = rewrite_frontmatter(data["path"], data["fm"]["links"], pending)
        changed_paths.add(data["path"])
        if not CHECK:
            data["path"].write_text(content)

    for path in sorted(changed_paths):
        print(f"Healed {path.relative_to(REPO_ROOT)}")
    print(
        f"Relationship reconciliation: {len(changed_paths)} file(s), "
        f"{len(changed_frontmatter)} record(s), 0 Chat(s)."
    )

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as handle:
            handle.write(f"changed={'true' if changed_paths else 'false'}\n")
    if CHECK and changed_paths:
        sys.exit(1)


if __name__ == "__main__":
    raise SystemExit(main())
