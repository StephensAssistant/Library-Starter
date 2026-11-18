---
id: SKILL-0276
type: skill
title: JPY Cross-Concentration Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, fx, jpy, concentration-risk]
trigger_phrases: ["review JPY pair concentration", "aggregate JPY cross exposure", "measure JPY portfolio concentration"]
---

# JPY Cross-Concentration Assessment

Normalize and aggregate JPY exposure across every portfolio cross so nominal pair count is not mistaken for diversification.

## Intent-routing contract

This Skill owns JPY cross-concentration measurement only. Carry/funding and intervention-risk assessments are separate actions.

## When to use

Use when multiple JPY pairs must be converted into one comparable exposure and concentration view.

## Method

1. Verify every current JPY pair, quote direction, position direction, size and weighting basis.
2. Normalize each position into a consistent JPY-factor direction and magnitude.
3. Aggregate gross, net and material clustered exposure across all JPY crosses.
4. Compare nominal pair diversification with effective JPY exposure.
5. Report concentration, assumptions and any missing position or conversion evidence.

## Output evidence

Retain the position snapshot time, declared weighting/conversion basis and per-position normalized contribution with gross/net aggregates. Missing position or conversion evidence makes the affected aggregate incomplete rather than a zero exposure.

## Benchmark case

Mixed long and short positions across several JPY crosses are normalized into one JPY factor view, revealing whether the portfolio represents diversified trades or one concentrated JPY bet.

Boundary design case: One JPY cross has unknown quote direction or size. Do not omit a position silently: identify the missing contribution and withhold a complete aggregate-concentration claim.

## Anti-patterns

- Treating each JPY cross as independent diversification.
- Aggregating without normalizing quote and position direction.
- Using stale positions or guessed weights.
- Mixing intervention probability into the concentration calculation.

## Stop

Stop when normalized gross and net JPY exposure, effective concentration and limitations are explicit.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0016--SKILL-0276 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0276 | related_to | undirected | inherited_from_source_split | supports
