---
id: SKILL-0213
type: skill
title: OpenFlow Private Connectivity Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["OpenFlow PrivateLink", "OpenFlow private connectivity", "OpenFlow network rule"]
---

# OpenFlow Private Connectivity Design

Reusable capability for designing supported private network connectivity for an OpenFlow deployment.

## When to use

Use only when the requested action is designing supported private network connectivity for an OpenFlow deployment. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Verify current cloud support, endpoint service, network rule, external access integration and runtime association; do not transpose provider-specific instructions.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Decision and evidence details

For this connectivity design, identify deployment cloud/account/region, source endpoint and required runtime path from authoritative environment evidence. Map each verified endpoint service, network rule, external access integration and runtime association to that path; preserve exact identities and evidence dates. The existing adjacent-architecture exclusion does not remove the owned connectivity-design task.

Return the supported design, prerequisites, unresolved links and required connectivity verification separately from deployment. Boundary design case: provider support is documented but the target runtime association is unknown. Keep the end-to-end path unverified and block dependent implementation instructions rather than copying another provider's setup.

## Benchmark case

An Azure deployment uses verified Azure connectivity components instead of copied AWS PrivateLink steps.

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
