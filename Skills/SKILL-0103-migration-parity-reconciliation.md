---
id: SKILL-0103
type: skill
title: Migration Parity Reconciliation
status: current
created: 2026-09-20
updated: 2026-10-13
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047]
tags: [data-quality, migration-parity]
trigger_phrases: ["reconcile a data migration", "compare legacy and new platform results", "validate migration parity"]
---

# SKILL-0103 — Migration Parity Reconciliation

## Purpose

Reconcile legacy and replacement data across population, allocation and measures while accounting for source-state timing.

## When to use

Use for: reconcile a data migration; compare legacy and new platform results; validate migration parity.

## Method

1. Align comparison cutoff, grain, keys, calendars, currency and tolerances.
2. Compare rows, distinct business keys, date coverage and status populations.
3. Compare material measures by meaningful segment and representative entity.
4. Quantify join coverage, orphans and duplicates.
5. Classify every variance as timing/source-state, legitimate scope or logic defect.

## Benchmark case

Compare SQL Server and Snowflake sales at one aligned cutoff by store and date, explaining advanced source records rather than forcing exact stale-snapshot equality.

## Anti-patterns

- Grand-total-only comparison.
- Forcing equality across different capture times.
- Ignoring allocation differences when totals match.

## Stop

Stop with a parity verdict and classified exception ledger.


## Live comparison and bounded acceptance — Killingworth, 13 October 2026

A fixed reporting/age clock does not freeze independently updating source tables. Generate summary and detail from one result/statement where possible; separate live reads can disagree internally. Validate totals from the exported detail and retain actual capture times. Align completed app reloads, selections and KPI definitions; identical displayed minute does not prove identical source snapshots.

When the Library owner explicitly sets native-source correctness/conservation as the acceptance criterion, use legacy variance diagnostically rather than repeatedly forcing identical stale totals. Prove relevant source coverage, join cardinality, key/grain and quantity/value conservation; retain missing-source exceptions and independent acceptance separately. More replacement rows alone never proves correctness; healthy processing cursors never prove complete exports.
