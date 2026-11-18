---
id: SKILL-0227
type: skill
title: Analytical Platform Capability Verification
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["verify semantic capability", "preview analytical feature", "materialization constraint"]
---

# Analytical Platform Capability Verification

Reusable capability for verifying volatile platform capabilities before architecture depends on them.

## When to use

Use only when the requested action is verifying volatile platform capabilities before architecture depends on them. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact capability and required behaviour, target account/edition/region, execution identity and authorised safe test scope.
2. Check current account, edition, region and feature status against authoritative documentation and a safe tenant test; record unsupported constraints.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return a capability finding scoped to the documented version/date and tested tenant context, distinguishing documented support, observed availability, unsupported constraints and unknown access.

## Benchmark case

A semantic integration is adopted only after the target account proves the required feature is available.

Boundary design case: Official documentation describes a feature but the target tenant cannot be tested with current access. Report tenant availability as unknown; do not call it supported or absent from the documentation alone.

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
