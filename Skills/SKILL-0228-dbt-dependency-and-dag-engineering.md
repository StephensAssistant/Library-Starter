---
id: SKILL-0228
type: skill
title: dbt Dependency and DAG Engineering
status: current
created: 2026-09-20
updated: 2026-10-24
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt DAG", "dbt source ref", "dbt run order"]
---

# dbt Dependency and DAG Engineering

Reusable capability for defining and diagnosing dbt dependency and execution order.

## When to use

Use only when the requested action is defining and diagnosing dbt dependency and execution order. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Use source() for governed upstream objects and ref() for dbt-owned dependencies; inspect selection scope and environment availability before changing SQL.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

A missing downstream field is resolved by correcting dependency order rather than rewriting valid transformation logic.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Dependency-refresh evidence — 2026-10-11

Use this check when a downstream incremental model is stale although its job succeeds.

1. Trace direct and indirect inputs, hooks, physical source bindings, inherited materialisations, and actual job selectors.
2. For each input, record source arrival, ingestion completion, stage refresh, downstream selection, and successful run order as separate evidence. Tags, object names, and generated audit timestamps do not prove cadence or freshness.
3. Compare compiled manifest and runtime logs with retained configuration. Distinguish a stage rebuilt when selected from a stage actually selected and successfully refreshed.
4. Preserve healthy dependencies. Change only an evidenced refresh or ordering gap; source remapping and materialisation replacement require their own agreed scope.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.

Anti-pattern: treating a successful DAG as proof that every business change reaches the target.

Stop with the dependency/freshness evidence matrix and the precise failing boundary. Keep unknown cadence explicit.

## Contextual links

- `SKILL-0035` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
