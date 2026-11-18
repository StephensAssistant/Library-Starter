---
id: SKILL-0041
type: skill
title: Snowflake Semantic View Model Design
status: current
created: 2026-09-17
updated: 2026-10-31
trigger_phrases: ["design Snowflake semantic view", "semantic view pattern", "model semantic facts dimensions metrics"]
links: []
tags: [skill, snowflake, semantic-layer, data-model]
---

# Snowflake Semantic View Model Design

Design a defensible Snowflake Semantic View model without metric inflation or ambiguous relationship paths.

## Intent-routing contract

This Skill owns semantic model design and pattern selection. Capability verification, definition authoring, query validation, security configuration and decision recording are separate actions.

## When to use

Use when business questions, facts, dimensions, metrics, relationships and semantic-query paths must be designed. Use SKILL-0098 for the upstream physicalization comparison and selection within the governing architecture; SKILL-0034 implements an already-approved serving-layer change.

## Method

1. State the business questions, table grains, conformed keys, time grains, metric additivity and security boundary.
2. Select the smallest fitting documented pattern.
3. Map each pattern role to exact source tables and columns.
4. Prove relationship cardinality and inspect fan traps, chasm traps and multiple valid paths.
5. Resolve grain, key or additivity gaps before definition authoring.

## Benchmark case

Two facts share date and product dimensions; the design proves each grain and selects a multi-fact pattern that prevents inflated totals.

Boundary design case: two facts share column names but the proposed relationship has unresolved many-to-many cardinality. Keep the affected semantic path unresolved and block dependent definition authoring; shared dimensions alone do not establish an inflation-safe multi-fact pattern.

## Anti-patterns

- Treating shared dimensions as proof of safe multi-fact joins
- Omitting metric additivity and time-grain rules
- Selecting patterns before proving exact source roles

## Authoritative source

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/semantic-view-patterns

## Stop

Stop when grains, keys, cardinalities, additivity and semantic paths are explicit and defensible.


## Contextual links

- `SKILL-0140` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0141` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0142` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0143` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0144` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 5 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
