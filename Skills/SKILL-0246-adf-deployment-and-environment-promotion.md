---
id: SKILL-0246
type: skill
title: ADF Deployment and Environment Promotion
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["deploy ADF pipeline", "ADF Git promotion", "ADF environment parameters"]
---

# ADF Deployment and Environment Promotion

Reusable capability for promoting ADF configuration safely between environments.

## When to use

Use only when the requested action is promoting ADF configuration safely between environments. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, pipeline implementation or approval work; this Skill executes only the specifically authorised environment promotion.

## Method

1. Confirm the authoritative inputs, scope and success condition.
2. Preserve environment separation, parameters, configuration ownership and rollback; verify the estate's current Git/live convention. Confirm the exact tested revision, destination, identities and environment-specific connections before promotion; check the deployed revision and representative operation afterward. On partial or ambiguous deployment, reconcile actual destination state before retry or use of the approved recovery path.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

## Benchmark case

A tested DEV pipeline reaches production with environment-specific connections and a documented rollback.

Boundary design case: The tested revision is known but the destination connection or executing identity is unresolved. Stop before promotion and name the missing environment evidence; a successful DEV test cannot substitute for it.

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
