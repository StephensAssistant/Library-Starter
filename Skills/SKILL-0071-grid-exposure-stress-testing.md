---
id: SKILL-0071
type: skill
title: Grid Exposure Stress Testing
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0001, SKILL-0004]
tags: [trading, grid-risk, stress-testing]
trigger_phrases: ["stress test a trading grid", "simulate grid stacking", "calculate tail margin usage"]
---

# SKILL-0071 — Grid Exposure Stress Testing

## Purpose

Simulate path-dependent grid exposure under normal, severe and tail scenarios.

## When to use

Use for: stress test a trading grid; simulate grid stacking; calculate tail margin usage.

## Method

1. Verify levels, spacing, direction, simultaneous sequences, pip value, protections and margin rules.
2. Define normal, severe and discontinuous tail paths before viewing results.
3. Calculate notional, positions, margin/free margin, unrealised and realised loss, and binding constraint in each scenario.
4. State assumptions, recovery conditions and gaps.


### Application checks

For each declared path, retain the ordered price/exposure states and show where an additional level, protection or broker constraint changes the result. Report the first binding constraint alongside notional, losses and free margin. Keep unverified gap fills and protection execution as assumptions; scenario arithmetic is not proof that the broker will execute a protection at its modelled price.

## Benchmark case

Stress several correlated grids through an adverse directional move, spread widening and a price gap, identifying when margin or protection constraints bind.

Missing-input design case: grid spacing is supplied but broker margin rules or configured protection behaviour are unverified. Identify which scenario consequences cannot be calculated and withhold the binding-constraint verdict; do not substitute conventional margin or assume a protection fills through a gap.

## Anti-patterns

- Modelling a grid as one entry.
- Using only the worst observed path.
- Inventing accepted stress thresholds.

## Stop

Stop with scenario consequences and the earliest binding constraint.
