---
id: SKILL-0210
type: skill
title: OpenFlow Asynchronous Operation Control
status: current
created: 2026-09-20
updated: 2026-10-24
links: []
tags: [skill, action-specific]
trigger_phrases: ["OpenFlow bulk operation", "asynchronous OpenFlow operation", "OpenFlow operation polling"]
---

# OpenFlow Asynchronous Operation Control

Reusable capability for controlling asynchronous and bulk source operations used by OpenFlow.

## When to use

Use only when the requested action is controlling asynchronous and bulk source operations used by OpenFlow. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Model submission, operation ID, running, completed, failed, result retrieval and retryability as separate states; never equate transport success with operation success. Retain the exact request identity and source-issued operation identity.
3. Define source-backed polling limits and terminal/error states. If acknowledgement is lost, reconcile the original operation using the supported source contract before resubmitting; an unknown outcome is not a failed operation. Retry submission only with evidenced duplicate protection or after proving no operation was created. Validate the completed result identity, scope and completeness before passing it to loading; hand an unresolved operation to its owner with the last confirmed state.
4. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
5. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

A bulk GraphQL request is not loaded until its completed state and result artifact are verified.

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
