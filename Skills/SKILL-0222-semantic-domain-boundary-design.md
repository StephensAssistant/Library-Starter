---
id: SKILL-0222
type: skill
title: Semantic Cross-Domain Composition Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["design cross-domain semantic composition", "govern semantic composition keys", "compose established semantic domains"]
---

# Semantic Cross-Domain Composition Design

Reusable capability for defining governed composition between already-established analytical semantic domains.

## When to use

Use only when the requested action is composing established semantic domains without reopening their individual boundaries. Use SKILL-0097 when deciding semantic-model scope or whether domains should split or combine.

## Intent-routing contract

This Skill owns cross-domain composition design after the domain boundaries are established. Generic semantic-domain boundary and model-scope decisions belong to SKILL-0097; this Skill does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the already-established domain contracts, intended cross-domain questions, conformed keys, grains, ownership and applicable security constraints.
2. Use conformed dimensions, supported cross-domain keys, grain, ownership and security to define coherent composition without duplicating metrics or collapsing incompatible domains.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the composition contract with key/grain mappings, permitted combinations, security constraints and evidence that representative questions preserve the established domains and metric meanings.

## Benchmark case

Established sales and inventory domains remain separate and compose through governed conformed date, product and store keys.

Boundary design case: Sales and inventory share a field name but its grain or key meaning is unproved. Leave that composition unresolved; if the request instead changes domain boundaries, hand it to SKILL-0097.

## Anti-patterns

- Reopening or redefining domain boundaries inside this Skill.
- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the established boundaries, required access or supported composition contract is unknown. Do not claim completion without evidence of this Skill's specific result.

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
