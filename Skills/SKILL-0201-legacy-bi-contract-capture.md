---
id: SKILL-0201
type: skill
title: Legacy BI Contract Capture
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["capture legacy report contract", "document qlik source contract", "migration contract inventory"]
links: []
tags: [skill, sql-server, snowflake, migration, contracts]
---

# Legacy BI Contract Capture

Captures the existing reporting contract before replacement work begins.

## When to use

Use when a SQL Server, QVD or bridge-backed BI workload is being migrated to Snowflake.

## Method

1. Record original SQL/Qlik logic and authoritative sources.
2. Capture output fields, aliases, QVD/file names, measures, filters, calendars and status rules.
3. Record downstream consumers and assumptions.
4. Separate verified contract facts from unresolved behaviour.
5. Preserve constraints, negations, units, dates and exceptions exactly.

## Decision and evidence details

Bind each captured rule/interface to its source revision and consumer, preserving exact output literals and known exceptions. Deliver a contract inventory that distinguishes observed behaviour, accepted requirements and unresolved assumptions before replacement work.

Boundary design case: the source query is available but a dependent app's definitions are not. Capture the verified source contract and mark consumer coverage incomplete; do not label apparently unused fields safe to remove.

## Benchmark case

Before converting a Qlik load, document its aliases, composite key, date filters and QVD output name.

## Anti-patterns

- Translating before reading the legacy logic
- Assuming unused-looking fields have no consumers
- Summarising away exceptions

## Stop

Stop when the legacy consumer contract is explicit or unresolved elements are raised.

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
