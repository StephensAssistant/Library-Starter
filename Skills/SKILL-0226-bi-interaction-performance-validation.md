---
id: SKILL-0226
type: skill
title: BI Interaction Performance Validation
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dashboard interaction latency", "BI first load performance", "filter latency test"]
---

# BI Interaction Performance Validation

Reusable capability for measuring customer-facing responsiveness for an analytical serving design.

## When to use

Use only when the requested action is measuring customer-facing responsiveness for an analytical serving design. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the dashboard/serving candidates, representative users and interactions, date/data scope, cache and concurrency conditions, and the agreed responsiveness requirement.
2. Record representative first load, filter and date interaction latency; test early filtering where semantics remain correct; separate experience from compute cost.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return first-load and per-interaction observations under declared conditions, correctness checks and the comparison/verdict; if no acceptance target exists, report measurements without inventing a pass threshold.

## Benchmark case

Two serving candidates are compared using the same dashboard interactions and date window.

Boundary design case: One candidate uses a warm cache and the other a cold first load. Keep those observations distinct and obtain comparable evidence before declaring a responsiveness improvement.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0034` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
