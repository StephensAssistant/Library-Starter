#!/usr/bin/env python3
"""Validate the deterministic-first, cost-bounded model routing contract."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / ".github" / "model-routing.json"


def findings(data):
    rows = []
    if data.get("schema_version") != 1:
        rows.append("schema_version must be 1")
    if data.get("default_route") != "deterministic":
        rows.append("default_route must be deterministic")
    tiers = data.get("tiers", {})
    if set(tiers) != {"deterministic", "low_cost_model", "strong_model"}:
        rows.append("exactly three governed tiers are required")
    low = tiers.get("low_cost_model", {})
    strong = tiers.get("strong_model", {})
    if low.get("requires") != ["deterministic_not_applicable_or_failed"]:
        rows.append("low-cost route must follow deterministic non-applicability or failure")
    if low.get("max_attempts_per_operation") not in {1, 2}:
        rows.append("low-cost route must be capped at one or two attempts per operation")
    required = set(strong.get("requires", []))
    if required != {"low_cost_attempt_failed", "bounded_retry_exhausted", "material_task"}:
        rows.append("strong route must require failed bounded low-cost handling for a material task")
    if strong.get("max_attempts_per_operation") != 1:
        rows.append("strong route must be capped at one attempt per operation")
    if data.get("fallback_on_budget_exhaustion") != "blocked_human_review":
        rows.append("budget exhaustion must fail closed to human review")
    return rows


def main():
    try:
        data = json.loads(CONTRACT.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"MODEL ROUTING FAIL: {exc}", file=sys.stderr)
        return 1
    rows = findings(data)
    if rows:
        for row in rows:
            print(f"MODEL ROUTING FAIL: {row}", file=sys.stderr)
        return 1
    print("Model routing contract clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
