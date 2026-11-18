---
id: SKILL-0066
type: skill
title: FX Factor-Concentration Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, fx, factor-risk, concentration, trading]
trigger_phrases: ["measure FX portfolio concentration", "identify common currency exposure", "assess FX factor concentration"]
---

# FX Factor-Concentration Assessment

Measure whether nominally different FX positions collapse into shared currency or macro-factor exposure.

## Intent-routing contract

This Skill owns portfolio factor-concentration assessment only. Pair-correlation measurement is a separate action.

## When to use

Use when current FX positions must be aggregated into common-currency or macro-factor exposures and effective diversification assessed.

## Method

1. Set the current pair universe, position direction, weights and analysis window.
2. Normalize common-currency exposure across base and quote directions.
3. Use factor or PCA analysis when it materially improves discrimination beyond direct currency exposure.
4. Repeat under stressed periods or direct scenario shocks.
5. Report dominant factors, effective diversification, unstable exposures, consequences and limitations without converting historical estimates into constants.

## Benchmark case

A 28-pair portfolio is normalized to reveal whether several positions represent one USD, JPY or risk-sentiment bet and how concentration changes under stress.

Missing-input design case: pair names are known but position directions or weights are absent. Report that current common-currency concentration cannot be calculated; nominal pair count and a historical PCA estimate cannot supply the missing signed exposure.

## Anti-patterns

- Treating pair count as independent diversification.
- Hard-coding an old effective-bet estimate.
- Treating pair correlation alone as factor attribution.
- Ignoring position direction and weight.

## Stop

Stop when current and stressed common-currency or macro-factor concentration, effective diversification and limitations are explicit.
