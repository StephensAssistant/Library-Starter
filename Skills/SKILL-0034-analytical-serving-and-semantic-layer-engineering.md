---
id: SKILL-0034
type: skill
title: Analytical Serving-Layer Change Implementation
status: current
created: 2026-09-16
updated: 2026-10-24
links: []
tags: [skill, serving-layer, dynamic-tables, materialization]
trigger_phrases: ["implement approved serving-layer change", "cut over analytical materialization", "replace view with approved dynamic table"]
---

# Analytical Serving-Layer Change Implementation

Implement and cut over one already-approved analytical serving-layer physicalization change.

## When to use

Use only after SKILL-0098 has selected and approved the target live view, persisted table, Dynamic Table or semantic materialisation. This Skill does not choose the physicalization pattern.

## Intent-routing contract

This Skill owns implementation and cutover of an approved serving-layer change. Pattern comparison, ranking and selection belong to SKILL-0098.

## Method

1. Confirm the approved source and target patterns, grain, freshness, ownership, security, acceptance evidence and rollback boundary.
2. Implement the target object with governed logic, required grants, ownership, refresh behavior and monitoring.
3. Prove row, key and metric parity before consumer cutover.
4. Cut over the named consumers, verify effective access, freshness, cost and latency, and retain the agreed recovery path.
5. Record evidence, exceptions and the reassessment trigger without reopening the approved selection.

## Evidence expected

Retain the approved decision, implementation changes, parity checks, cutover result, operational checks and unresolved gap.

## Benchmark case

After SKILL-0098 approves a Dynamic Table, a passing application creates it with correct ownership and refresh behavior, proves parity with the view, cuts over the named BI consumer and verifies access and freshness.

## Anti-patterns

- Choosing or re-ranking physicalization patterns inside this Skill.
- Cutting over before parity, grants and refresh behavior are proven.
- Treating object creation as verified consumer adoption.

## Stop

Stop after the approved target is implemented, cut over and operationally verified, or when the approval, parity, access, ownership, refresh or rollback contract is unresolved.

## Contextual links

- `SKILL-0222` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0223` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0224` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0225` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0226` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0227` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 6 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
