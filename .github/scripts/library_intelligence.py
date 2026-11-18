#!/usr/bin/env python3
"""Generate deterministic Library health metrics, alerts, and recommendations."""
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from library_scan import collect_entries  # noqa: E402

ROOT = SCRIPT_DIR.parents[1]
OUT = ROOT / "Catalog" / "SYSTEM-HEALTH.json"
LEGACY_PLANNING_BASELINE = ROOT / ".github" / "planning-legacy-baseline.json"
PLAN_ID_RE = re.compile(r"^(PROJ|TICK)-(\d{4})\.md$")
DATE_RE = re.compile(r"^Last meaningful update:\s*(\d{4}-\d{2}-\d{2})\s*$", re.M)
OPEN_RE = re.compile(r"(?m)^\s*- \[ \]")


def pct(n, d):
    return round((100.0 * n / d), 1) if d else 100.0


def parse_day(value):
    if not value or value in {"null", "None"}:
        return None
    try:
        return datetime.strptime(str(value)[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def utc_today(now=None):
    """Return the calendar date at UTC, independent of the runner's local TZ."""
    return (now or datetime.now(timezone.utc)).astimezone(timezone.utc).date()


def load_legacy_planning_baseline():
    if not LEGACY_PLANNING_BASELINE.exists():
        return set()
    try:
        data = json.loads(LEGACY_PLANNING_BASELINE.read_text())
        ids = data.get("ids", []) if isinstance(data, dict) else []
        return {str(item) for item in ids if isinstance(item, str)}
    except (ValueError, OSError):
        return set()


def relationship_metrics(entries):
    unique = set()
    linked_records = 0
    for entry_id, data in entries.items():
        links = data["fm"].get("links", [])
        if not isinstance(links, list):
            continue
        if links:
            linked_records += 1
        for target in links:
            if target in entries and target != entry_id:
                unique.add(tuple(sorted((entry_id, target))))
    ledger_path = ROOT / ".github" / "relationship-evidence.json"
    assessed = 0
    if ledger_path.exists():
        try:
            ledger = json.loads(ledger_path.read_text())
            rows = ledger.get("edges", ledger.get("relationships", ledger if isinstance(ledger, list) else []))
            if isinstance(rows, list):
                assessed = len(rows)
        except (ValueError, OSError):
            assessed = 0
    inferred_entities = inferred_records = inferred_connections = corpus_files = 0
    inferred_path = ROOT / ".github" / "relationship-candidates.json"
    if inferred_path.exists():
        try:
            inferred = json.loads(inferred_path.read_text())
            postings = inferred.get("entity_index", {})
            inferred_entities = len(postings)
            inferred_records = len(inferred.get("records", {}))
            inferred_connections = sum(len(set(ids)) for ids in postings.values())
            corpus_files = len(inferred.get("corpus_manifest", {}))
        except (ValueError, OSError, AttributeError):
            pass
    return {
        "direct_relationships": len(unique),
        "unique_links": len(unique),
        "records_with_links": linked_records,
        "records_with_links_pct": pct(linked_records, len(entries)),
        "direct_relationship_provenance_records": assessed,
        "assessed_relationships": assessed,
        "assessed_relationship_pct": pct(min(assessed, len(unique)), len(unique)),
        "inferred_entities": inferred_entities,
        "inferred_entity_memberships": inferred_connections,
        "inferred_records": inferred_records,
        "relationship_corpus_files": corpus_files,
    }


def collect_health(today=None):
    today = today or utc_today()
    entries = collect_entries()
    work = {k: v for k, v in entries.items() if k.startswith(("PROJ-", "TICK-"))}
    active = {
        k: v for k, v in work.items()
        if str(v["fm"].get("work_state", "")).lower() not in {"done"}
        and str(v["fm"].get("status", "")).lower() not in {"done", "closed", "archived", "superseded"}
    }
    plans = {}
    stale_plans = []
    open_plan_items = 0
    planning = ROOT / "Planning"
    if planning.exists():
        for path in sorted(planning.glob("*.md")):
            m = PLAN_ID_RE.match(path.name)
            if not m:
                continue
            parent = f"{m.group(1)}-{m.group(2)}"
            text = path.read_text(errors="ignore")
            plans[parent] = path
            open_plan_items += len(OPEN_RE.findall(text))
            dm = DATE_RE.search(text)
            if dm:
                changed = parse_day(dm.group(1))
                if changed and (today - changed).days > 7 and parent in active:
                    stale_plans.append(parent)

    inline_plans = set()
    for parent_id, entry in active.items():
        text = Path(entry["path"]).read_text(errors="ignore")
        section = re.search(r"(?ms)^## Work plan\s*\n(.*?)(?=^## |\Z)", text)
        if section and re.search(r"(?m)^- \[[ xX]\] \S", section.group(1)):
            inline_plans.add(parent_id)
    all_missing_plans = sorted(set(active) - set(plans) - inline_plans)
    legacy_baseline = load_legacy_planning_baseline()
    legacy_unplanned = sorted(set(all_missing_plans) & legacy_baseline)
    missing_plans = sorted(set(all_missing_plans) - legacy_baseline)

    no_next = sorted(
        k for k, v in active.items()
        if str(v["fm"].get("next_action", "")).strip().lower() in {"", "null", "none"}
    )
    waiting_invalid = sorted(
        k for k, v in active.items()
        if str(v["fm"].get("work_state", "")).lower() == "waiting"
        and (str(v["fm"].get("waiting_on", "")).strip().lower() in {"", "null", "none"}
             or str(v["fm"].get("review_on", "")).strip().lower() in {"", "null", "none"})
    )
    overdue = []
    for k, v in active.items():
        due = parse_day(v["fm"].get("due"))
        if due and due < today:
            overdue.append(k)
    doing_ids = sorted(k for k, v in active.items() if str(v["fm"].get("work_state", "")).lower() == "doing")
    review_ids = sorted(k for k, v in active.items() if str(v["fm"].get("work_state", "")).lower() == "review")
    doing = len(doing_ids)
    review = len(review_ids)
    rel = relationship_metrics(entries)
    planning_applicable = len(active) - len(legacy_unplanned)
    plan_rate = pct(planning_applicable - len(missing_plans), planning_applicable)
    hygiene_good = len(active) - len(set(no_next) | set(waiting_invalid))
    hygiene_rate = pct(hygiene_good, len(active))
    wip_score = 100.0 if doing <= 30 and review <= 2 else max(0.0, 100.0 - (max(0, doing - 30) * 5 + max(0, review - 2) * 15))
    # Operational health measures enforced cleanliness and recovery controls.
    # Relationship assessment coverage remains visible as a maturity diagnostic:
    # raising it requires qualifying evidence and must never be incentivised by a
    # health score that can only be improved by inventing evidence.
    health_weights = {
        "planning_coverage_pct": 25,
        "work_hygiene_pct": 20,
        "wip_compliance_pct": 10,
    }
    health_components = {
        "planning_coverage_pct": plan_rate,
        "work_hygiene_pct": hygiene_rate,
        "wip_compliance_pct": wip_score,
    }
    weight_total = sum(health_weights.values())
    score = round(
        sum(health_components[name] * weight for name, weight in health_weights.items())
        / weight_total,
        1,
    )
    alerts = []
    if missing_plans:
        alerts.append({"severity": "high", "code": "planning-coverage", "count": len(missing_plans), "message": "Active work has neither an inline checklist nor a linked plan."})
    if stale_plans:
        alerts.append({"severity": "medium", "code": "stale-plans", "count": len(stale_plans), "message": "Active plans have not had a meaningful update for more than 7 days."})
    if no_next:
        alerts.append({"severity": "high", "code": "missing-next-action", "count": len(no_next), "message": "Active work items have no canonical next action."})
    if waiting_invalid:
        alerts.append({"severity": "high", "code": "waiting-hygiene", "count": len(waiting_invalid), "message": "Waiting items are missing waiting_on or review_on."})
    if overdue:
        alerts.append({"severity": "medium", "code": "overdue", "count": len(overdue), "message": "Active work has a confirmed due date in the past."})
    if doing > 30 or review > 2:
        alerts.append({"severity": "high", "code": "wip-limit", "count": max(doing - 30, 0) + max(review - 2, 0), "message": "Work-in-progress limits are exceeded."})
    recs = []
    mapping = {
        "planning-coverage": "For the requested work, add an inline checklist or use a linked plan when substantial detail is needed.",
        "stale-plans": "On resumption, reconcile only a stale claim that affects the next action.",
        "missing-next-action": "Restore one verb-led canonical next_action on each affected parent.",
        "waiting-hygiene": "Add exact waiting_on and review_on values, or move the item out of Waiting.",
        "overdue": "Review overdue commitments; do not silently move dates without evidence.",
        "wip-limit": "Finish, pause, block or review-complete work before starting more WIP.",
    }
    for a in alerts:
        recs.append({"code": a["code"], "action": mapping[a["code"]]})
    return {
        "schema_version": 3,
        "generated_on": today.isoformat(),
        "health_score": score,
        "health_score_basis": {
            "kind": "operational_integrity",
            "weights": health_weights,
            "weight_total": weight_total,
            "excluded_diagnostics": ["assessed_relationship_pct", "inferred_entity_memberships"],
            "note": "Inferred discovery coverage is reported separately and never affects operational health.",
        },
        "metrics": {
            "entries": len(entries),
            "active_work": len(active),
            "planning_coverage_pct": plan_rate,
            "planning_applicable_active": planning_applicable,
            "missing_plans": len(missing_plans),
            "legacy_unplanned_active": len(legacy_unplanned),
            "stale_plans": len(stale_plans),
            "open_plan_items": open_plan_items,
            "work_hygiene_pct": hygiene_rate,
            "missing_next_actions": len(no_next),
            "invalid_waiting_items": len(waiting_invalid),
            "overdue_items": len(overdue),
            "doing_wip": doing,
            "review_wip": review,
            "wip_compliance_pct": wip_score,
            **rel,
        },
        "details": {
            "missing_plan_ids": missing_plans,
            "stale_plan_ids": stale_plans,
            "missing_next_action_ids": no_next,
            "invalid_waiting_ids": waiting_invalid,
            "overdue_ids": sorted(overdue),
            "doing_ids": doing_ids,
            "review_ids": review_ids,
        },
        "transition_backlog": {
            "legacy_unplanned_ids": legacy_unplanned,
            "note": "Historical records are preserved. On material resumption, use an inline checklist or a linked plan."
        },
        "alerts": alerts,
        "recommendations": recs,
    }


def main():
    data = collect_health()
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    previous = OUT.read_text() if OUT.exists() else ""
    if previous != rendered:
        OUT.write_text(rendered)
    print(f"Library health: {data['health_score']}%; {len(data['alerts'])} alert(s).")
    import os
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as handle:
            handle.write(f"changed={'true' if previous != rendered else 'false'}\n")
            handle.write(f"health_score={data['health_score']}\n")


if __name__ == "__main__":
    main()
