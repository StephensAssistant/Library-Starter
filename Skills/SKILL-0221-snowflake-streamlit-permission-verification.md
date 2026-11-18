---
id: SKILL-0221
type: skill
title: Snowflake Streamlit Permission Verification
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["Streamlit application role", "Streamlit permission check", "Snowflake Streamlit grants"]
---

# Snowflake Streamlit Permission Verification

Reusable capability for verifying Snowflake permissions from the application execution context.

## When to use

Use only when the requested action is verifying Snowflake permissions from the application execution context. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the application execution context, exact objects, required read/write/procedure operations and expected permitted or denied outcomes from the current access contract.
2. Identify the executing role and required warehouse, database, schema, table and procedure privileges; test from that context rather than an administrator account.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return an operation/object/role matrix with observed access and evidence from the actual execution context; report missing privileges without changing grants during verification.

## Benchmark case

The deployed app role can read options and execute the write procedure without inherited developer privileges.

Boundary design case: An administrator can execute the procedure but the application role cannot. Report the application-context failure; the administrator result does not satisfy the required permission proof.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0033` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
