---
id: SKILL-0260
type: skill
title: Snowflake Object Ownership Transfer Execution
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["transfer Snowflake ownership", "execute ownership transfer", "change Snowflake object owner"]
links: []
tags: [snowflake, ownership, transfer]
---

# Snowflake Object Ownership Transfer Execution

Execute one approved Snowflake object-ownership transfer with verified authority and known downstream grant effects.

## Intent routing contract

Activate only for transfer Snowflake ownership, execute ownership transfer, change Snowflake object owner or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to execute one approved Snowflake object-ownership transfer with verified authority and known downstream grant effects.

## Method

1. Confirm the exact object, approved target owner, executing role and current owner immediately before mutation.
2. Confirm the approved grant-preservation or revocation behaviour and affected consumer/system roles.
3. Execute only the approved transfer with the least-privileged authorised role and capture the exact result.
4. If execution fails or the result is ambiguous, inspect current ownership and grants before retry or recovery; a failed call does not prove no transfer occurred. Stop dependent changes until actual effects are reconciled.
5. Hand off the resulting object to independent ownership and effective-grant verification.

## Benchmark case

An approved dynamic-table transfer runs under the least-privileged authorised role and captures the resulting owner and grant-handling outcome.

Boundary design case: The transfer request times out. Inspect current owner and grants before another transfer; hand off actual or unknown effects to verification rather than assuming rollback or reporting success.

## Anti-patterns

- Expanding this Skill into planning, approval, verification or another adjacent job.
- Treating tool success or an assumption as outcome evidence.
- Proceeding through an unresolved authority or evidence gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop before mutation when the target owner, approval, executing authority or grant effect is unknown; after execution, hand off to ownership verification.


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
