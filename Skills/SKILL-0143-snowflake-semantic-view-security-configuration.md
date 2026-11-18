---
id: SKILL-0143
type: skill
title: Snowflake Semantic View Security Configuration
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["secure Snowflake semantic view", "semantic view row access", "semantic view caller rights"]
links: []
tags: [skill, action-specific]
---

# Snowflake Semantic View Security Configuration

Configure verified security behaviour for a Snowflake Semantic View.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when an approved semantic design requires row access, caller rights or role-sensitive behaviour.

## Method

1. Define the required audience and access boundary.
2. Verify current platform capability and interaction with underlying policies.
3. Prepare the least-privilege configuration and obtain approval before mutation.
4. Validate representative allowed and denied access through effective roles.

## Decision and evidence details

Retain the approved access boundary, exact view/policy configuration and effective-role context for each allow/deny result. After an interrupted or failed configuration change, inspect actual saved security state before repair; do not assume failure left the previous policy intact. Recovery remains within approved mutation scope.

Boundary design case: the allowed persona works but the denied persona cannot be tested. Keep security acceptance incomplete and name the missing denial evidence.

## Benchmark case

A regional semantic view applies verified row access and proves one permitted and one denied persona outcome.

## Anti-patterns

- Assuming underlying security propagation
- Using undocumented role behaviour
- Testing only an allowed case

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/semantic-view-patterns

## Stop

Stop when the intended allow and deny behaviour is evidenced under representative roles.

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
