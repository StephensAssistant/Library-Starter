---
id: SKILL-0144
type: skill
title: Snowflake Semantic View Decision Recording
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["document semantic view design", "record semantic model decisions", "semantic view rollback plan"]
links: []
tags: [skill, action-specific]
---

# Snowflake Semantic View Decision Recording

Record the approved design and redeployment decisions for a Snowflake Semantic View.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after design or material change so grain, relationships, metrics and recovery route remain reproducible.

## Method

1. Record object identity, source authority and business questions.
2. Record grains, keys, cardinalities, metric additivity and selected patterns.
3. Record capability constraints, security decisions and validation evidence.
4. Record ordered redeployment and recovery steps without inventing rollback capability.

## Decision and evidence details

Bind the decision record to the approved model/definition revision and distinguish observed validation results from planned checks. For each recovery step, identify its prerequisite and verified capability; record any unavailable recovery route as a gap instead of an executable instruction.

Boundary design case: the DDL is available but the reason for a multi-fact path is missing. Keep that design decision unresolved; generated syntax alone cannot explain or reproduce the approved semantic meaning.

## Benchmark case

A multi-fact view record explains the grain and path decision, validation totals and exact redeployment sequence.

## Anti-patterns

- Recording only generated DDL
- Omitting rejected alternatives that affect maintenance
- Claiming rollback without a proven route

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/semantic-view-patterns

## Stop

Stop when another authorised developer can explain and reproduce the approved semantic design.

## Contextual links

- `SKILL-0041` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
