#!/usr/bin/env python3
"""Build the versioned retrieval index, advisory suggestions and evaluation."""
import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import evaluate_library_retrieval as evaluator  # noqa: E402
import library_retrieval as retrieval  # noqa: E402

ROOT = SCRIPT_DIR.parents[1]
INDEX = ROOT / ".github/retrieval-index.json"
SUGGESTIONS = ROOT / ".github/relationship-suggestions.json"
RESULTS = ROOT / ".github/evaluation/tick-0166-results.json"


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evaluate", action="store_true")
    args = parser.parse_args(argv)
    prior = load(INDEX)
    prior_advisory = load(SUGGESTIONS)
    index = retrieval.build_index(prior=prior)
    changed = retrieval.write_if_changed(INDEX, index, compact=True)
    advisory = retrieval.update_suggestions(index, prior, prior_advisory, cap=3, minimum=2.0)
    changed = retrieval.write_if_changed(SUGGESTIONS, advisory, compact=True) or changed
    if args.evaluate:
        fixture = json.loads(evaluator.DEFAULT_FIXTURE.read_text(encoding="utf-8"))
        report = evaluator.evaluate(fixture)
        if report["metrics"]["held_out"]["recall_at_10"] < 0.8:
            raise ValueError("held-out retrieval recall is below 0.8")
        for field in ("latency_ms_total", "query_latency_ms_total", "historical_build_ms"):
            report.pop(field, None)
        changed = retrieval.write_if_changed(RESULTS, report) or changed
    print(retrieval.canonical_json({"changed": changed, "corpus_hash": index["corpus_hash"],
                                    "changed_or_deleted": retrieval.changed_ids(index, prior),
                                    "documents": len(index["documents"]),
                                    "advisory_records": len(advisory["records"]),
                                    "evaluated": args.evaluate}))


if __name__ == "__main__":
    raise SystemExit(main())
