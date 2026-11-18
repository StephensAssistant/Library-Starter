---
id: SKILL-0215
type: skill
title: Snowflake Streamlit Entity and Write Contract
status: current
created: 2026-09-20
updated: 2026-10-24
links: []
tags: [skill, action-specific]
trigger_phrases: ["Streamlit entity contract", "Streamlit write contract", "editable Snowflake entity"]
---

# Snowflake Streamlit Entity and Write Contract

Reusable capability for defining the authoritative entity and write boundary for a Snowflake Streamlit application.

## When to use

Use only when the requested action is defining the authoritative entity and write boundary for a Snowflake Streamlit application. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. State grain, natural key, editable and immutable fields, validations, deletion semantics and downstream consumers; keep reusable domain rules in governed Snowflake objects.
3. Define the expected pre-mutation state/version and the business decision for conflicting edits. State whether a stale request is rejected, reconciled or deliberately overwrites, who may make that decision, and the observable committed/rejected/unknown outcome. Hand this contract to mutation and idempotency implementation; UI state alone is not a concurrency control.
4. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
5. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

An Additional Charges editor has a declared one-row grain and stable stored key before UI construction.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.


## Contextual links

- `SKILL-0033` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
