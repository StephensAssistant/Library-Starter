---
id: SKILL-0220
type: skill
title: Snowflake Streamlit CRUD Test Execution
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["test Streamlit CRUD", "Streamlit CRUD matrix", "Streamlit application test"]
---

# Snowflake Streamlit CRUD Test Execution

Reusable capability for executing a complete CRUD behavior matrix for a Snowflake Streamlit application.

## When to use

Use only when the requested action is executing a complete CRUD behavior matrix for a Snowflake Streamlit application. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact app/version, authorised test environment and identities, bounded fixtures/cleanup, supported CRUD actions and independently specified business/audit outcomes.
2. Test create, duplicate create, edit, no-op edit, remove, repeated remove, invalid input, rerun, tab state and downstream synchronization.
3. Exercise the contracted denied actor, stale edit, concurrent duplicate and lost-response cases in the authorised test scope. Compare committed business rows and trusted audit outcomes with explicit expectations; prove rejected operations leave protected state unchanged. Keep test fixtures and their permitted cleanup bounded, and hand an unknown mutation outcome to the mutation/idempotency owner rather than rerunning it blindly.
4. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
5. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the action/case matrix with expected and observed business state, audit evidence, downstream result and any unexecuted case; a designed matrix alone is not execution evidence.

## Benchmark case

The test matrix proves duplicate prevention and stable state across every supported CRUD action.

Boundary design case: The test cannot determine whether a lost-response mutation committed. Preserve the fixture/request state and hand it to reconciliation; do not rerun merely to complete the matrix.

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
