---
id: SKILL-0202
type: skill
title: Semantic SQL Dialect Translation
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["translate tsql to snowflake", "preserve sql semantics", "sql dialect migration"]
links: []
tags: [skill, sql-server, snowflake, sql, migration]
---

# Semantic SQL Dialect Translation

Translates SQL dialect while preserving business meaning.

## When to use

Use after the legacy contract is known and T-SQL logic must run in Snowflake.

## Method

1. Identify grain, null handling, date boundaries, status meanings and join semantics.
2. Translate syntax separately from semantic decisions.
3. Compare output shape and representative edge cases.
4. Reject compilable SQL that changes business behaviour.
5. Hand grain/key redesign to the relevant modelling Skill.

## Decision and evidence details

Retain source/target SQL versions, agreed grain/population, comparison cutoff and representative inputs/outputs. Check the boundary conditions identified in the source: nulls, inclusion/exclusion at dates, status branches and join population. Compilation remains syntax evidence only.

Boundary design case: both queries compile and totals agree, but a record exactly on the accepted date boundary is excluded in Snowflake. Keep translation unaccepted and correct the semantic difference rather than adjusting the expected result.

## Benchmark case

A T-SQL date predicate is rewritten in Snowflake and verified to retain the same inclusive boundary.

## Anti-patterns

- Mechanical syntax conversion
- Treating compilation as parity
- Changing grain during dialect translation

## Stop

Stop when semantic equivalence is evidenced or an unresolved rule blocks translation.

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
