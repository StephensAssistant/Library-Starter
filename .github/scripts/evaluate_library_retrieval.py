#!/usr/bin/env python3
"""Evaluate exact/BM25 retrieval on development and held-out task fixtures."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import library_retrieval as retrieval  # noqa: E402

ROOT = SCRIPT_DIR.parents[1]
DEFAULT_FIXTURE = ROOT / ".github/evaluation/tick-0166-retrieval.json"


def reciprocal_rank(ids, relevant):
    for position, entry_id in enumerate(ids, 1):
        if entry_id in relevant:
            return 1.0 / position
    return 0.0


def evaluate(fixture, root=ROOT):
    cases = fixture["cases"]
    family_partitions = {}
    for case in cases:
        prior = family_partitions.setdefault(case["family"], case["partition"])
        if prior != case["partition"]:
            raise ValueError(f"family crosses partitions: {case['family']}")
    index = retrieval.build_index(root=root)
    ref_indexes = {}
    historical_refs = {}

    def index_for(case):
        opening_id = case.get("opening_id") or next(iter(case.get("essential", [])), None)
        path = index["documents"].get(opening_id, {}).get("path") if opening_id else None
        source_ref = None
        if path and (root / ".git").exists():
            proc = subprocess.run(
                ["git", "log", "--diff-filter=A", "--format=%H", "--reverse", "--", path],
                cwd=root, capture_output=True, text=True, check=True,
            )
            opening_commit = next((line for line in proc.stdout.splitlines() if line), None)
            if opening_commit:
                parent = subprocess.run(["git", "rev-parse", f"{opening_commit}^"], cwd=root,
                                        capture_output=True, text=True)
                source_ref = parent.stdout.strip() if parent.returncode == 0 else None
        key = source_ref or "current-fixture-fallback"
        if key not in ref_indexes:
            ref_indexes[key] = retrieval.build_index(root=root, git_ref=source_ref) if source_ref else index
        if source_ref and opening_id in ref_indexes[key]["documents"]:
            raise ValueError(f"{case['id']} opening ID is present in historical snapshot: {opening_id}")
        historical_refs[case["id"]] = key
        return ref_indexes[key]
    started = time.perf_counter()
    query_latency = 0.0
    rows = []
    for case in cases:
        case_index = index_for(case)
        labelled = set(case.get("essential", [])) | set(case.get("useful", []))
        missing_labels = sorted(labelled - set(case_index["documents"]))
        if missing_labels:
            raise ValueError(f"{case['id']} labels unavailable at opening: {', '.join(missing_labels)}")
        query_started = time.perf_counter()
        found = retrieval.rank(case_index, case["query"], limit=10, confirmed_depth=case.get("confirmed_depth", 1))
        query_latency += time.perf_counter() - query_started
        ids = [row["id"] for row in found]
        relevant = labelled
        if case.get("abstain"):
            passed = not found
        else:
            passed = bool(relevant & set(ids[:10]))
        rows.append({"id": case["id"], "partition": case["partition"], "top_ids": ids,
                     "abstain_case": bool(case.get("abstain")),
                     "recall_at_5": bool(relevant & set(ids[:5])), "recall_at_10": bool(relevant & set(ids[:10])),
                     "reciprocal_rank": reciprocal_rank(ids, relevant), "passed": passed})
    elapsed = (time.perf_counter() - started) * 1000
    metrics = {}
    for partition in ("development", "held_out"):
        subset = [row for row in rows if row["partition"] == partition]
        relevant_subset = [row for row in subset if not row["abstain_case"]]
        abstain_subset = [row for row in subset if row["abstain_case"]]
        metrics[partition] = {
            "cases": len(subset),
            "relevance_cases": len(relevant_subset),
            "abstention_cases": len(abstain_subset),
            "recall_at_5": round(sum(row["recall_at_5"] for row in relevant_subset) / max(len(relevant_subset), 1), 4),
            "recall_at_10": round(sum(row["recall_at_10"] for row in relevant_subset) / max(len(relevant_subset), 1), 4),
            "mrr_at_10": round(sum(row["reciprocal_rank"] for row in relevant_subset) / max(len(relevant_subset), 1), 4),
            "correct_abstention": round(sum(row["passed"] for row in abstain_subset) / max(len(abstain_subset), 1), 4),
            "pass_rate": round(sum(row["passed"] for row in subset) / max(len(subset), 1), 4),
        }
    return {"schema_version": 1, "fixture_revision": retrieval.revision(retrieval.canonical_json(fixture)),
            "design": "exact identifier + BM25 lexical/entity ranking + one-depth confirmed-link expansion",
            "budgets": {"candidate_pool": 10, "final_sources": 10, "confirmed_link_depth": 1,
                        "saved_suggestion_cap": 3, "external_models": 0},
            "metrics": metrics, "latency_ms_total": round(elapsed, 3),
            "query_latency_ms_total": round(query_latency * 1000, 3),
            "historical_build_ms": round(elapsed - query_latency * 1000, 3),
            "historical_family_refs": historical_refs,
            "rows": rows,
            "selection": "lexical baseline retained; no reviewed-label volume for learned challenger",
            "limitations": fixture.get("limitations", [])}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--minimum-held-out-recall", type=float, default=0.8)
    args = parser.parse_args(argv)
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    report = evaluate(fixture)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["metrics"]["held_out"]["recall_at_10"] >= args.minimum_held_out_recall else 1


if __name__ == "__main__":
    raise SystemExit(main())
