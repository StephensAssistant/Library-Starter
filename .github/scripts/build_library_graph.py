#!/usr/bin/env python3
"""Generate the offline Library graph from the destination checkout."""

import argparse
import json
import re
from pathlib import Path

import library_scan
from chat_utils import FILENAME_PATTERN


TEMPLATE = Path('.github/templates/ART-0134-library-knowledge-graph.html')
OUTPUT = Path('Catalog/library-knowledge-graph.html')
PAYLOAD = re.compile(r'(<script id="library-graph-data" type="application/json">).*?(</script>)', re.S)
CHAT_HEADING = re.compile(r'^### (CHAT-\d{4}) — [^\r\n]*', re.M)
LINK_IDS = re.compile(r'\b[A-Z]+-\d{4}\b')


def chat_links(root):
    """Read the Library's dated chat sections and their explicit outbound links."""
    links = {}
    for path in sorted((root / 'Chats').glob('*.md')):
        if path.is_symlink() or not FILENAME_PATTERN.fullmatch(path.name):
            continue
        text = path.read_text(encoding='utf-8')
        headings = list(CHAT_HEADING.finditer(text))
        for i, heading in enumerate(headings):
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            line = re.search(r'^Links:\s*\[([^\r\n\]]*)\]', text[heading.end():end], re.M)
            links[heading.group(1)] = LINK_IDS.findall(line.group(1)) if line else []
    return links


def build_topology(entries, chats):
    """Project explicit links to anonymous endpoints. Unresolved links stay out."""
    relationship_map = {
        record_id: entry['fm'].get('links', []) for record_id, entry in entries.items()
    }
    relationship_map.update(chats)
    aliases = {
        record_id: f'NODE-{number:04d}'
        for number, record_id in enumerate(sorted(relationship_map), 1)
    }
    edges = set()
    for record_id, links in relationship_map.items():
        if not isinstance(links, list):
            continue
        for target in links:
            if isinstance(target, str) and target in aliases and target != record_id:
                edges.add(tuple(sorted((aliases[record_id], aliases[target]))))
    return {
        'schema_version': 'public-topology-v1',
        'public_safe': True,
        'nodes': [{'id': alias} for alias in aliases.values()],
        'links': [[source, target, True] for source, target in sorted(edges)],
    }


def render(template, topology):
    encoded = json.dumps(topology, separators=(',', ':'), ensure_ascii=True).replace('<', r'\u003c')
    if len(PAYLOAD.findall(template)) != 1:
        raise ValueError('Graph template must contain exactly one graph data payload')
    return PAYLOAD.sub(lambda match: f'{match[1]}{encoded}{match[2]}', template)


def generate(artifact=None):
    root = library_scan.REPO_ROOT
    entries = library_scan.collect_entries()
    output = OUTPUT
    if artifact is not None:
        if not re.fullmatch(r'Artifacts/ART-[0-9]{4}-[a-z0-9-]+\.html', artifact):
            raise ValueError('Use the existing native ART HTML path in Artifacts/')
        output = Path(artifact)
        target = root / output
        owners = [
            entry for entry in entries.values()
            if entry['fm'].get('type') == 'artifact' and entry['fm'].get('stored_at') == artifact
        ]
        if (len(owners) != 1 or not target.is_file() or target.is_symlink()
                or not target.resolve().is_relative_to(root.resolve())
                or 'name="library-graph-renderer"' not in target.read_text(encoding='utf-8')):
            raise ValueError('Refresh requires an existing graph HTML with exactly one companion')
    for record_id, entry in library_scan.collect_native_artifact_entries(entries).items():
        path = entry['path']
        if not path.is_symlink() and path.is_file() and path.resolve().is_relative_to(root.resolve()):
            if record_id not in entries:
                entries[record_id] = entry
    topology = build_topology(entries, chat_links(root))
    result = render((root / TEMPLATE).read_text(encoding='utf-8'), topology)
    target = root / output
    if target.is_symlink() or not target.resolve().is_relative_to(root.resolve()):
        raise ValueError('Graph output must be inside this Library')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(result, encoding='utf-8', newline='\n')
    print(f'{output.as_posix()}: {len(topology["nodes"])} nodes, {len(topology["links"])} links')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-artifact', metavar='ARTIFACT_PATH')
    generate(parser.parse_args().refresh_artifact)
