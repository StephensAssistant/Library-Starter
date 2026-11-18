---
id: SKILL-0142
type: skill
title: Snowflake Semantic View Query Validation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["validate semantic view", "test semantic queries", "check semantic metric totals"]
links: []
tags: [skill, action-specific]
---

# Snowflake Semantic View Query Validation

Validate a Snowflake Semantic View through introspection and representative semantic queries.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after creation or change; object creation alone is not correctness evidence.

## Method

1. Inspect the deployed definition and resolved objects.
2. Run representative queries across known metrics, dimensions and time slices.
3. Reconcile row-count sanity checks and known totals.
4. Test ambiguous paths, fan traps and multi-fact combinations explicitly.

## Decision and evidence details

Bind each query result to the deployed view/revision, query, role, population/time slice and authoritative expected total. Compare like-for-like populations and retain the first mismatch rather than relying on a matching grand total.

Boundary design case: a query executes but its expected total or cutoff is unknown. Report that validation gap and withhold correctness acceptance; successful execution proves neither metric meaning nor multi-fact additivity.

## Benchmark case

Two facts sharing dimensions are queried separately and together; known totals remain stable and ambiguous paths are rejected or resolved as designed.

## Anti-patterns

- Declaring success from CREATE alone
- Checking only one total
- Ignoring ambiguous-path behaviour

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/semantic-view-patterns

## Stop

Stop when representative queries return defensible totals and no unresolved ambiguity remains.

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
