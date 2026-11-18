#!/usr/bin/env python3
"""Deterministic local retrieval and compact inferred-discovery export.

GitHub is authoritative. Browser assistants use GitHub search/read at task time;
this module supplies the equivalent repository-side baseline, evaluation surface,
and advisory export without turning suggestions into confirmed relationships.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from frontmatter_utils import parse_frontmatter  # noqa: E402
from record_paths import is_support_document  # noqa: E402

ROOT = SCRIPT_DIR.parents[1]
RECORD_FOLDERS = ("Projects", "Tickets", "Planning", "Knowledge", "People", "Decisions",
                  "Chats", "Artifacts", "Playbooks", "Skills", "AIHats", "Workflows",
                  "Transcriptions")
ID_RE = re.compile(r"\b(?:PROJ|KNOW|PERS|DEC|TICK|CHAT|ART|PLAY|SKILL|HAT|FLOW|TRAN)-\d{4}\b", re.I)
TOKEN_RE = re.compile(r"[a-z0-9]+(?:[._/-][a-z0-9]+)*", re.I)
ENTITY_RE = re.compile(r"\b(?:[A-Z][A-Z0-9_]{2,}(?:\.[A-Z][A-Z0-9_]{1,})+|(?:INC|SR|CHN)-\d+)\b")
SCHEMA_VERSION = 7
SCORING_VERSION = "fixed-bm25-v1"
BM25_REFERENCE_DOCUMENTS = 100_000
BM25_REFERENCE_LENGTH = 500


def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def revision(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def tokens(text):
    return [token.lower() for token in TOKEN_RE.findall(text)]


def title_from(text, fm, fallback):
    if fm and fm.get("title"):
        return str(fm["title"])
    match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return match.group(1).strip() if match else fallback


def passages(text, limit=300, maximum=None):
    """Cover every section with bounded overlapping excerpts and source lines."""
    if limit < 2 or (maximum is not None and maximum < 1):
        raise ValueError("passage limits must be positive (limit >= 2)")
    rows, heading, body, start = [], "Document", [], 1

    def flush():
        value = "".join(body)
        step = max(1, limit - min(50, limit // 2))
        source_line, previous_offset = start, 0
        for offset in range(0, len(value), step):
            source_line += value[previous_offset:offset].count("\n")
            previous_offset = offset
            excerpt = value[offset:offset + limit]
            if excerpt.strip():
                rows.append((heading, source_line, excerpt))
            if offset + limit >= len(value):
                break

    for number, line in enumerate(text.splitlines(keepends=True), 1):
        if line.startswith("## "):
            flush()
            heading, body, start = line[3:].strip(), [], number + 1
        else:
            body.append(line)
    flush()
    rows = rows or [("Document", 1, text[:limit])]
    return rows if maximum is None else rows[:maximum]


def _git(*args, root=ROOT):
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


def source_files(root=ROOT, git_ref=None):
    def eligible(path):
        return path.endswith(".md") and Path(path).name.lower() != "index.md" \
            and path.split("/", 1)[0] in RECORD_FOLDERS
    if git_ref:
        output = _git("ls-tree", "-r", "--name-only", git_ref, root=root)
        return [path for path in output.splitlines() if eligible(path)]
    result = []
    for folder in RECORD_FOLDERS:
        base = root / folder
        if base.exists():
            result.extend(path.relative_to(root).as_posix() for path in base.rglob("*.md")
                          if path.name.lower() != "index.md")
    return sorted(result)


def read_source(path, root=ROOT, git_ref=None):
    if git_ref:
        try:
            return _git("show", f"{git_ref}:{path}", root=root)
        except subprocess.CalledProcessError:
            return None
    file_path = root / path
    return file_path.read_text(encoding="utf-8", errors="ignore") if file_path.exists() else None


def _changed_source_paths(root, prior):
    """Return changed record paths since the prior index, or None for a full scan."""
    if not prior or prior.get("schema_version") != SCHEMA_VERSION or not prior.get("source_commit"):
        return None, None
    try:
        current = _git("rev-parse", "HEAD", root=root).strip()
        previous = prior["source_commit"]
        subprocess.run(["git", "merge-base", "--is-ancestor", previous, current], cwd=root,
                       check=True, capture_output=True, text=True)
        output = _git("diff", "--name-status", "--find-renames", previous, "--", *RECORD_FOLDERS,
                      root=root)
        untracked = _git("ls-files", "--others", "--exclude-standard", "--", *RECORD_FOLDERS,
                         root=root)
    except (KeyError, OSError, subprocess.CalledProcessError):
        return None, None
    paths = set()
    for line in output.splitlines():
        fields = line.split("\t")
        if not fields:
            continue
        paths.update(fields[1:])
    paths.update(untracked.splitlines())
    return sorted(path for path in paths if path.endswith(".md")), current


def _document(path, text):
    if Path(path).name.lower() == "index.md" or text is None or is_support_document(path, text):
        return None
    source_revision = revision(text)
    fm = parse_frontmatter(text)
    entry_id = str(fm.get("id", "")).upper() if fm else ""
    if not ID_RE.fullmatch(entry_id) or not Path(path).stem.upper().startswith(entry_id):
        return None
    links = []
    if fm and isinstance(fm.get("links"), list):
        links = sorted({str(item).upper() for item in fm["links"] if ID_RE.fullmatch(str(item))})
    title = title_from(text, fm, entry_id)
    body_tokens = tokens(title + "\n" + text)
    return entry_id, {
        "id": entry_id, "path": path, "revision": source_revision, "title": title,
        "length": len(body_tokens), "term_counts": dict(sorted(Counter(body_tokens).items())),
        "entities": sorted({match.lower() for match in ENTITY_RE.findall(text)}),
        "links": links,
        "passages": [[heading, line, value] for heading, line, value in passages(text)],
    }


def build_documents(root=ROOT, git_ref=None, prior=None):
    documents = {}
    prior_documents = (prior or {}).get("documents", {}) if isinstance(prior, dict) else {}
    changed_paths, _ = _changed_source_paths(root, prior) if not git_ref else (None, None)
    if changed_paths is not None:
        documents = copy.deepcopy(prior_documents)
        for path in changed_paths:
            for entry_id in [key for key, row in documents.items() if row.get("path") == path]:
                del documents[entry_id]
        paths = changed_paths
    else:
        paths = source_files(root, git_ref)
    for path in paths:
        text = read_source(path, root, git_ref)
        parsed = _document(path, text)
        if not parsed:
            continue
        entry_id, document = parsed
        source_revision = document["revision"]
        prior_id = next((entry_id for entry_id, row in prior_documents.items()
                         if row.get("path") == path and row.get("revision") == source_revision), None)
        if prior_id:
            documents[prior_id] = prior_documents[prior_id]
            continue
        documents[entry_id] = document
    return dict(sorted(documents.items()))


def build_index(root=ROOT, git_ref=None, prior=None):
    compatible_prior = prior if (not git_ref and isinstance(prior, dict)
                                 and prior.get("schema_version") == SCHEMA_VERSION) else None
    documents = build_documents(root, git_ref, prior=compatible_prior)
    manifest = {key: value["revision"] for key, value in documents.items()}
    previous_documents = compatible_prior.get("documents", {}) if compatible_prior else {}
    next_ordinal = int((compatible_prior or {}).get("next_ordinal", 0))
    for entry_id, document in documents.items():
        if entry_id in previous_documents and "ordinal" in previous_documents[entry_id]:
            document["ordinal"] = previous_documents[entry_id]["ordinal"]
        elif "ordinal" not in document:
            document["ordinal"] = next_ordinal
            next_ordinal += 1
    if compatible_prior and isinstance(compatible_prior.get("postings"), dict):
        postings = {term: {ordinal: frequency for ordinal, frequency in rows}
                    for term, rows in compatible_prior["postings"].items()}
    else:
        postings = {}
    changed = changed_ids({"documents": documents}, compatible_prior)
    removed_ordinals = {previous_documents[entry_id]["ordinal"] for entry_id in changed
                        if entry_id in previous_documents}
    for term in list(postings):
        for ordinal in removed_ordinals:
            postings[term].pop(ordinal, None)
        if not postings[term]:
            del postings[term]
    for entry_id, document in documents.items():
        counts = document.pop("term_counts", None)
        if counts is None:
            continue
        for term, frequency in counts.items():
            postings.setdefault(term, {})[document["ordinal"]] = frequency
    postings = {term: [[ordinal, frequency] for ordinal, frequency in sorted(rows.items())]
                for term, rows in sorted(postings.items())}
    source_commit = None
    if not git_ref:
        changed_paths, current = _changed_source_paths(root, compatible_prior)
        if changed_paths:
            source_commit = current
        elif compatible_prior:
            source_commit = compatible_prior.get("source_commit")
        if not source_commit:
            try:
                source_commit = _git("rev-parse", "HEAD", root=root).strip()
            except (OSError, subprocess.CalledProcessError):
                source_commit = None
    return {
        "schema_version": SCHEMA_VERSION,
        "owner": "library_retrieval.py",
        "source_ref": git_ref or "working-tree",
        "source_commit": git_ref or source_commit,
        "scoring_version": SCORING_VERSION,
        "next_ordinal": next_ordinal,
        "corpus_hash": revision(canonical_json(manifest)),
        "documents": documents,
        "postings": postings,
        "incremental": {"strategy": "changed records plus affected and reverse-displaced neighbours"},
    }


def changed_ids(index, prior):
    current = index.get("documents", {})
    previous = (prior or {}).get("documents", {}) if isinstance(prior, dict) else {}
    return sorted(key for key in set(current) | set(previous)
                  if current.get(key, {}).get("revision") != previous.get(key, {}).get("revision"))


def _idf(index):
    return {term: math.log(1 + (BM25_REFERENCE_DOCUMENTS - len(rows) + 0.5) / (len(rows) + 0.5))
            for term, rows in index["postings"].items()}


def rank(index, query, limit=10, confirmed_depth=1):
    if index.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Incompatible retrieval index; rebuild before querying.")
    documents = index["documents"]
    query_tokens = tokens(query)
    exact_ids = {item.upper() for item in ID_RE.findall(query)}
    if exact_ids and not (exact_ids & set(documents)):
        return []
    query_entities = {item.lower() for item in ENTITY_RE.findall(query)}
    idf = _idf(index)
    ordinal_ids = {document["ordinal"]: entry_id for entry_id, document in documents.items()}
    scores = defaultdict(float)
    reasons = defaultdict(list)
    lexical = set()
    for entry_id in exact_ids:
        if entry_id in documents:
            scores[entry_id] += 1000.0
            reasons[entry_id].append("exact_id")
    for term in query_tokens:
        for ordinal, frequency in index["postings"].get(term, []):
            entry_id = ordinal_ids.get(ordinal)
            if entry_id is None:
                continue
            doc = documents[entry_id]
            denom = frequency + 1.2 * (1 - 0.75 + 0.75 * doc["length"] / BM25_REFERENCE_LENGTH)
            scores[entry_id] += idf.get(term, 0.0) * (frequency * 2.2 / denom)
            lexical.add(entry_id)
    for entry_id, doc in documents.items():
        overlap = sorted(query_entities & set(doc["entities"]))
        if overlap:
            scores[entry_id] += 4.0 * len(overlap)
            reasons[entry_id].append("entity:" + ",".join(overlap))
    scored = []
    for entry_id, score in scores.items():
        if score >= 1.0:
            if entry_id in lexical:
                reasons[entry_id].append("bm25")
            scored.append((score, entry_id, reasons[entry_id]))
    scored.sort(key=lambda row: (-row[0], row[1]))
    results = []
    seen = set()
    for score, entry_id, reasons in scored:
        if entry_id in seen:
            continue
        doc = documents[entry_id]
        passage = max(doc["passages"], key=lambda row: sum(tokens(row[2]).count(t) for t in query_tokens))
        results.append({"id": entry_id, "path": doc["path"], "source_revision": doc["revision"],
                        "score": round(score, 6), "evidence_kind": "source", "reasons": reasons,
                        "passage": {"heading": passage[0], "line": passage[1], "text": passage[2]}})
        seen.add(entry_id)
        if len(results) >= limit:
            break
    if confirmed_depth and results:
        seeds = list(results[:min(3, len(results))])
        for seed in seeds:
            for linked in documents[seed["id"]]["links"]:
                if linked in documents and linked not in seen and len(results) < limit:
                    doc = documents[linked]
                    passage = doc["passages"][0]
                    results.append({"id": linked, "path": doc["path"], "source_revision": doc["revision"],
                                    "score": round(seed["score"] * 0.5, 6), "evidence_kind": "confirmed_link",
                                    "reasons": ["confirmed_link_from:" + seed["id"]],
                                    "passage": {"heading": passage[0], "line": passage[1], "text": passage[2]}})
                    seen.add(linked)
    return results


def diagnostic(index, query, expected_id=None, limit=10):
    if index.get("schema_version") != SCHEMA_VERSION:
        return {"cause": "incompatible_index", "query": query, "expected_id": expected_id,
                "action": "Rebuild the retrieval index before querying."}
    current = build_documents(ROOT)
    current_hash = revision(canonical_json({k: v["revision"] for k, v in current.items()}))
    if current_hash != index.get("corpus_hash"):
        cause = "stale_index"
    elif expected_id and expected_id not in index.get("documents", {}):
        cause = "missing_evidence"
    elif expected_id and expected_id not in {row["id"] for row in rank(index, query, limit)}:
        cause = "ranking_failure"
    else:
        cause = "ok"
    return {"cause": cause, "query": query, "expected_id": expected_id}


def _suggestions_for(index, entry_id, cap, minimum):
    doc = index["documents"][entry_id]
    candidates = []
    for result in rank(index, doc["title"], limit=cap + 8, confirmed_depth=0):
            if result["id"] == entry_id or result["score"] < minimum or result["id"] in doc["links"]:
                continue
            candidates.append({"target": result["id"], "score": result["score"],
                               "reason": result["reasons"], "source_revision": doc["revision"],
                               "target_revision": result["source_revision"]})
            if len(candidates) == cap:
                break
    return candidates


def _advisory(index, cap, rows):
    return {"schema_version": 1, "owner": "library_retrieval.py", "layer": "inferred_advisory",
            "scoring_version": SCORING_VERSION,
            "corpus_hash": index["corpus_hash"], "saved_suggestion_cap": cap,
            "records": dict(sorted(rows.items())),
            "note": "Suggestions are hypotheses; zero suggestions is valid and none are confirmed automatically."}


def suggestions(index, cap=3, minimum=2.0):
    rows = {}
    for entry_id in index["documents"]:
        candidates = _suggestions_for(index, entry_id, cap, minimum)
        if candidates:
            rows[entry_id] = candidates
    return _advisory(index, cap, rows)


def update_suggestions(index, prior_index, prior_advisory, cap=3, minimum=2.0):
    """Incrementally update suggestions, including reverse-neighbour displacement."""
    if (not prior_index or prior_index.get("schema_version") != SCHEMA_VERSION
            or not prior_advisory or prior_advisory.get("schema_version") != 1
            or prior_advisory.get("owner") != "library_retrieval.py"
            or prior_advisory.get("scoring_version") != SCORING_VERSION
            or prior_advisory.get("saved_suggestion_cap") != cap
            or prior_advisory.get("corpus_hash") != prior_index.get("corpus_hash")
            or not isinstance(prior_advisory.get("records"), dict)):
        return suggestions(index, cap, minimum)
    current = index["documents"]
    previous = prior_index.get("documents", {})
    changed = set(changed_ids(index, prior_index))
    if not changed:
        rows = copy.deepcopy(prior_advisory.get("records", {}))
        return _advisory(index, cap, rows)

    changed_terms = {term for term in set(index.get("postings", {})) | set(prior_index.get("postings", {}))
                     if index.get("postings", {}).get(term) != prior_index.get("postings", {}).get(term)}
    changed_entities = set()
    for entry_id in changed:
        for document in (current.get(entry_id), previous.get(entry_id)):
            if document:
                changed_entities.update(document.get("entities", []))

    affected = set(changed)
    for source_id, document in current.items():
        if set(tokens(document["title"])) & changed_terms or set(document.get("entities", [])) & changed_entities:
            affected.add(source_id)
    for source_id, candidates in prior_advisory.get("records", {}).items():
        if any(row.get("target") in changed for row in candidates):
            affected.add(source_id)

    rows = copy.deepcopy(prior_advisory.get("records", {}))
    for entry_id in set(rows) - set(current):
        del rows[entry_id]
    for entry_id in sorted(affected & set(current)):
        candidates = _suggestions_for(index, entry_id, cap, minimum)
        if candidates:
            rows[entry_id] = candidates
        else:
            rows.pop(entry_id, None)
    return _advisory(index, cap, rows)


def write_if_changed(path, value, compact=False):
    rendered = (canonical_json(value) if compact else json.dumps(
        value, indent=2, sort_keys=True, ensure_ascii=False)) + "\n"
    before = path.read_text(encoding="utf-8") if path.exists() else None
    if before != rendered:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
        return True
    return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build")
    build.add_argument("--index", type=Path, required=True)
    build.add_argument("--suggestions", type=Path)
    build.add_argument("--cap", type=int, default=3)
    query = sub.add_parser("query")
    query.add_argument("text")
    query.add_argument("--index", type=Path)
    query.add_argument("--limit", type=int, default=10)
    query.add_argument("--expected-id")
    args = parser.parse_args(argv)
    if args.command == "build":
        prior = json.loads(args.index.read_text()) if args.index.exists() else None
        prior_advisory = (json.loads(args.suggestions.read_text())
                          if args.suggestions and args.suggestions.exists() else None)
        index = build_index(prior=prior)
        changed = write_if_changed(args.index, index, compact=True)
        if args.suggestions:
            advisory = update_suggestions(index, prior, prior_advisory, args.cap)
            changed = write_if_changed(args.suggestions, advisory, compact=True) or changed
        print(canonical_json({"changed": changed, "corpus_hash": index["corpus_hash"],
                              "changed_or_deleted": changed_ids(index, prior)}))
    else:
        index = json.loads(args.index.read_text()) if args.index else build_index()
        check = diagnostic(index, args.text, args.expected_id, args.limit)
        incompatible = check["cause"] == "incompatible_index"
        result = {"source_ref": index.get("source_ref"), "corpus_hash": index.get("corpus_hash"),
                  "results": [] if incompatible else rank(index, args.text, args.limit),
                  "diagnostic": check}
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 2 if incompatible else 0


if __name__ == "__main__":
    raise SystemExit(main())

