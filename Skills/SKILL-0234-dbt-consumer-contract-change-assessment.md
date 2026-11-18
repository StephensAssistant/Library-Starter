---
id: SKILL-0234
type: skill
title: dbt Consumer Contract Change Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["rename dbt model", "change dbt column", "dbt downstream impact"]
---

# dbt Consumer Contract Change Assessment

Reusable capability for assessing downstream impact before changing a dbt model contract.

## When to use

Use only when the requested action is assessing downstream impact before changing a dbt model contract. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the proposed before/after model contract, current grain/name/columns/materialization, known downstream models and BI consumers, and available dependency evidence.
2. Trace models and BI consumers for column, name, grain and materialization dependencies; define migration and compatibility handling.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the affected-consumer inventory, contract differences, compatibility/migration handling and uncovered consumers; an incomplete inventory cannot establish no downstream impact.

## Benchmark case

A column rename proceeds only after every dependent model and report has a migration path.

Boundary design case: The dbt graph has no dependent model but BI consumer discovery is incomplete. Retain the BI impact gap; do not approve a column rename as safe from the graph alone.

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
