---
id: SKILL-0141
type: skill
title: Snowflake Semantic View Definition Authoring
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["author semantic view DDL", "create semantic view YAML", "write CREATE SEMANTIC VIEW"]
links: []
tags: [skill, action-specific]
---

# Snowflake Semantic View Definition Authoring

Author a Snowflake Semantic View definition in DDL or YAML from an approved semantic design.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after grains, relationships, metrics and exact source identities are agreed.

## Method

1. Choose DDL or YAML from current feature parity and deployment needs.
2. Map approved roles to exact table and column names.
3. Generate the smallest readable definition and preserve object identity.
4. For YAML, run the supported dry-run; include required post-deploy DDL where parity is incomplete.

## Decision and evidence details

Retain the approved semantic design, exact source identities, chosen format/capability evidence and the definition/check result. Authoring the definition and required post-deploy statements does not itself authorise their deployment. A dry-run proves only its checked scope, not deployed query correctness.

Boundary design case: a required capability has no verified YAML representation. Keep the approved DDL-only configuration explicit or report the format gap; do not silently omit it to obtain a valid YAML file.

## Benchmark case

An approved multi-fact model is expressed with exact production names, dry-run successfully and retains any required DDL-only configuration.

## Anti-patterns

- Copying example object names
- Using YAML for a DDL-only feature
- Changing the semantic design while authoring

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/semantic-view-patterns

## Stop

Stop when the definition represents the approved model and passes the applicable syntax or dry-run check.

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
