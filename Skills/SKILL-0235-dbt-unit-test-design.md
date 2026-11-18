---
id: SKILL-0235
type: skill
title: dbt Unit Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt unit test", "mock dbt model input", "dbt test fixture"]
---

# dbt Unit Test Design

Reusable capability for designing deterministic dbt unit tests for transformation logic.

## When to use

Use only when the requested action is designing deterministic dbt unit tests for transformation logic. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the transformation revision, direct input contracts, business rules, supported test context and deterministic expected rows; sanitize fixture data before reuse.
2. Mock direct inputs, specify expected rows, sanitize fixtures and cover meaningful branches, joins and date logic; run before materialization.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return minimal fixtures and exact expected outputs tied to branches, joins and date boundaries, plus actual execution evidence when available; design alone is not a passing test.

## Benchmark case

A date-allocation regression is reproduced with a small fixed input and exact expected rows.

Boundary design case: A date-allocation rule has no agreed boundary meaning. Keep the expected row unresolved and route the rule to its owner; do not derive the oracle solely from current implementation output.

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
