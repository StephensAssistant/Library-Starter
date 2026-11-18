---
id: SKILL-0207
type: skill
title: Backend-to-Frontend Migration Validation
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["validate migrated qlik app", "backend parity before visual check", "migration front end validation"]
links: []
tags: [skill, qlik, snowflake, migration, validation]
---

# Backend-to-Frontend Migration Validation

Validates a migrated workload from backend parity through unchanged front-end behaviour.

## When to use

Use after source and transformation parity are established for a Qlik/reporting migration.

## Method

1. Verify authoritative source populations and material measures first.
2. Test Qlik selections, expressions, blanks/nulls and visuals second.
3. Confirm expected front-end field names and associations.
4. Record remaining presentation defects separately from backend defects.
5. Do not declare success while backend parity is unresolved.

## Decision and evidence details

Retain the migrated app/revision, authoritative backend comparison/cutoff and tested selection/expression/visual states. Map each front-end check to the unchanged consumer contract and keep backend, association, expression and presentation findings distinguishable.

Boundary design case: backend totals reconcile but one required selection produces blanks. Keep end-to-end acceptance open and route that failed boundary; a successful reload or a matching default-view screenshot does not prove unchanged behaviour.

## Benchmark case

Matching backend measures are followed by selection and blank-value checks in the duplicated Qlik app.

## Anti-patterns

- Judging presentation before source parity
- Treating one visual as full validation
- Mixing backend and formatting defects

## Stop

Stop when backend evidence and front-end behaviour both meet the migration contract.

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
