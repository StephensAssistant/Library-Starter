---
id: SKILL-0203
type: skill
title: BI Consumer Contract Preservation
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["preserve qlik contract", "retain qvd interface", "migration field aliases"]
links: []
tags: [skill, qlik, snowflake, migration, interfaces]
---

# BI Consumer Contract Preservation

Preserves downstream BI field, file and load contracts during source replacement.

## When to use

Use when a migrated source feeds an existing Qlik app or report interface.

## Method

1. Inventory exposed aliases, QVD/file names, field casing, `NoConcatenate`, resident loads and composite keys.
2. Preserve each contract through explicit aliases/preloads where practical.
3. If a contract must change, identify and update every consumer together.
4. Verify the consumer sees the expected interface before presentation testing.

## Decision and evidence details

Return a producer-to-consumer contract map with exact field casing, aliases, stored outputs and load/association expectations. Compare the actual consumer-visible interface before and after replacement; source-query equivalence alone does not cover resident loads or published files.

Boundary design case: a requested rename has an unverified downstream consumer. Preserve the established interface and report the migration gap until coordinated scope and consumer verification exist; do not assume visual testing will find it.

## Benchmark case

A Snowflake preload retains the uppercase aliases and QVD name expected by the unchanged Qlik front end.

## Anti-patterns

- Accidental renaming
- Changing producer without consumers
- Ignoring load-script association contracts

## Stop

Stop when the downstream interface is unchanged or an authorised coordinated change is complete.

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
