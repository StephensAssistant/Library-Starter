---
id: SKILL-0101
type: skill
title: Analytical SQL Performance Optimisation
status: current
created: 2026-09-20
updated: 2026-10-05
links: []
tags: [data-modelling, sql-performance]
trigger_phrases: ["optimise analytical SQL", "reduce warehouse query cost", "improve report query performance"]
---

# SKILL-0101 — Analytical SQL Performance Optimisation

## Purpose

Improve analytical SQL performance using representative workload evidence while preserving output semantics.

## When to use

Use for: optimise analytical SQL; reduce warehouse query cost; improve report query performance.

## Method

1. Capture query profile, history, filters, volume, latency and compute baseline.
2. Identify repeated work, pruning failures, fan-out, unnecessary columns/rows and expensive operators.
3. Apply the smallest semantic-preserving change.
4. Re-run comparable workload and reconcile outputs.
5. Report latency, compute and operational tradeoffs.

## Benchmark case

Optimise a repeated reporting query by pruning early and materialising only proven reused work, then compare identical filters and reconcile results.

## Anti-patterns

- Tuning without a baseline.
- Changing grain to gain speed.
- Reporting a cost percentage from incomparable runs.

## Stop

Stop with before/after evidence, parity result and residual bottleneck.


## Historical VARIANT enrichment diagnostic boundary — 4 October 2026

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

- Inspect actual longest-running child statement/query history/profile before another revision after an unsuccessful tuning attempt. Separate queuing, blocking, source staging, join fan-out, writes and verification; total duration cannot identify which occurred.
- ID-only joins between retained source and target versions can multiply the population before GROUP BY. Define and inspect both grains. Deduplicate source IDs for presence checks and use a unique ID/version relation for exact-version joins. Preserve physical receiver duplicates and source conflicts rather than silently changing grain.
- Consider staging genuinely reused scope once and retaining full VARIANT payload only for eligible candidates; use compact scalar ID/version joins plus old-payload/metadata compare-and-set guards. Skip mutation/verification branches for routes with zero candidates.
- These are candidate techniques, not proof of an improvement. In this example all were present in the second cancelled revision; the remaining bottleneck is unresolved. Do not recommend another rerun, larger warehouse or cost/duration estimate without evidence and authority.
- Obtain comparable completed workload and value/preservation results before claiming optimisation. Keep previously accepted field publications intact; a cancelled run does not authorise rebuilding them.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

## Anonymous-block child-history diagnosis and recoverable publications — 5 October 2026

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

- Obtain actual child history, full SQL and elapsed/execution/compile/provisioning/overload/transaction-blocking times. For recent history, use the documented, fully qualified INFORMATION_SCHEMA.QUERY_HISTORY_BY_SESSION with exact SESSION_ID, explicit time boundaries, RESULT_LIMIT 10000 and INCLUDE_CLIENT_GENERATED_STATEMENT TRUE. Apply the function's documented output contract; ROWS_INSERTED on UPDATE is not affected-update evidence. Retain the DML result if update counts are required.
- The outer SYSTEM$ANONYMOUS_BLOCK node and its 97.2% network time did not isolate a source/network issue. Actual child history showed source CTAS 3.51s, scope CTAS 105.81s, stage CTAS 179.90s/4,352,838 staged rows, current UPDATE 48.55s, HISTORY UPDATE 348.28s and HISTORY_2 UPDATE 556.04s on X-Small, with zero recorded provisioning/overload/blocking time. HISTORY_3 was cancelled after 111.29s. Known bottleneck location: receiver writes. Join spill/operator cause and useful warehouse resizing remain unproven; do not claim them.
- Child UPDATE SUCCESS is statement completion, not publication COMMIT. These blocks had not reached validation/COMMIT; supplied history did not show subsequent explicit rollback/commit. Cancellation state must remain uncertain until verified.
- Where independently valid receiver publications are authorised, one receiver per independently validated transaction preserves committed progress if a later receiver fails/cancels. Retain fixed source scope, source conflict rejection, version/ID binding, absent-key preservation, old-payload/metadata guards, and full value/preservation validation. Compare affected/verified physical rows to expected physical candidate count so skipped CAS rows cannot produce a false complete receipt. Report receiver-local coverage distinctly from global coverage.
- This is a recoverability technique, not automatic performance improvement. Revised candidate is pending runtime acceptance; no new permanent machinery, schedules, API recovery or larger warehouse was authorised. Reuse previously accepted field publications.

Current representative verification: persisted revision 3 contains four isolated receiver blocks; static/manual review confirms guard/validation before each receiver COMMIT. Completed Snowflake receipts and comparable runtime results remain pending. Authority boundary: do not auto-rollback unrelated session work, alter existing keys/versions, invent metadata fields, or describe pending candidate behaviour as deployed success.
