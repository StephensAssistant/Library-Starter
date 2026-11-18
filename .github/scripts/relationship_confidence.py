#!/usr/bin/env python3
"""Validate and score evidence-backed Library relationships.

Scores are deterministic evidence-strength indicators, not probabilities.
Dates are audit facts only: v1 deliberately applies no ageing or decay.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from record_paths import is_support_document
REPO_ROOT = SCRIPT_DIR.parents[1]
LEDGER_PATH = REPO_ROOT / ".github" / "relationship-evidence.json"
SCORING_MODEL = "relationship-confidence-v1"
SCALE = 10_000
LEGACY_BASELINE = 4_000
MAX_LEDGER_BYTES = 5_000_000
ID_RE = re.compile(r"^(?:PROJ|KNOW|PERS|DEC|TICK|CHAT|ART|PLAY|SKILL|HAT|FLOW|TRAN)-\d{4}$")
LINK_ID_RE = re.compile(r"\b(?:PROJ|KNOW|PERS|DEC|TICK|CHAT|ART|PLAY|SKILL|HAT|FLOW|TRAN)-\d{4}\b")
EVIDENCE_ID_RE = re.compile(r"^EVD-[A-Z0-9][A-Z0-9_-]{2,63}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
GENERATED_GRAPH_NAMES = {"library-knowledge-graph.html"}

SUPPORT_WEIGHTS = {
    "owner_confirmation": 3_000,
    "authoritative_record": 2_500,
    "validated_outcome": 2_000,
    "independent_corroboration": 1_500,
    "successful_use": 1_000,
}
CONTRADICTION_WEIGHT = 6_000
UNDIRECTED_TYPES = {"related_to"}
DIRECTED_TYPES = {
    "supports", "depends_on", "implements", "documents",
    "supersedes", "owned_by", "originated_from", "blocks",
}
RELATIONSHIP_TYPES = UNDIRECTED_TYPES | DIRECTED_TYPES
DISPOSITIONS = {"candidate", "confirmed", "rejected"}
OUTCOMES = {"supports", "contradicts"}


class ConfidenceError(ValueError):
    """Raised when relationship evidence fails closed validation."""


@dataclass(frozen=True)
class EdgeScore:
    score: int
    band: str
    status: str
    independent_evidence_count: int
    supporting_evidence_count: int
    contradicting_evidence_count: int


def canonical_edge(left: str, right: str) -> tuple[str, str, str]:
    if left == right:
        raise ConfidenceError(f"self-edge is forbidden: {left}")
    a, b = sorted((left, right))
    return a, b, f"{a}--{b}"


def _combine(score: int, weight: int) -> int:
    """Fixed-point noisy-OR; integer-only for cross-run determinism."""
    return SCALE - (((SCALE - score) * (SCALE - weight) + SCALE // 2) // SCALE)


def _band(score: int) -> str:
    if score >= 8_000:
        return "high"
    if score >= 6_000:
        return "medium"
    if score > 0:
        return "low"
    return "unknown"


def _validate_date(value: object, field: str) -> None:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        raise ConfidenceError(f"{field} must be YYYY-MM-DD")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ConfidenceError(f"{field} is not a real date") from exc


def _blob_text(blob_sha: str, source_path: str, supplied: dict[tuple[str, str], str] | None) -> str:
    if supplied is not None:
        key = (blob_sha, source_path)
        if key not in supplied:
            raise ConfidenceError(f"evidence source blob is not bound to canonical path: {blob_sha} {source_path}")
        return supplied[key]

    history = subprocess.run(
        ["git", "rev-list", "--objects", "HEAD", "--", source_path], cwd=REPO_ROOT,
        capture_output=True, text=True,
    )
    if history.returncode != 0 or f"{blob_sha} {source_path}" not in history.stdout.splitlines():
        raise ConfidenceError(f"evidence source blob is not a canonical path version: {blob_sha} {source_path}")
    result = subprocess.run(
        ["git", "cat-file", "blob", blob_sha], cwd=REPO_ROOT,
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise ConfidenceError(f"evidence source blob unavailable: {blob_sha}")
    return result.stdout


def _record_text(blob: str, source_id: str) -> str:
    if source_id.startswith("CHAT-"):
        match = re.search(
            rf"^### {re.escape(source_id)} —.*?(?=^### CHAT-\d{{4}} —|\Z)",
            blob, flags=re.M | re.S,
        )
        if not match:
            raise ConfidenceError(f"Chat source id is not present as its own block: {source_id}")
        return match.group(0)
    if not re.search(rf"(?m)^id:\s*{re.escape(source_id)}\s*$", blob):
        raise ConfidenceError(f"source blob is not the claimed canonical record: {source_id}")
    return blob


def evidence_declaration(record: dict, item: dict) -> str:
    return (
        f"RELATIONSHIP-EVIDENCE: {record['edge_id']} | {record['relationship_type']} | "
        f"{record['direction']} | {item['kind']} | {item['outcome']}"
    )


def validate_evidence(item: object, record: dict, known_ids: set[str], source_paths: dict[str, str], source_blobs: dict[tuple[str, str], str] | None = None, validate_source: bool = True) -> dict:
    if not isinstance(item, dict):
        raise ConfidenceError("evidence item must be an object")
    required = {"id", "kind", "outcome", "source_id", "source_sha", "sequence", "anchor", "observed_at", "state"}
    allowed = required | {"resolution_ref"}
    missing = sorted(required - item.keys())
    if missing:
        raise ConfidenceError(f"evidence missing fields: {', '.join(missing)}")
    extra = sorted(item.keys() - allowed)
    if extra:
        raise ConfidenceError(f"evidence has unsupported fields: {', '.join(extra)}")
    if not isinstance(item["id"], str) or not EVIDENCE_ID_RE.fullmatch(item["id"]):
        raise ConfidenceError("invalid evidence id")
    if item["kind"] not in SUPPORT_WEIGHTS:
        raise ConfidenceError(f"unknown evidence kind: {item['kind']}")
    if item["outcome"] not in OUTCOMES:
        raise ConfidenceError(f"invalid evidence outcome: {item['outcome']}")
    if item["source_id"] not in known_ids:
        raise ConfidenceError(f"unknown evidence source: {item['source_id']}")
    if item["source_id"] not in source_paths:
        raise ConfidenceError(f"canonical path unavailable for evidence source: {item['source_id']}")
    if Path(source_paths[item["source_id"]]).name in GENERATED_GRAPH_NAMES:
        raise ConfidenceError(f"generated output cannot be evidence: {item['source_id']}")
    if not isinstance(item["source_sha"], str) or not SHA_RE.fullmatch(item["source_sha"]):
        raise ConfidenceError("source_sha must be a full lowercase Git blob SHA")
    if not isinstance(item["sequence"], int) or isinstance(item["sequence"], bool) or item["sequence"] <= 0:
        raise ConfidenceError("evidence sequence must be a positive integer")
    if not isinstance(item["anchor"], str) or len(item["anchor"].strip()) < 12 or len(item["anchor"]) > 500:
        raise ConfidenceError("evidence anchor must contain 12-500 characters")
    if validate_source:
        blob = _blob_text(item["source_sha"], source_paths[item["source_id"]], source_blobs)
        record_text = _record_text(blob, item["source_id"])
        if item["anchor"] not in record_text:
            raise ConfidenceError(f"evidence anchor does not resolve in source blob: {item['id']}")
        if evidence_declaration(record, item) not in record_text:
            raise ConfidenceError(f"source record does not declare relationship evidence kind/outcome: {item['id']}")
    if item["kind"] == "owner_confirmation" and not item["source_id"].startswith(("CHAT-", "DEC-")):
        raise ConfidenceError("owner_confirmation requires a Chat or Decision source")
    _validate_date(item["observed_at"], "observed_at")
    if date.fromisoformat(item["observed_at"]) > datetime.now(ZoneInfo("Europe/London")).date():
        raise ConfidenceError("observed_at cannot be in the future")
    if item["state"] not in {"active", "resolved"}:
        raise ConfidenceError("evidence state must be active or resolved")
    if item["state"] == "resolved":
        if item["outcome"] != "contradicts" or not isinstance(item.get("resolution_ref"), str) or not item["resolution_ref"].strip():
            raise ConfidenceError("only contradictions may be resolved, with an evidence-id resolution_ref")
        if not EVIDENCE_ID_RE.fullmatch(item["resolution_ref"]):
            raise ConfidenceError("resolution_ref must be an evidence id")
    elif "resolution_ref" in item:
        raise ConfidenceError("active evidence must not contain resolution_ref")
    return item


def score_edge(record: dict, known_ids: set[str], source_paths: dict[str, str], source_blobs: dict[tuple[str, str], str] | None = None, trusted_evidence_ids: set[str] | None = None) -> EdgeScore:
    evidence = record.get("evidence")
    if not isinstance(evidence, list):
        raise ConfidenceError("edge evidence must be a list")
    trusted = trusted_evidence_ids or set()
    checked = [
        validate_evidence(
            item, record, known_ids, source_paths, source_blobs,
            validate_source=item.get("id") not in trusted,
        )
        for item in evidence
    ]
    ids = [item["id"] for item in checked]
    if len(ids) != len(set(ids)):
        raise ConfidenceError("duplicate evidence id")

    by_id = {item["id"]: item for item in checked}
    for item in checked:
        if item["state"] != "resolved":
            continue
        resolution = by_id.get(item["resolution_ref"])
        if (
            resolution is None or resolution["state"] != "active"
            or resolution["outcome"] != "supports"
            or resolution["kind"] not in {"owner_confirmation", "authoritative_record", "validated_outcome"}
            or resolution["sequence"] <= item["sequence"]
        ):
            raise ConfidenceError(f"contradiction resolution is not supported by qualifying later evidence: {item['id']}")

    # Only active evidence participates. One strongest item per canonical
    # source/outcome prevents a contributor inventing independence keys.
    collapsed: dict[tuple[str, str], dict] = {}
    for item in (value for value in checked if value["state"] == "active"):
        key = (item["source_id"], item["outcome"])
        prior = collapsed.get(key)
        if prior is None or SUPPORT_WEIGHTS[item["kind"]] > SUPPORT_WEIGHTS[prior["kind"]]:
            collapsed[key] = item

    active = list(collapsed.values())
    support = sorted(
        (item for item in active if item["outcome"] == "supports"),
        key=lambda item: (item["source_id"], item["id"]),
    )
    contradictions = sorted(
        (item for item in active if item["outcome"] == "contradicts"),
        key=lambda item: (item["source_id"], item["id"]),
    )
    score = LEGACY_BASELINE if record["disposition"] == "confirmed" else 0
    for item in support:
        score = _combine(score, SUPPORT_WEIGHTS[item["kind"]])
    for _item in contradictions:
        score = (score * (SCALE - CONTRADICTION_WEIGHT) + SCALE // 2) // SCALE

    status = "contested" if contradictions else record["disposition"]
    return EdgeScore(
        score=(score + 50) // 100,
        band="contested" if contradictions else _band(score),
        status=status,
        independent_evidence_count=len(active),
        supporting_evidence_count=len(support),
        contradicting_evidence_count=len(contradictions),
    )


def _reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ConfidenceError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_ledger(path: Path) -> dict:
    try:
        if path.stat().st_size > MAX_LEDGER_BYTES:
            raise ConfidenceError("relationship evidence ledger exceeds size limit")
        ledger = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise ConfidenceError(f"cannot read relationship evidence ledger: {exc}") from exc
    if not isinstance(ledger, dict):
        raise ConfidenceError("relationship evidence ledger root must be an object")
    return ledger


def parse_ledger_text(text: str) -> dict:
    try:
        ledger = json.loads(text, object_pairs_hook=_reject_duplicate_keys)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ConfidenceError(f"cannot parse prior relationship evidence ledger: {exc}") from exc
    if not isinstance(ledger, dict):
        raise ConfidenceError("prior relationship evidence ledger root must be an object")
    return ledger


def validate_append_only(current: dict, prior: dict) -> None:
    if prior.get("schema_version") != current.get("schema_version") or prior.get("scoring_model") != current.get("scoring_model"):
        raise ConfidenceError("ledger schema/scoring model changes require an explicit migration")
    current_edges = {item.get("edge_id"): item for item in current.get("edges", []) if isinstance(item, dict)}
    prior_items = {
        item.get("id"): item
        for edge in prior.get("edges", []) if isinstance(edge, dict)
        for item in edge.get("evidence", []) if isinstance(item, dict)
    }
    current_items = {
        item.get("id"): item
        for edge in current.get("edges", []) if isinstance(edge, dict)
        for item in edge.get("evidence", []) if isinstance(item, dict)
    }
    prior_max_sequence = max((item.get("sequence", 0) for item in prior_items.values()), default=0)
    for item in current_items.values():
        if item.get("id") not in prior_items and item.get("sequence", 0) <= prior_max_sequence:
            raise ConfidenceError(f"new evidence sequence must exceed prior history: {item.get('id')}")
        if item.get("state") == "resolved":
            old = prior_items.get(item.get("id"))
            resolution = current_items.get(item.get("resolution_ref"))
            if old is None or old.get("state") != "active" or item.get("resolution_ref") in prior_items or resolution is None:
                raise ConfidenceError(f"resolved contradiction requires a prior active event and new resolution evidence: {item.get('id')}")
    for old_edge in prior.get("edges", []):
        edge_id = old_edge.get("edge_id")
        new_edge = current_edges.get(edge_id)
        if new_edge is None:
            raise ConfidenceError(f"ledger edge history cannot be deleted: {edge_id}")
        for field in ("edge_id", "endpoints", "relationship_type", "direction"):
            if new_edge.get(field) != old_edge.get(field):
                raise ConfidenceError(f"immutable edge field changed: {edge_id}.{field}")
        allowed_transitions = {
            "candidate": {"candidate", "confirmed", "rejected"},
            "confirmed": {"confirmed"},
            "rejected": {"rejected"},
        }
        if new_edge.get("disposition") not in allowed_transitions.get(old_edge.get("disposition"), set()):
            raise ConfidenceError(f"invalid disposition transition: {edge_id}")
        new_evidence = {item.get("id"): item for item in new_edge.get("evidence", []) if isinstance(item, dict)}
        for old_item in old_edge.get("evidence", []):
            evidence_id = old_item.get("id")
            new_item = new_evidence.get(evidence_id)
            if new_item is None:
                raise ConfidenceError(f"evidence history cannot be deleted: {evidence_id}")
            if new_item == old_item:
                continue
            permitted = dict(old_item)
            if old_item.get("outcome") == "contradicts" and old_item.get("state") == "active":
                permitted["state"] = "resolved"
                permitted["resolution_ref"] = new_item.get("resolution_ref")
            if new_item != permitted:
                raise ConfidenceError(f"evidence history is immutable: {evidence_id}")


def evidence_ids_from_ledger(ledger: dict | None) -> set[str]:
    if not ledger:
        return set()
    return {
        item.get("id")
        for edge in ledger.get("edges", []) if isinstance(edge, dict)
        for item in edge.get("evidence", []) if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


def prior_ledger(ref: str) -> dict | None:
    verified = subprocess.run(
        ["git", "rev-parse", "--verify", f"{ref}^{{commit}}"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if verified.returncode != 0:
        raise ConfidenceError(f"base ref cannot be resolved: {ref}")
    exists = subprocess.run(
        ["git", "cat-file", "-e", f"{ref}:.github/relationship-evidence.json"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if exists.returncode != 0:
        return None
    result = subprocess.run(
        ["git", "show", f"{ref}:.github/relationship-evidence.json"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise ConfidenceError(f"base ledger exists but cannot be read: {ref}")
    return parse_ledger_text(result.stdout)


def load_ledger(path: Path = LEDGER_PATH, known_ids: set[str] | None = None, relationships: dict[str, list[str]] | None = None, source_paths: dict[str, str] | None = None, source_blobs: dict[tuple[str, str], str] | None = None, trusted_evidence_ids: set[str] | None = None) -> dict[str, tuple[dict, EdgeScore]]:
    ledger = read_ledger(path)
    if trusted_evidence_ids is None and source_blobs is None:
        try:
            trusted_evidence_ids = evidence_ids_from_ledger(prior_ledger("origin/main"))
        except ConfidenceError:
            trusted_evidence_ids = set()
    if ledger.get("schema_version") != 1 or ledger.get("scoring_model") != SCORING_MODEL:
        raise ConfidenceError("unsupported relationship evidence schema/scoring model")
    if set(ledger) != {"schema_version", "scoring_model", "edges"} or not isinstance(ledger["edges"], list):
        raise ConfidenceError("ledger must contain only schema_version, scoring_model, and edges")
    known = known_ids or set()
    result: dict[str, tuple[dict, EdgeScore]] = {}
    global_evidence_ids = set()
    global_sequences = set()
    for record in ledger["edges"]:
        if not isinstance(record, dict) or set(record) != {"edge_id", "endpoints", "relationship_type", "direction", "disposition", "evidence"}:
            raise ConfidenceError("edge has invalid fields")
        endpoints = record["endpoints"]
        if not isinstance(endpoints, list) or len(endpoints) != 2 or not all(isinstance(value, str) and ID_RE.fullmatch(value) for value in endpoints):
            raise ConfidenceError("edge endpoints must be two canonical IDs")
        if known and any(value not in known for value in endpoints):
            raise ConfidenceError(f"edge references unknown endpoint: {endpoints}")
        a, b, edge_id = canonical_edge(*endpoints)
        if endpoints != [a, b] or record["edge_id"] != edge_id:
            raise ConfidenceError(f"edge must use canonical order/key: {edge_id}")
        if edge_id in result:
            raise ConfidenceError(f"duplicate or reversed edge: {edge_id}")
        if record["relationship_type"] not in RELATIONSHIP_TYPES:
            raise ConfidenceError(f"unknown relationship type: {record['relationship_type']}")
        if record["relationship_type"] in UNDIRECTED_TYPES and record["direction"] != "undirected":
            raise ConfidenceError("undirected relationship type requires direction=undirected")
        if record["relationship_type"] in DIRECTED_TYPES and record["direction"] not in {"a_to_b", "b_to_a"}:
            raise ConfidenceError("directional relationship type requires a_to_b or b_to_a")
        chat_edge = a.startswith("CHAT-") or b.startswith("CHAT-")
        if chat_edge and record["relationship_type"] != "documents":
            raise ConfidenceError("Chat edge requires relationship_type=documents")
        if not chat_edge and record["relationship_type"] == "documents":
            raise ConfidenceError("relationship_type=documents requires a Chat endpoint")
        if record["disposition"] not in DISPOSITIONS:
            raise ConfidenceError(f"invalid disposition: {record['disposition']}")
        if relationships is not None:
            a_to_b = b in relationships.get(a, [])
            b_to_a = a in relationships.get(b, [])
            if chat_edge:
                if a_to_b and b_to_a:
                    raise ConfidenceError(f"directional Chat edge is reciprocal: {edge_id}")
                actual_direction = "a_to_b" if a_to_b else "b_to_a" if b_to_a else ""
                if record["disposition"] == "confirmed":
                    if not actual_direction:
                        raise ConfidenceError(f"confirmed Chat edge is absent from outbound provenance: {edge_id}")
                    if record["direction"] != actual_direction:
                        raise ConfidenceError(f"confirmed Chat edge direction does not match outbound provenance: {edge_id}")
                elif actual_direction:
                    raise ConfidenceError(f"{record['disposition']} edge must not appear in links: {edge_id}")
            else:
                reciprocal = a_to_b and b_to_a
                if record["disposition"] == "confirmed" and not reciprocal:
                    raise ConfidenceError(f"confirmed edge lacks reciprocal links: {edge_id}")
                if record["disposition"] != "confirmed" and reciprocal:
                    raise ConfidenceError(f"{record['disposition']} edge must not appear in links: {edge_id}")
        score = score_edge(record, known, source_paths or {}, source_blobs, trusted_evidence_ids)
        # A reciprocal direct relationship is a structural fact and is not
        # confidence-scored. Evidence remains useful for type, direction,
        # provenance and contradiction history, but is not an admission gate.
        for item in record["evidence"]:
            if item["id"] in global_evidence_ids:
                raise ConfidenceError(f"evidence id reused across edges: {item['id']}")
            if item["sequence"] in global_sequences:
                raise ConfidenceError(f"evidence sequence reused: {item['sequence']}")
            global_evidence_ids.add(item["id"])
            global_sequences.add(item["sequence"])
        result[edge_id] = (record, score)
    return result


def legacy_score() -> EdgeScore:
    return EdgeScore(40, "low", "legacy_unassessed", 0, 0, 0)


def collect_chat_data() -> tuple[dict[str, list[str]], dict[str, str]]:
    relationships = {}
    source_paths = {}
    for path in (REPO_ROOT / "Chats").glob("*.md"):
        text = path.read_text(errors="ignore")
        if is_support_document(path, text):
            continue
        for block in re.split(r"(?=^### CHAT-\d{4} — )", text, flags=re.M):
            match = re.match(r"^### (CHAT-\d{4}) —", block)
            if not match:
                continue
            link_match = re.search(r"^Links:\s*\[([^\]]*)\]", block, flags=re.M)
            relationships[match.group(1)] = LINK_ID_RE.findall(link_match.group(1)) if link_match else []
            source_paths[match.group(1)] = path.relative_to(REPO_ROOT).as_posix()
    return relationships, source_paths


def validate_repository(base_ref: str | None = None) -> int:
    sys.path.insert(0, str(SCRIPT_DIR))
    from library_scan import collect_entries, collect_native_artifact_entries
    entries = collect_entries()
    entries.update(collect_native_artifact_entries(entries))
    chat_relationships, chat_source_paths = collect_chat_data()
    known_ids = set(entries) | set(chat_relationships)
    source_paths = {
        entry_id: data["path"].relative_to(REPO_ROOT).as_posix()
        for entry_id, data in entries.items()
    }
    source_paths.update(chat_source_paths)
    relationships = {
        entry_id: data["fm"].get("links", []) if isinstance(data["fm"].get("links"), list) else []
        for entry_id, data in entries.items()
    }
    relationships.update(chat_relationships)
    try:
        previous = prior_ledger(base_ref) if base_ref is not None else None
        trusted_evidence_ids = evidence_ids_from_ledger(previous)
        attested_ref = os.environ.get("RELATIONSHIP_EVIDENCE_ATTESTED_REF", "").strip()
        if attested_ref:
            attested = prior_ledger(attested_ref)
            trusted_evidence_ids.update(evidence_ids_from_ledger(attested))
        scores = load_ledger(
            known_ids=known_ids, relationships=relationships, source_paths=source_paths,
            trusted_evidence_ids=trusted_evidence_ids,
        )
        if previous is not None:
            validate_append_only(read_ledger(LEDGER_PATH), previous)
    except ConfidenceError as exc:
        print(f"::error::Relationship confidence violation: {exc}")
        return 1
    print(f"Relationship confidence clean: {len(scores)} evidenced edges; scoring model {SCORING_MODEL}.")
    return 0


def main() -> int:
    base_ref = None
    if "--base-ref" in sys.argv:
        index = sys.argv.index("--base-ref")
        if index + 1 >= len(sys.argv):
            print("::error::--base-ref requires a git ref")
            return 2
        base_ref = sys.argv[index + 1]
    return validate_repository(base_ref)


if __name__ == "__main__":
    raise SystemExit(main())
