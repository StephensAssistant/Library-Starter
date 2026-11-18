---
id: SKILL-0231
type: skill
title: dbt Model Contract Testing
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt data test", "dbt freshness test", "dbt model contract"]
---

# dbt Model Contract Testing

Reusable capability for defining and executing data tests at a dbt model's real grain.

## When to use

Use only when the requested action is defining and executing data tests at a dbt model's real grain. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the model/version, true row grain, business keys, accepted values/invariants, source freshness requirement and authoritative reconciliation population.
2. Test uniqueness, non-null, relationships, accepted values, business invariants and source freshness; reconcile key measures across changed boundaries.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return each test expectation, observed result and failing population with source/model context; distinguish syntax success, data-test results and cross-boundary reconciliation.

## Benchmark case

A model passes syntax and also proves its business key and downstream totals.

Boundary design case: The model compiles and its grand total matches, but the real business key duplicates. Report the uniqueness failure and exact population rather than accepting the model or weakening the key test.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

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
