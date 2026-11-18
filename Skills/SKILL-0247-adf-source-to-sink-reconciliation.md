---
id: SKILL-0247
type: skill
title: ADF Source-to-Sink Reconciliation
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["validate ADF load", "ADF source sink parity", "ADF freshness check"]
---

# ADF Source-to-Sink Reconciliation

Reusable capability for proving that ADF moved the expected data and met freshness.

## When to use

Use only when the requested action is proving that ADF moved the expected data and met freshness. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact run, expected source files/window, source and sink grain/keys, aligned observation cutoff and agreed freshness requirement.
2. Compare expected files, rows, windows, business keys, late/missing data and downstream availability.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return expected/observed files, rows, keys and downstream availability with missing/extra/late populations and scoped freshness findings; distinguish timing differences from proven transfer defects.

## Benchmark case

A successful activity is accepted only after its expected file and business-date rows appear in Snowflake.

Boundary design case: Source and sink counts were taken at different cutoffs while new data arrived. Classify the discrepancy as unresolved timing evidence and align the comparison before claiming a missing load.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0036` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
