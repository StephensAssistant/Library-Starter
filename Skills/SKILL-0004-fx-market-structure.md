---
id: SKILL-0004
type: skill
title: FX Regime Classification
status: current
created: 2026-08-22
updated: 2026-10-31
links: [SKILL-0070, SKILL-0071, SKILL-0072, SKILL-0073, SKILL-0074]
tags: [fx, regime-classification, mean-reversion, trading]
trigger_phrases: ["classify the FX regime", "what is the current FX regime", "range or trend", "is this market reverting", "volatility regime"]
source_skill: fx-market-structure
migrated_from: SKILL-0004-old-library
---

# SKILL-0004 — FX Regime Classification

## Purpose

Classify the current FX environment as range/reverting, directional/trending, volatility shock/gap, or mixed/transition using current observable evidence relevant to the strategy.

## When to use

Use when a trading decision needs an evidenced current-regime label. Verify current data; historical behaviour is comparison evidence, not current state.

## Method

1. Set the analysis window and representative baseline.
2. Measure realised volatility relative to its own history, directional persistence, deviation reversion, sequence depth, adverse excursion, completion duration, spreads and liquidity.
3. Classify:
   - **Range/reverting:** deviations revert promptly and exposure remains contained.
   - **Directional/trending:** positions accumulate one way and completion lengthens.
   - **Shock/gap:** rapid displacement can stack exposure before reversion.
   - **Mixed/transition:** reversion continues but dispersion, duration or direction is unstable.
4. State the evidence, conflicting indicators, confidence and expiry condition.
5. Keep implementation defects separate: one-sided signals, order asymmetry or exit errors are not regime evidence.

## Benchmark case

Given four weeks of current pair returns, deviations, sequence depth and spreads, classify the regime from multiple discriminating measures, compare it with a representative baseline, and avoid declaring a software asymmetry to be a market regime.

Missing-input design case: current pair data is unavailable while historical returns are accessible. Return the current-data gap and any separately labelled historical comparison; do not infer a present regime or recycle a historical confidence label.

## Anti-patterns

- Assigning a regime from one fixed threshold.
- Treating a historical statistic as permanent.
- Using a macro story without measured strategy behaviour.
- Explaining an execution defect as market structure.

## Stop

Stop when the regime is evidence-labelled with confidence and limitations, or when current data is unavailable. Route session, factor, event, JPY and configuration work to their action-specific Skills.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0016--SKILL-0004 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: SKILL-0004--SKILL-0005 | related_to | undirected | authoritative_record | supports
