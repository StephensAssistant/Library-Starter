---
id: SKILL-0147
type: skill
title: Snowflake Policy-Aware Role Evaluation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["evaluate Snowflake secondary roles", "policy role session semantics", "IS_ROLE_IN_SESSION"]
links: []
tags: [skill, action-specific]
---

# Snowflake Policy-Aware Role Evaluation

Evaluate effective Snowflake role behaviour where row-access or masking policies depend on session roles.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when CURRENT_ROLE, secondary roles or policy functions may change an access decision.

## Method

1. Identify the policy condition and every role active in the representative session.
2. Verify current supported role-evaluation functions and semantics.
3. Model intended allow and deny outcomes without assuming CURRENT_ROLE represents all access.
4. Test with representative sessions and retain effective-role evidence.

## Decision and evidence details

For each tested policy outcome, retain policy revision, test identity, primary and active secondary roles, expected allow/deny result and actual result. Compare representative sessions under the verified current semantics; an administrator's successful query cannot substitute for the intended persona.

Boundary design case: changing secondary-role state changes policy access unexpectedly. Preserve both session results and the unresolved policy boundary; do not explain it solely from CURRENT_ROLE or accept only the permissive session.

## Benchmark case

A row-access policy using role membership is tested with primary and secondary role combinations to prove intended access.

## Anti-patterns

- Ignoring secondary roles
- Using undocumented session semantics
- Testing policies only as an administrator

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/rbac

## Stop

Stop when policy outcomes are explained by verified effective-session semantics.

## Contextual links

- `SKILL-0042` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
