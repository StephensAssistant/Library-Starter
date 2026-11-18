---
id: SKILL-0070
type: skill
title: FX Portfolio Dependence Risk Measurement
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0001, SKILL-0004]
tags: [fx, portfolio-risk, dependence]
trigger_phrases: ["measure effective FX bets", "assess correlated portfolio risk", "calculate stressed dependence"]
---

# SKILL-0070 — FX Portfolio Dependence Risk Measurement

## Purpose

Quantify current and stressed dependence across an FX strategy before capital risk is sized.

## When to use

Use for: measure effective FX bets; assess correlated portfolio risk; calculate stressed dependence.

## Method

1. Verify current universe, weights and representative window.
2. Measure return dependence, factor/common-currency exposure and effective diversification.
3. Repeat in stressed periods and explicit shocks.
4. Return ranges, instability and sizing-relevant consequences.


### Application checks

Keep the current exposure weights and aligned return window attached to every estimate, and distinguish measured dependence from explicit shock assumptions. Return normal and stressed ranges with their source/window, affected exposures and implications for sizing. If weights or alignment are missing, identify that gap rather than issuing a point estimate suitable for capital allocation.

## Benchmark case

Show whether 28 active pairs behave like materially fewer independent bets and how that changes under a USD or risk-off shock.

Missing-input design case: the current weights are unavailable or return series cover incompatible periods. Identify the missing exposure/alignment evidence and withhold the sizing-ready dependence result; a historical effective-bet number or pair count cannot replace it.

## Anti-patterns

- Using pair count as diversification.
- Treating one historical PCA result as permanent.
- Ignoring direction and weights.

## Stop

Stop with current and stressed dependence evidence suitable for position sizing.
