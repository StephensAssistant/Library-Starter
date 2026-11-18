---
id: SKILL-0056
type: skill
title: Sigma Workbook Formula Implementation
status: current
created: 2026-09-20
updated: 2026-09-20
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265]
tags: [skill, sigma]
trigger_phrases: [implement sigma workbook formula, relocate sigma workbook formula, sigma presentation calculation]
---

# Sigma Workbook Formula Implementation

Implement or relocate an already-placed workbook-specific calculation within Sigma.

## When to use

Use only when the governed layer decision is already established and the requested action is implementing or relocating a metric, calculated column, comparison or display formula within a Sigma workbook. Use SKILL-0223 when selecting the governed layer for reusable analytical logic or metrics.

## Intent-routing contract

Activate only for Sigma workbook-formula implementation or relocation. Cross-layer metric-placement and canonical KPI-layer decisions belong to SKILL-0223.

## Method

1. Confirm the signed-off business definition, evaluation grain and established calculation layer.
2. Reuse the governed Snowflake metric when the placement decision says it is canonical upstream.
3. Implement transparent workbook-specific presentation calculations in the correct Sigma parent or element.
4. Relocate duplicated Sigma presentation logic to the agreed shared workbook level without changing its business definition.
5. Reconcile outputs across filters, totals, nulls and boundary periods.

## Benchmark case

Net Sales Mix and variance have an agreed Sigma presentation-layer placement; a passing application implements them once at the correct workbook level and reconciles row, subtotal and grand-total results.

## Anti-patterns

- Choosing the governed metric layer inside this Skill.
- Moving reusable or cross-tool business logic between Sigma and Snowflake without SKILL-0223's placement decision.
- Inventing Sigma capabilities, identifiers, schemas or successful evidence.
- Duplicating governed logic without a measured reason.
- Treating a syntactically accepted change as verified behaviour.

## Stop

Stop after the requested Sigma formula is read back and reconciled, or when the governed placement, capability, access, source or evidence is unresolved. Route an unresolved cross-layer placement decision to SKILL-0223.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0056--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0056--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0056--SKILL-0265 | related_to | undirected | user_confirmed | supports
