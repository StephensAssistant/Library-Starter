---
id: SKILL-0146
type: skill
title: Snowflake Object Owner Determination
status: current
created: 2026-09-20
updated: 2026-10-24
owner: Library owner

trigger_phrases: ["determine Snowflake object owner", "select Snowflake object owner", "Snowflake ownership rule"]
links: []
tags: [skill, snowflake, ownership, determination]
---

# Snowflake Object Owner Determination

Determine the required governed owner before a Snowflake object is created, replaced or transferred.

## Intent routing contract

Activate only for determine Snowflake object owner, select Snowflake object owner, Snowflake ownership rule or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to determine the required governed owner before a Snowflake object is created, replaced or transferred.

## Method

1. Inventory current ownership rules and multiple comparable governed objects in the same estate area, including warehouses when warehouse ownership is in scope.
2. Resolve the least-privileged owner role from verified estate rules; object names or one inconsistent precedent are not authority.
3. Keep object-owner roles separate from consumer/access roles; warehouse ownership gives administrative control and must not be assigned merely to permit queries.
4. Before CREATE OR REPLACE, identify the executing role and required post-create owner because replacement can leave ownership with the creator.
5. Record one evidenced owner and the source rules; conflicting or absent evidence is a blocker.

## Benchmark case

Comparable governed production objects and current rules identify the required owner for a new dynamic table; conflicting evidence blocks the decision.

## Anti-patterns

- Expanding this Skill into an adjacent diagnosis, execution or verification job.
- Treating one inconsistent precedent or assumption as authority.
- Proceeding through an unresolved evidence or authority gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when one evidenced owner is identified; block when ownership rules or comparable evidence conflict.

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
