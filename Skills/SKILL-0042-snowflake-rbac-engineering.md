---
id: SKILL-0042
type: skill
title: Snowflake Role Hierarchy Design
status: current
created: 2026-09-17
updated: 2026-10-31
trigger_phrases: ["design Snowflake RBAC", "Snowflake role hierarchy", "access role persona role design"]
links: []
tags: [skill, snowflake, access-control, security]
---

# Snowflake Role Hierarchy Design

Design a least-privilege Snowflake role hierarchy for an approved access requirement.

## Intent-routing contract

This Skill owns role hierarchy design only. Grant planning, ownership governance, policy-role evaluation, RBAC execution and effective-access validation are separate actions.

## When to use

Use when account, environment, domain, database, schema, warehouse, access or persona roles must be designed or rationalised.

## Method

1. Inventory current roles, inheritance, persona assignments, ownership and access boundaries.
2. Separate data-product access roles from functional or persona roles.
3. Separate data-object access roles, warehouse-use roles and object-owner roles; consumer/persona roles may inherit access and warehouse-use roles but must not inherit routine ownership merely to query data.
4. Grant object privileges conceptually to access roles, then grant access and approved warehouse-use roles to functional roles.
5. Keep warehouse administration separate: USAGE permits query execution; OPERATE permits start, stop, suspend and resume; MONITOR supports authorised operational visibility; OWNERSHIP and CREATE WAREHOUSE remain administrative unless explicitly required.
6. Choose only hierarchy layers the estate requires; names and layer counts are local decisions.
7. Produce the proposed hierarchy and explain each boundary before grant planning.

## Benchmark case

A BI persona inherits a reporting-schema access role and warehouse USAGE role, while OPERATE, MONITOR and OWNERSHIP remain with explicitly authorised operational or owner roles.

Missing-input design case: a persona needs to query data but its operational privileges are unspecified. Design only the evidenced access boundary and identify the remaining decision; do not add warehouse OPERATE or ownership to compensate for an unknown requirement.

## Anti-patterns

- Direct routine object access through individual users
- One giant role owning and accessing everything
- Granting warehouse OWNERSHIP or OPERATE to a consumer role that only needs USAGE
- Copying a generic layer count without estate need

## Authoritative source

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/rbac

## Stop

Stop when role purposes, inheritance and persona boundaries are explicit enough for grant planning.

## Contextual links

- `SKILL-0145` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0146` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0147` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0148` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0149` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0260` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0261` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0262` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 8 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
