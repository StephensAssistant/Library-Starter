---
id: SKILL-0145
type: skill
title: Snowflake Current and Future Grant Planning
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["plan Snowflake grants", "Snowflake future grants", "grant existing and future objects"]
links: []
tags: [skill, action-specific]
---

# Snowflake Current and Future Grant Planning

Plan paired current-object and future Snowflake grants for an approved access requirement.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when durable schema-level access must cover existing and newly created objects.

## Method

1. Identify the audience, access role, databases, schemas, warehouses and object types.
2. Inventory current grants, future grants, ownership and managed-access authority.
3. Plan required database and schema USAGE plus matching grants on ALL existing and FUTURE applicable schema objects, including tables, views and dynamic tables.
4. Plan warehouse privileges separately: grant USAGE for query execution; add OPERATE, MONITOR or ownership privileges only when the approved operational responsibility requires them.
5. For managed-access schemas, identify the schema owner or role authorised to grant; object owners alone cannot grant access there.
6. After CREATE OR REPLACE or ownership transfer, require effective-grant verification because recreated objects or ownership changes can alter access.
7. Document narrower object, row-policy or other exceptions and the authority needed to apply them.

## Decision and evidence details

Return a current-versus-required grant plan by role, scope and object type, with current/future coverage, separate warehouse privileges, exceptions and executing authority. This planning result is not a mutation receipt.

Boundary design case: object ownership is visible but managed-access grant authority is unresolved. Keep the plan's authority gap explicit and block application rather than assuming the object owner can grant. Record effective-access verification as a required post-change check, not a completed result.

## Benchmark case

A reporting role receives database/schema USAGE, warehouse USAGE and SELECT on all current and future tables, views and dynamic tables; warehouse OPERATE and OWNERSHIP remain excluded.

## Anti-patterns

- Future grants without current grants
- Omitting dynamic tables or another applicable type
- Granting directly to users
- Treating warehouse USAGE, OPERATE, MONITOR and OWNERSHIP as interchangeable
- Omitting database/schema USAGE or managed-access grant authority

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/rbac

## Stop

Stop when current and future coverage, grant authority and exceptions are explicit.

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
