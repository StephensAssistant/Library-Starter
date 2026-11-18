---
id: SKILL-0212
type: skill
title: OpenFlow Service-Boundary Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["OpenFlow runtime failure", "OpenFlow processor failure", "diagnose OpenFlow"]
---

# OpenFlow Service-Boundary Diagnosis

Reusable capability for locating the first unhealthy component in an OpenFlow service graph.

## When to use

Use only when the requested action is locating the first unhealthy component in an OpenFlow service graph. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Check controller/runtime, connector, object registry, checkpoint service, target service and authentication independently; preserve boundary-specific evidence before editing flow logic.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Decision and evidence details

Bind the diagnosis to the failed flow/run, sanitized error, time and last confirmed healthy boundary. Trace the actual request path through the named components, recording each component's own evidence rather than treating a downstream symptom as its cause. Distinguish confirmed failure from inaccessible health evidence.

Boundary design case: connector metadata is readable but checkpoint access is denied. Preserve the healthy connector observation and checkpoint evidence gap; do not repeatedly edit connector logic or declare checkpoint corruption without proof. Stop with the earliest evidenced unhealthy boundary, owner and next discriminating check; this diagnosis does not authorise deployment or replay.

## Benchmark case

A failed flow is traced to checkpoint state rather than repeatedly changing a healthy connector definition.

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
