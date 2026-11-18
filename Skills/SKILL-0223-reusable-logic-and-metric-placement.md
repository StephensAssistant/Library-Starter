---
id: SKILL-0223
type: skill
title: Reusable Logic and Metric Placement
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["metric placement", "canonical KPI layer", "reusable business logic location"]
---

# Reusable Logic and Metric Placement

Reusable capability for selecting one governed layer for reusable analytical logic and metrics.

## When to use

Use only when the requested action is selecting one governed layer for reusable analytical logic and metrics. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the approved logic/metric definition, consumers, current canonical owner, candidate layers and whether this is initial source-only Qlik conversion or a later reporting rebuild.
2. Place shared logic upstream and presentation-only logic in the BI layer; name the canonical owner and prevent divergent copies. For Snowflake-backed reporting, apply AGENTS.md’s Snowflake-owned facts/dimensions, Semantic View and per-report golden dynamic-table baseline. Reuse approved definitions; a placement decision does not authorise changing their meanings.
3. Preserve AGENTS.md’s source-only Qlik migration exception: keep existing Qlik load-script transformations during the initial source conversion. Apply the full reporting architecture at a later Sigma rebuild. Temporary testing and explicit front-end capabilities remain the governed exceptions, not permission for duplicated reusable metrics.
4. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
5. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return one justified canonical placement with consumer references, duplicate-definition risks and any applicable approved exception; preserve metric meaning and the current migration stage.

## Benchmark case

Net Sales is defined once in the governed model and consumed consistently by every workbook.

Boundary design case: An initial source-only Qlik migration contains portable load-script transformations. Preserve them under the stated exception; a placement review does not authorise an early Sigma architecture rebuild.

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
