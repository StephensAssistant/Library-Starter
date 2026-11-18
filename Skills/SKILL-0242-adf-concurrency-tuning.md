---
id: SKILL-0242
type: skill
title: ADF Concurrency Tuning
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["ADF ForEach concurrency", "ADF parallel copy", "integration runtime tuning"]
---

# ADF Concurrency Tuning

Reusable capability for tuning ADF parallelism against measured source and sink capacity.

## When to use

Use only when the requested action is tuning ADF parallelism against measured source and sink capacity. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the representative pipeline/data volume, current ForEach/copy/runtime settings, source and sink capacity evidence, approved tuning scope and runtime/cost baseline.
2. Measure throttling, runtime, sink capacity and cost; adjust ForEach, copy and integration runtime settings from evidence.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return measured throughput, throttling, runtime and cost for each tested setting, retaining the last evidenced stable level and any untested capacity limit.

## Benchmark case

Concurrency increases until throughput stops improving or source throttling begins, then uses the last stable level.

Boundary design case: Higher parallelism increases source throttling without throughput improvement. Stop increasing it and retain the last evidenced stable setting; do not infer more capacity from an available concurrency field.

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
