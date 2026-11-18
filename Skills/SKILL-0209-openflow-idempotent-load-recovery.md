---
id: SKILL-0209
type: skill
title: OpenFlow Idempotent Load Recovery
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["OpenFlow replay", "OpenFlow recovery", "partial OpenFlow failure", "idempotent OpenFlow load"]
---

# OpenFlow Idempotent Load Recovery

Reusable capability for recovering and replaying OpenFlow loads without corrupting target state.

## When to use

Use only when the requested action is recovering and replaying OpenFlow loads without corrupting target state. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Use stable source identifiers and deterministic merge behavior; preserve the failed window and sanitized error; test partial failure, replay and schema evolution.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Decision and evidence details

Before replay, identify the failed window, stable source IDs, target grain and deterministic merge rule. Inspect which target rows/effects actually committed and retain committed, rejected and unknown state. Resolve unknown effects before another load; a failure response is not proof that no rows changed. Keep retry/recovery bounded by the authorised source and load contract.

After authorised replay, compare expected IDs, duplicates and affected values with the failed-window baseline; repeat evidence must show correct rows remain unchanged. Boundary design case: a response is lost after a partial load. Reconcile target state first rather than launching the whole window blindly. Unknown schema-evolution semantics remain a gap, not an improvised merge rule.

## Benchmark case

Replaying an already-loaded Shopify window changes no correct target rows and adds no duplicates.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0032` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
