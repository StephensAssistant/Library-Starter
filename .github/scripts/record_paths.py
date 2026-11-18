"""Shared recognition of non-record authoring support documents.

An underscore is not an ID/schema bypass: live identity declarations remain
records. Templates may carry frontmatter only with an explicit placeholder ID.
"""
import re
from pathlib import Path

from frontmatter_utils import parse_frontmatter


def is_support_document(path, content=None):
    path = Path(path)
    if not path.name.startswith("_") or path.suffix != ".md":
        return False
    if re.search(r"[A-Z]+-\d{4}(?:\b|_)", path.stem):
        return False
    if content is None:
        if not path.is_file():
            return False
        content = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    if content.startswith("---"):
        if fm is None or not re.fullmatch(r"[A-Z]+-<NNNN>", str(fm.get("id", ""))):
            return False
    # Concrete identities inside fenced examples are documentation, not entries.
    fence = None
    visible = []
    for line in content.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if match:
            token = match.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            visible.append(line)
    text = "\n".join(visible)
    if re.search(r"(?m)^###\s+CHAT-\d{4}\b|^Parent:\s*\[\[(?:PROJ|TICK)-\d{4}\]\]", text):
        return False
    return True
