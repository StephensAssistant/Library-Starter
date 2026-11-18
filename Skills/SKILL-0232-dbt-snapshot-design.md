---
id: SKILL-0232
type: skill
title: dbt Snapshot Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt snapshot", "dbt history tracking", "dbt SCD"]
---

# dbt Snapshot Design

Reusable capability for designing dbt snapshots for an explicit historical-state decision.

## When to use

Use only when the requested action is designing dbt snapshots for an explicit historical-state decision. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Define unique key, change strategy, timestamp/check behavior and consumer need; do not snapshot data without a history requirement.
3. Specify evidence-backed deletion, reappearance, late correction and validity-boundary meanings required by consumers. Confirm the installed dbt/adapter support before selecting configuration; do not infer that an omitted source row has a particular history effect.
4. Define expected histories for unchanged repeated input, update, delete and reappearance where applicable, with uniqueness and boundary checks. Deliver the design and expected results to testing; a design is not evidence that the history was built.
5. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
6. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

A status snapshot preserves decision-relevant state changes with a stable unique key.

Boundary design case: A source row disappears and the installed dbt/adapter deletion behaviour is unverified. Keep that history outcome unresolved; do not infer a closed validity interval or a successful deletion-history test.

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
