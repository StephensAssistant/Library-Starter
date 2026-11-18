---
id: SKILL-0052
type: skill
title: Sigma Performance Diagnostics
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265]
tags: [skill, sigma]
trigger_phrases: [sigma workbook performance, slow sigma dashboard, sigma query diagnostics]
---

# Sigma Performance Diagnostics

Diagnose where Sigma interaction latency originates across workbook lineage and Snowflake execution.

## When to use

Use when page load, control response or element interaction is slow or inconsistent.

## Method

1. Reproduce the user-visible delay with representative filters and cache state.
2. Trace parent/child lineage, repeated transformations, relationships and control scope.
3. Use query history to separate queue, compilation, execution, scanning and refresh costs.
4. Check fan-out, repeated formulas, unused columns and duplicated expensive work.
5. Validate that the chosen change improves both backend evidence and user response.

## Benchmark case

A date filter is slow; the diagnosis identifies repeated upstream transformation, removes duplication and proves improved query and interaction times.

Missing-input design case: query history is available but the slow user interaction cannot be reproduced under comparable filters or cache conditions. Report the backend observations and reproduction gap separately; do not claim an interaction improvement from an isolated fast warehouse query.

## Anti-patterns

- Inventing Sigma capabilities, identifiers, schemas or successful evidence.
- Duplicating governed logic without a measured reason.
- Treating a syntactically accepted change as verified behaviour.

## Stop

Stop after the named outcome is read back and verified, or the precise capability, access, source or evidence gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0052--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0052--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0052--SKILL-0265 | related_to | undirected | user_confirmed | supports
