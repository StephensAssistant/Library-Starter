---
id: SKILL-0148
type: skill
title: Snowflake RBAC Change Planning
status: current
created: 2026-09-20
updated: 2026-10-24
owner: Library owner

trigger_phrases: ["prepare Snowflake RBAC change plan", "design RBAC change", "Snowflake grant plan"]
links: []
tags: [skill, snowflake, rbac, planning]
---

# Snowflake RBAC Change Planning

Produce an approval-ready Snowflake RBAC before/after graph and ordered change and recovery plan without mutation.

## Intent routing contract

Activate only for prepare Snowflake RBAC change plan, design RBAC change, Snowflake grant plan or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to produce an approval-ready Snowflake RBAC before/after graph and ordered change and recovery plan without mutation.

## Method

1. Confirm the target hierarchy, exact privileges, affected users/roles and current grant evidence.
2. Produce the before/after role and grant graph plus ordered SQL plan.
3. Include revocations, ownership effects, managed-access effects, user-impact checks, executing authority and recovery steps.
4. Present the plan for explicit approval; do not execute any mutation under this Skill.

## Benchmark case

A BI role change plan lists ordered grants and revocations, ownership and user impacts, execution authority and recovery steps before approval.

## Anti-patterns

- Expanding this Skill into an adjacent diagnosis, execution or verification job.
- Treating one inconsistent precedent or assumption as authority.
- Proceeding through an unresolved evidence or authority gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the target hierarchy, exact privileges, affected users/roles, execution authority or recovery path is unresolved.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; adjacent jobs moved to independent Skills.

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
