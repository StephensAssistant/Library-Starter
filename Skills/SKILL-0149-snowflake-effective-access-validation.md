---
id: SKILL-0149
type: skill
title: Snowflake Effective Access Validation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["validate Snowflake access", "test Snowflake grants", "prove allow deny access"]
links: []
tags: [skill, action-specific]
---

# Snowflake Effective Access Validation

Validate effective Snowflake access after an RBAC change.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after grants, revocations, ownership or role hierarchy changes.

## Method

1. Inspect SHOW GRANTS and effective inheritance for the target persona.
2. Run representative allowed operations with the intended role context.
3. Run representative denied operations to prove the boundary.
4. Record discrepancies between configured and effective access for repair.

## Decision and evidence details

Before an access test, verify its target, representative persona and permitted test effects. A denied-case test must have an authorised safe boundary if access unexpectedly succeeds. Retain the operation, role context, expected/actual outcome and any actual effect; unexpected success is a boundary failure, not a reason to continue broader testing.

Boundary design case: an intended read-only role can write. Preserve the observed effect and route repair; do not grant more access or repeat destructive operations to demonstrate the defect.

## Benchmark case

A BI persona can query one reporting schema and use its warehouse but cannot write or access unrelated schemas.

## Anti-patterns

- Treating successful GRANT as access proof
- Testing only as an administrator
- Skipping denied-case testing

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/rbac

## Stop

Stop when both intended access and intended denial are evidenced.

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
