---
id: SKILL-0068
type: skill
title: JPY Carry-Risk Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, fx, jpy, carry-risk]
trigger_phrases: ["assess JPY carry risk", "analyse JPY carry unwind", "review JPY funding risk"]
---

# JPY Carry-Risk Assessment

Assess JPY funding, carry positioning, liquidity and reversal risk for the current portfolio.

## Intent-routing contract

This Skill owns JPY carry-risk assessment only. Intervention-risk and aggregate JPY cross-concentration assessments are separate actions.

## When to use

Use when current JPY funding conditions, carry positioning, liquidity or a carry-unwind scenario must be assessed.

## Method

1. Verify the current JPY positions, direction, weights and relevant execution horizon.
2. Assess funding conditions, carry positioning, Japanese monetary policy, liquidity and reversal catalysts using current sources.
3. Test plausible carry-unwind scenarios against the current positions.
4. Use historical unwinds as stress evidence, not deterministic templates.
5. Report current catalysts, consequences, uncertainty and evidence timestamps.

## Benchmark case

Current short-JPY positions are tested against a sharp funding reversal and liquidity contraction, with exposure and uncertainty stated without assuming a historical unwind will repeat identically.

Missing-input design case: current JPY positions are verified but funding or policy evidence is unavailable. Separate the known portfolio from conditional unwind scenarios and identify the missing current facts; do not assert a present catalyst or import a historical unwind as a forecast.

## Anti-patterns

- Assuming past carry unwinds repeat identically.
- Relying on unverified policy or funding claims.
- Treating positive carry as evidence that reversal risk is low.
- Mixing intervention probability or cross-pair concentration into the carry assessment.

## Stop

Stop when current carry conditions, reversal catalysts, portfolio consequences and limitations are explicit.
