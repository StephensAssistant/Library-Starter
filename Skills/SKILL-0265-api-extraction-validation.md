---
id: SKILL-0265
type: skill
title: API Extraction Validation
status: current
created: 2026-09-20
updated: 2026-10-11
owner: Library owner

links: [SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0054, SKILL-0056, SKILL-0057, SKILL-0058]
tags: [skill, api, extraction-validation, reconciliation]
trigger_phrases: ["validate an API extraction", "prove API population completeness", "reconcile extracted API records"]
---

# SKILL-0265 — API Extraction Validation

## Purpose

Prove that an API or GraphQL extraction is complete, unique, structurally intact and replay-safe against authoritative source evidence.

## When to use

Use after paginated or bulk extraction returns data and an independent correctness verdict is required. Do not own transport traversal, bulk-job control or watermark advancement.

## Method

1. Confirm extraction scope, grain, stable IDs, requested window and expected source controls.
2. Compare source-declared totals or representative source queries with extracted rows and distinct stable IDs.
3. Test duplicates, missing IDs, pagination or result-part coverage, child-parent integrity and null critical keys.
4. Verify update and delete handling for the covered window.
5. Replay a representative page, part or window and prove idempotent results.
6. Classify variances as scope, timing, source-state, extraction defect or validation gap.
7. Return PASS, FAIL or INCONCLUSIVE with direct evidence and residual risk.

## Benchmark case

A completed GraphQL extract contains roots and child objects across several pages. A passing validation reconciles source counts, proves every page and child-parent relationship, finds no duplicate stable IDs and shows an identical result after replay.

## Anti-patterns

- Treating HTTP or terminal-operation success as data correctness.
- Validating grand totals without stable IDs or child integrity.
- Ignoring update and delete behaviour.
- Calling timing variance an extraction defect without aligned source evidence.
- Advancing a checkpoint from an inconclusive verdict.

## Stop

Stop with an evidence-backed PASS, FAIL or INCONCLUSIVE verdict and exact exception population; hand transport or checkpoint defects to their owning Skills.

## Field and history parity claims — 2026-10-11

When comparing an API replacement with a retained connector, keep extraction completeness, structural coverage, historical enrichment, existing-value equality, and downstream consumer parity as separate verdicts.

1. Align scope and capture cutoff; compare stable IDs at each actual grain before interpreting count differences.
2. Inspect root and child containers, requested field shapes, native types, parent/version bindings, and exact receiver schemas. A matching root count does not prove nested content.
3. Distinguish source absence, optional empty branches, missing target keys, version mismatch, and wrong existing values. Confirm a residual requirement before requesting more source history.
4. Verify positive child/terminal-publication cases independently of empty pilots and schema installation. Report checks not exercised.
5. After absent-key enrichment, verify value and full-record preservation. A zero-candidate result does not establish equality inside existing objects/arrays or consumer readiness.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

Representative checks: equal root IDs with a truncated child array must not pass full parity; an absent-key publication with no candidates must not pass existing-value parity. Different capture times remain classified timing evidence until an aligned comparison exists.

Stop with separate scoped verdicts and exact residual populations. Do not infer cutover or connector-retirement authority.
