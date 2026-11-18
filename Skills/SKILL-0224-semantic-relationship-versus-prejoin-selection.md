---
id: SKILL-0224
type: skill
title: Semantic Relationship-versus-Prejoin Selection
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["relationship versus prejoin", "semantic prejoin decision", "denormalise analytical model"]
---

# Semantic Relationship-versus-Prejoin Selection

Reusable capability for deciding whether analytical entities should remain related or be prejoined.

## When to use

Use only when the requested action is deciding whether analytical entities should remain related or be prejoined. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the entities, keys, grains, representative analytical queries, measured join cost and required result semantics before comparing relationship and prejoin candidates.
2. Prove cardinality and fan-out; prefer relationships when pruning works; prejoin only when repeated measured cost justifies it.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the evidenced cardinality/fan-out checks and comparable workload findings, with the selected approach and unresolved pruning or cost assumptions.

## Benchmark case

A high-cost stable join is precomputed only after relationship queries show material repeated overhead.

Boundary design case: A fast prejoin duplicates a measure because join cardinality is unproved. Withhold the selection until grain and fan-out are resolved; latency alone cannot justify it.

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
