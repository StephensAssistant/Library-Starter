---
id: SKILL-0214
type: skill
title: OpenFlow Native-versus-Custom Flow Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["replace custom OpenFlow", "native OpenFlow connector parity", "retain custom flow"]
---

# OpenFlow Native-versus-Custom Flow Assessment

Reusable capability for deciding whether a custom OpenFlow flow should be retained or replaced.

## When to use

Use only when the requested action is deciding whether a custom OpenFlow flow should be retained or replaced. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Compare field, grain, incremental, recovery, performance and cost parity using current evidence; define rollback and reassessment triggers.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Decision and evidence details

Compare native and custom flow against the same required fields, grain, incremental scope and recovery scenarios. Record source/version evidence, observed measurements versus estimates, coverage gaps and the conditions that would change the recommendation. Missing comparable performance/cost evidence remains unknown rather than an assumed native advantage.

Boundary design case: the native connector covers fields but cannot prove required replay recovery. Retain the custom-flow recommendation or a precise assessment blocker; do not call coverage equivalent or retire anything. Return the retain/replace proposal with rollback/reassessment prerequisites; this assessment authorises no cutover.

## Benchmark case

A custom Orders flow is retired only after the native connector proves equivalent coverage and recovery.

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
