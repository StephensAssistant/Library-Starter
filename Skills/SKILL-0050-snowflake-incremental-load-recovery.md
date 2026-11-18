---
id: SKILL-0050
type: skill
title: Snowflake Incremental Load Recovery
status: current
created: 2026-09-20
updated: 2026-10-28
owner: Library owner

links: [SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0054, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0271]
tags: [skill, snowflake, incremental-load, recovery]
trigger_phrases: [snowflake incremental load, ingestion replay, pipeline backfill]
---

# Snowflake Incremental Load Recovery

Design and verify checkpoints, idempotency, replay, backfill and recovery for Snowflake ingestion.

## When to use

Use when a load must resume, rerun, replay a bounded window, backfill history or recover after partial failure.

## Method

1. Prove the authoritative checkpoint: source timestamp, increasing sequence, connector state, CDC position, file identity or API cursor.
2. Define batch grain, winning-record rule, unchanged-row behaviour and delete/cancel handling before MERGE.
3. Prove source-key uniqueness and make rerunning the same batch safe.
4. Separate delta, bounded replay and full/backfill modes with explicit scopes.
5. Reconcile rows, distinct keys, timestamps, duplicates, missing windows and material totals after recovery.

## Benchmark case

A failed load stopped after several API pages. A passing application resumes from a proven checkpoint or safely replays the bounded window, creates no duplicate governed rows and reconciles the recovered period.

## Anti-patterns

- Inventing a high watermark.
- MERGE before proving source-key uniqueness.
- Full rebuild without deterministic scope and reconciliation.
- Retrying an unchanged failure.

## Stop

Stop after the required recovery mode is repeatable and reconciled, or the precise checkpoint, grain or delete-semantics gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0050--SKILL-0266 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0050--SKILL-0267 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0050--SKILL-0268 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0050--SKILL-0269 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0050--SKILL-0270 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0050--SKILL-0271 | related_to | undirected | user_confirmed | supports

## Preservation-controlled recovery — 2026-10-11

Before repairing historical values, freeze the exact scope, source date field, source version, target receivers, and permitted columns or payload paths.

1. Enumerate current and history receivers before declaring missing data. Bind nested records to evidenced parent identity/version and child identity; reject ambiguous matches or conflicting source versions.
2. For absent-key enrichment, distinguish an absent key from an existing JSON null, empty value, or populated container. Preserve existing keys unless replacement is explicitly in scope.
3. Retain before images and verify both the requested value and every protected payload/column, key, and operating metadata value. Report distinct logical records separately from physical copies; repeated field enrichments are not additional recovered populations.
4. Require a committed receipt and resolved transaction state. A cancellation proves neither rollback nor success. Diagnose the retained failing statement before another repair; do not roll back unrelated session work.
5. After a correction to a recurring transformed target, repeat the read-only candidate/preservation check after the normal pipeline runs. Do not rerun accepted historical publications merely to reacquire confidence.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

Representative checks: add an absent native object while preserving an existing JSON-null key and all other fields; reject same-ID/version conflicts. A zero-candidate route reports no eligible enrichment, not existing-value parity. A cancelled run without a commit receipt remains inconclusive.

Stop with the committed scope/value/preservation receipt and repeat-run evidence where applicable, or the exact transaction, identity, source-version, or preservation gap. Recovery guidance grants no new execution authority.

## Sparse-delete and multi-table recovery lessons — 28 October 2026

Trigger: a retained live target has a later source tombstone, or a count-bound historical repair stops/times out. Prove actual key, flag type and order contract before borrowing another table's MERGE.

1. Inspect winner selection and freshness separately. A sparse delete may lack SYSROWVERSION but have a valid later VERSIONNUMBER; use that fallback for deletes only when evidenced. Prefer populated SYSROWVERSION, use strict greater-than, test mixed batches, and retain deletion markers when old live replay could resurrect a physically deleted target.
2. Distinguish retained source history from current-state targets and presentation filters. A NULL-flag live target may correctly pass INGESTED filtering while being wrongly retained upstream.
3. Treat assessment counts captured while writers run as provisional. Pause/drain writers/claims and recompute or strictly revalidate expected counts. Count drift with no review cases is new evidence, not permission to weaken the guard. Preserve original failed logs/backups and use an explicitly reviewed retry/new run.
4. Record expected/candidate/review, backup/current, busy, affected-row, after-count and remaining-key values before raising. Capture SQLROWCOUNT immediately; make DML and its committed receipt atomic. Keep post-commit refresh failures distinct. Drop task-owned temporary candidates on success/handled failure; retain recovery evidence.
5. A multi-table outer statement can time out after some child tables commit. Check warehouse plus session/account limits; the lower non-zero limit applies. Preserve verified subsets. After cancellation inspect durable state and close only the known repair transaction in its original session. Confirm no open transaction before DDL or changing AUTOCOMMIT.
6. Reuse an existing backup only for an explicitly diagnosed interrupted/no-commit table after verified identity/state. Never reset every failure or overwrite backup names. Skip verified tables, admit only supported recovery states and restore temporary warehouse settings with readback.
7. Test source VARCHAR versus typed STAGED timestamps appropriately. Parse text flags explicitly and reject unknown strings. The exercised WHSLOADLINE repair replaced a failing preflight SELECT/INTO form with RESULTSET iteration for GET_DDL and SELECT COUNT INTO FROM aggregation.
8. Refresh/reconcile presentation targets after commit and repeat the candidate assessment after ordinary ingestion. Keep downstream business/financial reconciliation separate from count and absent-key checks.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

## Contextual links

