---
id: SKILL-0089
type: skill
title: Migration Parity Test Design
status: current
created: 2026-09-20
updated: 2026-10-23
links: [SKILL-0007]
tags: [testing, migration-parity]
trigger_phrases: ["design migration parity tests", "compare legacy and replacement systems", "test SQL Server to Snowflake migration"]
---

# SKILL-0089 — Migration Parity Test Design

## Purpose

Design parity evidence that preserves legacy business semantics while distinguishing legitimate source-time differences.

## When to use

Use for: design migration parity tests; compare legacy and replacement systems; test SQL Server to Snowflake migration.

## Method

1. Establish the legacy contract and aligned comparison cutoff.
2. Compare source populations and key/grain coverage before measures.
3. Compare segmented measures, dates, statuses and representative entities.
4. Verify aliases, outputs and consumer behaviour.
5. Classify differences as timing, source-state or logic before changing implementation.

## Benchmark case

For SQL Server-to-Snowflake migration, align reload cutoffs and compare keys and measures by store rather than forcing the newer source to equal an older snapshot.

## Anti-patterns

- Grand-total-only parity.
- Changing correct logic to match stale data.
- Ignoring consumer aliases.

## Stop

Stop with PASS/FAIL/INCONCLUSIVE parity and classified exceptions.


## Refresh-safe dynamic-table parity snapshots — 23 October 2026

**Owned outcome and inputs.** Design an exact comparison of a materialized Snowflake dynamic-table row bag and its expanded base-source query at a proved coordinated cutoff. Require the current definition, effective actor/access, base-table dependency expansion, time-travel availability, owner/grants contract and explicit rollback/acceptance authority from the calling work. This technique grants no refresh, replacement, source mutation or schedule authority.

**Required method.** Read the table's DATA_TIMESTAMP, capture a physical materialization time with CURRENT_TIMESTAMP, and immediately read DATA_TIMESTAMP again before the expensive comparison. Accept the capture only when those two metadata reads agree. Pin the actual table with AT (TIMESTAMP => captured physical time) and all expanded base tables at the agreed DATA_TIMESTAMP. Then compare full row bags, including multiplicity, against these immutable inputs. An automatic refresh after the captured physical instant does not change either time-travel input; report the newer observed timestamp as context rather than rejecting the already-pinned comparison. Recheck owner/grants/definitions as required by the caller. Never confuse the base data timestamp with the physical materialization/commit time of an upstream dynamic table.

**Failure and bounds.** If metadata moves across the capture interval, discard that capture and retry only with the newly observed input timestamps, at most three capture attempts for this method. If no stable interval is obtained, return an explicit inconclusive snapshot gap. Missing metadata, unsupported retention or changed definitions/access block their dependent test; do not invent a cutoff or a PASS. Exact missing/extra row occurrences remain real failures even when a later refresh also occurs. Restore only the authorised affected object through the caller's guarded rollback; never widen a repair or suspend/change schedules merely to make a test pass.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

**Anti-pattern.** Treating a normal refresh observed after a fixed time-travel comparison started as evidence that the comparison's immutable inputs moved.


## Native definition guards across pasted exports — 23 October 2026

**Trigger and inputs.** A migration preflight rejects a deployed DDL/query against a definition carried through Markdown or chat. Establish the native source, comparison scope, current owner/grants and the exact rejected representation before changing a guard. A definition mismatch is not yet proof of business-data divergence or a semantic source change.

**Method.** Compare the complete native query and expected query using documented normalization, preserving SQL literals and comments. Obtain native lengths/hashes and bounded difference contexts. Where the export has flattened comment line breaks, transform only freshly captured native newline-preserving DDL, never the flattened export. Distinguish DDL header representation from query text, and keep owner, grants, column order/types and exact current-definition checks at their separate boundaries. Correct only transport escapes proved by the native difference. Verify the corrected complete query against the returned native hash/length before retrying. Do not apply indiscriminate backslash removal: SQL string/regex escapes can be legitimate.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.
