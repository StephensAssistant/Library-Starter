---
id: SKILL-0261
type: skill
title: Snowflake Object Ownership Verification
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["verify Snowflake object ownership", "check owner after replace", "validate Snowflake ownership"]
links: []
tags: [snowflake, ownership, verification]
---

# Snowflake Object Ownership Verification

Verify the Snowflake object owner and effective grants after creation, replacement or ownership transfer.

## Intent routing contract

Activate only for verify Snowflake object ownership, check owner after replace, validate Snowflake ownership or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to verify the Snowflake object owner and effective grants after creation, replacement or ownership transfer.

## Method

1. Identify the expected governed owner and every required consumer/system role from current evidence.
2. Inspect the live object owner after the change; do not infer it from the creator, object name or prior state.
3. Verify applicable effective grants for each required role, including replacement-sensitive access.
4. Return the exact match, mismatch or access gap with evidence.

## Benchmark case

After CREATE OR REPLACE, the object’s owner matches the governed production owner and every required effective consumer grant is proven.

Boundary design case: The owner is correct after replacement but a required consumer grant is absent. Return that exact mismatch; owner equality alone does not complete ownership/effective-grant verification.

## Anti-patterns

- Expanding this Skill into access planning, approval or grant/ownership mutation.
- Treating tool success or an assumption as outcome evidence.
- Proceeding through an unresolved authority or evidence gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop complete only when ownership and applicable grants are evidenced; otherwise return the precise mismatch or access gap.

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
