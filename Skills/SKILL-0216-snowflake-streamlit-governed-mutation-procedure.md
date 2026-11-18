---
id: SKILL-0216
type: skill
title: Snowflake Streamlit Governed Mutation Procedure
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["Streamlit stored procedure write", "governed Streamlit mutation", "Streamlit persistent write"]
---

# Snowflake Streamlit Governed Mutation Procedure

Reusable capability for implementing persistent Streamlit mutations through a governed Snowflake write layer.

## When to use

Use only when the requested action is implementing persistent Streamlit mutations through a governed Snowflake write layer. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the exact application, target records, permitted mutation, procedure execution context, required business rules, audit evidence and expected affected-row outcomes from authoritative sources.
2. Use explicit procedure parameters, backend validation, duplicate checks, audit stamping and transactional outcomes; keep business rules out of button callbacks.
3. Specify and verify the transaction boundary for the exact statements and execution context. Define expected-state/version checks and exact affected-row outcomes for conflicting, absent and duplicate records; commit the permitted business mutation and trusted audit evidence consistently. Do not infer atomicity from a procedure call succeeding.
4. On failure or a lost response, retain request identity and establish committed, rejected or unknown state from durable evidence before retry. Reconcile a prior result through the idempotency contract rather than blindly repeating the mutation. Verify rollback/preservation and stale-edit behaviour in the authorised runtime before claiming enforcement.
5. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
6. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the procedure contract, transaction and conflict outcomes, request-reconciliation path and actual verification evidence; distinguish an implemented procedure from runtime-proven enforcement.

## Benchmark case

A charge update calls one governed procedure that validates and commits the complete mutation.

Boundary design case: A procedure response is lost after submission. Preserve request identity and reconcile durable business/audit state before retry; unresolved commit state prevents a completion claim.

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
