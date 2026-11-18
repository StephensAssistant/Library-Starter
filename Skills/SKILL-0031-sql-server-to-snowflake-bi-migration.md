---
id: SKILL-0031
type: skill
title: BI Migration Contract and Completion Judgement
status: current
created: 2026-09-16
updated: 2026-10-24
links: []
tags: [skill, sql-server, snowflake, qlik, migration, completion]
trigger_phrases: ["judge migration completion", "remaining legacy dependency", "Snowflake migration complete"]
---

# BI Migration Contract and Completion Judgement

Defines the compatibility boundary and decides whether a legacy BI workload is truly Snowflake-native.

## When to use

Use when a Qlik or reporting workload has a known legacy contract and a proposed Snowflake replacement. Do not use for generic SQL syntax or new models without a legacy contract.

## Method

1. Confirm the legacy contract, authoritative source, target consumer and migration scope are identified.
2. Route contract capture, SQL translation, consumer interfaces, key migration, parity, Qlik blank diagnosis and end-to-end validation to their focused Skills.
3. Require evidence for legacy source/query, Snowflake replacement, grain/key map, row/key/measure comparisons, accepted exceptions, consumer checks, front-end verification and remaining dependencies.
4. Classify a Snowflake-hosted bridge still populated from SQL Server as temporary parity, not native completion.
5. Declare completion only when the authoritative upstream dependency is Snowflake-native or the remaining dependency is explicitly accepted by the authorised owner.
6. Stop on unresolved source authority, grain, business key, legacy contract or material parity variance.

## Benchmark case

A Qlik app reads a Snowflake table that is still fed by SQL Server: record temporary parity and the remaining dependency; do not declare the migration complete.

## Anti-patterns

- Declaring completion because the new query compiles
- Treating a Snowflake-hosted legacy bridge as native
- Omitting unresolved dependencies
- Accepting unexplained material variance
- Mixing implementation detail into the completion judgement

## Stop

Stop with an evidenced complete, temporary-parity or blocked judgement and the named remaining dependency or hand-off.

## Contextual links

- `SKILL-0201` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0202` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0203` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0204` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0205` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0206` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0207` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 7 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
