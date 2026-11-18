#!/usr/bin/env python3
"""
Shared entry-scanning logic, used by build_tag_index.py, auto_heal_links.py,
build_folder_indexes.py, and build_board.py. Kept as one module for the same
reason frontmatter_utils.py is: multiple copies of "scan every folder, parse
every entry" would drift apart silently.
"""
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
from frontmatter_utils import parse_frontmatter  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parents[1]


def load_prefix_map():
    data = json.loads((REPO_ROOT / ".github" / "type-prefixes.json").read_text())
    return data["folders"]


def collect_entries():
    """Returns {id: {'path': Path, 'folder': str, 'fm': dict}} for every
    real entry across every mapped type folder. Chats excluded (no
    per-entry frontmatter). Artifacts' raw files excluded (no
    frontmatter at all) - only the companion record is included."""
    prefix_map = load_prefix_map()
    entries = {}
    for folder in prefix_map:
        folder_path = REPO_ROOT / folder
        if not folder_path.exists():
            continue
        for f in sorted(folder_path.iterdir()):
            if f.name == "README.md" or not f.is_file():
                continue
            content = f.read_text(errors="ignore")
            if is_support_document(f, content):
                continue
            fm = parse_frontmatter(content)
            if fm is None:
                continue
            entry_id = fm.get("id")
            if not entry_id:
                continue
            entries[entry_id] = {"path": f, "folder": folder, "fm": fm}
    return entries


def collect_native_artifact_entries(entries):
    """Return metadata projections for native files owned by companions."""
    native = {}
    for companion_id, data in entries.items():
        fm = data["fm"]
        if fm.get("type") != "artifact":
            continue
        stored_at = fm.get("stored_at")
        if not isinstance(stored_at, str):
            continue
        match = re.match(r"^(ART-\d{4})(?:-|\.)", Path(stored_at).name)
        if not match or match.group(1) == companion_id:
            continue
        native_id = match.group(1)
        native[native_id] = {
            "path": REPO_ROOT / stored_at,
            "folder": "Artifacts",
            "fm": {
                "type": "artifact",
                "title": f"{fm.get('title', native_id)} — native file",
                "status": fm.get("status"),
                "links": list(fm.get("links", [])) if isinstance(fm.get("links"), list) else [],
            },
        }
    return native
