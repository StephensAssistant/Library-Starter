---
id: SKILL-0217
type: skill
title: Snowflake Streamlit Write Idempotency
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["Streamlit double submit", "Streamlit rerun duplicate", "idempotent Streamlit write"]
---

# Snowflake Streamlit Write Idempotency

Reusable capability for preventing duplicate or corrupt writes from repeated Streamlit actions.

## When to use

Use only when the requested action is preventing duplicate or corrupt writes from repeated Streamlit actions. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the application action, entity identity, logical request identity, backend duplicate-protection contract and expected business/audit result, including the supported identity scope and lifetime.
2. Use stable entity IDs, form boundaries, duplicate guards and explicit outcomes; distinguish entity identity from one logical mutation request. Preserve a request identity across reruns and lost responses.
3. Define backend duplicate protection for concurrent requests, the scope/lifetime of request identity, and how an already committed result is retrieved. Reject a reused request identity with conflicting content. A disabled button or pre-write existence check alone is not proof of durable duplicate prevention.
4. Prove repeated and concurrent submission, rerun and response-loss behaviour against the same request, including committed mutation/audit evidence. Reconcile unknown outcomes before retrying and stop with the exact unresolved request state if the evidence is unavailable.
5. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
6. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the request-to-result mapping and repeated/concurrent/lost-response observations, identifying any unproved duplicate-protection boundary.

## Benchmark case

Double-clicking Add creates one governed record, not two.

Boundary design case: The same request identity arrives with changed content. Reject it as a conflict; do not treat it as a successful repeat or allocate a new identity merely to bypass the guard.

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
