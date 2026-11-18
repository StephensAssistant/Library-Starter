---
id: SKILL-0088
type: skill
title: Data Pipeline Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [testing, data-pipeline]
trigger_phrases: ["design data pipeline tests", "test ingestion and transformations", "test replay and backfill"]
---

# SKILL-0088 — Data Pipeline Test Design

## Purpose

Design tests for data movement and transformation at the earliest changed boundary through affected consumers.

## When to use

Use for: design data pipeline tests; test ingestion and transformations; test replay and backfill.

## Method

1. Define grain, keys, schema, expected population, date range and material measures.
2. Test types, required fields, counts, keys, nulls, duplicates, freshness and source availability.
3. Prove join cardinality, fan-out, transformations and referential integrity.
4. Test idempotency, replay, retry, backfill or rebuild where supported.
5. Reconcile affected downstream outputs.

## Benchmark case

For an incremental load change, test watermark boundaries, rerun idempotency, late records, duplicates and final consumer totals.

Missing-input design case: an incremental test has no authoritative expected watermark or delete semantics. Identify the dependent cases as blocked and seek the actual contract; do not guess a checkpoint or call a rerun safe from final-table row counts alone.

## Anti-patterns

- Testing only the final table.
- Relying on one grand total.
- Backfilling without idempotency evidence.

## Stop

Stop with boundary-to-consumer cases and expected evidence.
