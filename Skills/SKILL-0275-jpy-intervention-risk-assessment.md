---
id: SKILL-0275
type: skill
title: JPY Intervention Risk Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, fx, jpy, intervention-risk]
trigger_phrases: ["assess JPY intervention risk", "analyse Japanese FX intervention exposure", "check JPY intervention conditions"]
---

# JPY Intervention Risk Assessment

Assess current Japanese FX-intervention conditions and the portfolio consequences of an intervention scenario.

## Intent-routing contract

This Skill owns JPY intervention-risk assessment only. Carry/funding risk and aggregate JPY cross-concentration are separate actions.

## When to use

Use when current Japanese policy, official intervention signals, liquidity conditions or portfolio exposure to an intervention require assessment.

## Method

1. Verify the current JPY positions, direction, weights and relevant execution horizon.
2. Research current Japanese policy, official statements, intervention conditions and liquidity using authoritative current sources.
3. Separate verified signals from commentary and historical analogy.
4. Model plausible intervention scenarios against the current positions without treating a past episode as deterministic.
5. Report catalysts, exposure, consequences, uncertainty and the evidence timestamp.

## Benchmark case

Several short-JPY positions are assessed against current official signals and a sharp intervention scenario; the result identifies portfolio impact without claiming intervention timing is predictable.

Boundary design case: Current official signals are available but the position inventory is stale. Report policy evidence separately and leave portfolio consequences provisional; do not guess direction, size or intervention timing.

## Anti-patterns

- Treating a historical intervention as a repeatable template.
- Relying on unverified policy claims.
- Converting intervention risk into a certain forecast.
- Ignoring position direction when estimating impact.

## Stop

Stop when current intervention evidence, exposed positions, scenario consequences and uncertainty are explicit.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0016--SKILL-0275 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0275 | related_to | undirected | inherited_from_source_split | supports
