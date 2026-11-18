---
id: SKILL-0262
type: skill
title: Snowflake RBAC Change Execution
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["execute Snowflake grants", "apply approved RBAC plan", "change Snowflake roles"]
links: []
tags: [snowflake, rbac, execution]
---

# Snowflake RBAC Change Execution

Execute an explicitly approved Snowflake RBAC plan in controlled dependency order and capture exact results.

## Intent routing contract

Activate only for execute Snowflake grants, apply approved RBAC plan, change Snowflake roles or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to execute an explicitly approved Snowflake RBAC plan in controlled dependency order and capture exact results.

## Method

1. Reconfirm the approved plan, target objects/roles, order, recovery steps and executing authority immediately before mutation.
2. Execute only the approved CREATE ROLE, GRANT, REVOKE, ownership, managed-access or DROP statements in dependency order.
3. Use the least-privileged authorised role and capture every exact result or failed statement.
4. On the first failed or ambiguous statement, stop dependent mutations and reconcile each already-applied statement against live state. Do not replay the entire plan or assume earlier effects rolled back; use only the approved recovery steps after authority and actual effects are confirmed.
5. Stop at the approved mutation boundary and hand off the applied, failed and unexecuted statement receipt to effective-access validation.

## Benchmark case

An approved BI access-role plan is applied by the least-privileged authorised role in dependency order, with every result and failed statement captured.

Boundary design case: A GRANT succeeds and the next REVOKE fails. Preserve applied, failed and unexecuted statements, reconcile live effects and stop dependent mutations; do not replay the full plan or claim all statements rolled back.

## Anti-patterns

- Expanding this Skill into planning, approval, verification or another adjacent job.
- Treating tool success or an assumption as outcome evidence.
- Proceeding through an unresolved authority or evidence gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop before any mutation without explicit approval and verified authority; stop after approved mutations and hand off to effective-access validation.


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
