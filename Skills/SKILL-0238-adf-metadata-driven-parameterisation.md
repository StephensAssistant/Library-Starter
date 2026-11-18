---
id: SKILL-0238
type: skill
title: ADF Metadata-Driven Parameterisation
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["ADF metadata pipeline", "ADF parameterization", "config driven ADF"]
---

# ADF Metadata-Driven Parameterisation

Reusable capability for designing reusable parameterised ADF pipelines for homogeneous sources.

## When to use

Use only when the requested action is designing reusable parameterised ADF pipelines for homogeneous sources. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the candidate feeds, authentication, pagination, error/recovery behaviour, configuration owner and parameters from current source contracts.
2. Define configuration ownership and parameters; reuse only where authentication, pagination, errors and recovery are materially alike.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the shared parameter/configuration contract and a feed-by-feed compatibility decision, identifying sources whose materially different behaviour requires a separate pipeline.

## Benchmark case

Ten equivalent file feeds share one configured pipeline while an API with different recovery stays separate.

Boundary design case: Two sources share field names but one has different authentication and recovery. Keep it outside the reusable pipeline until compatibility is evidenced; a common schema alone is insufficient.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0036` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
