---
id: SKILL-0205
type: skill
title: Migration Divergence Localization
status: current
created: 2026-09-20
updated: 2026-10-24
trigger_phrases: ["locate earliest migration divergence", "trace SQL Server Snowflake variance boundary", "isolate first migration mismatch"]
links: []
tags: [skill, sql-server, snowflake, migration, reconciliation]
---

# Migration Divergence Localization

Find and explain the earliest material transformation boundary where SQL Server and Snowflake migration outputs diverge after a parity check identifies a variance.

## When to use

Use to localize an already-observed SQL Server-to-Snowflake migration variance at successive transformation boundaries. Use SKILL-0103 for the overall legacy-versus-replacement parity verdict and exception ledger.

## Intent-routing contract

This Skill owns earliest-boundary divergence localization only. Generic migration parity reconciliation and verdicts belong to SKILL-0103.

## Method

1. Start from the evidenced variance and aligned comparison cutoff, grain, keys and tolerances.
2. Compare row counts, distinct keys, unmatched populations, date range and material quantities or amounts at each transformation boundary.
3. Segment variance by date, entity, status or rule.
4. Locate the earliest boundary where divergence appears.
5. Distinguish timing or source-availability differences from logic defects.
6. Record tolerances and documented exceptions; never force equality without cause.

## Benchmark case

A known total variance is traced boundary by boundary, isolated to one load date and confirmed as source timing rather than rewritten away.

## Anti-patterns

- Replacing the overall parity reconciliation or verdict.
- Validating only grand totals.
- Changing logic before finding cause.
- Treating all differences as defects.

## Stop

Stop when the earliest material divergence is evidenced and explained or assigned for repair, or when the comparison contract is unresolved.

## Contextual links

- `SKILL-0031` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
