---
id: SKILL-0036
type: skill
title: ADF Source-to-Sink Pipeline Orchestration
status: current
created: 2026-09-16
updated: 2026-10-31
links: []
tags: [skill, azure, adf, orchestration]
trigger_phrases: ["ADF source to sink", "ADF copy pipeline", "Azure Data Factory orchestration", "ADF service boundary"]
---

# ADF Source-to-Sink Pipeline Orchestration

Reusable capability for orchestrating one defined source-to-sink movement in Azure Data Factory.

## When to use

Use only when the requested action is orchestrating one defined source-to-sink movement in Azure Data Factory. Use the independent action-specific Skills for adjacent validation, recovery, testing, performance, rehearsal or delivery work.

## Intent-routing contract

This Skill owns this one action from authoritative inputs to its evidenced result. It does not absorb adjacent jobs merely because they use the same platform or subject.

## Method

1. Confirm authoritative inputs, scope and success condition.
2. Define source and sink contracts, movement boundary, executing services, request/response behavior and durable success point. Keep auxiliary calls explicit and do not bury state transitions in opaque activities.
3. Preserve evidence, assumptions, result and any unresolved material gap.


### Application checks

Map the source read, each transport/service boundary and sink write to the exact object, executing identity, request output and durable evidence. Keep “request accepted”, “data moved” and “sink committed” distinct. Before a retry after an uncertain write, identify the last confirmed boundary and hand the affected state to the appropriate recovery capability; do not replay the whole path from a successful source response alone.

## Evidence expected

Retain the inputs, checks, chosen result, source/date context and any condition that requires reassessment.

## Benchmark case

An SFTP file is moved through Blob Storage into Snowflake with explicit boundaries and a durable sink-write success condition.

Boundary design case: the source read succeeds but the sink write times out. Report the last confirmed boundary and uncertain sink effect; inspect durable state under the recovery owner before replay, rather than treating the source response as end-to-end success.

## Anti-patterns

- Expanding this Skill into another action because the subject is similar.
- Treating tool success or polished output as verified evidence.
- Proceeding through an unresolved material input or authority gap.

## Stop

Stop when the authoritative input or success condition is unknown. Route the next distinct action to its own Skill.

## Contextual links

- `SKILL-0238` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0239` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0240` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0241` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0242` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0243` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0244` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0245` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0246` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0247` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0283` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0284` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 12 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
