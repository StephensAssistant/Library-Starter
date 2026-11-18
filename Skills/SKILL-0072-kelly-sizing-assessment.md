---
id: SKILL-0072
type: skill
title: Kelly Sizing Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0001, SKILL-0004]
tags: [trading, kelly, growth-sizing]
trigger_phrases: ["calculate Kelly sizing", "assess fractional Kelly", "estimate growth-optimal risk"]
---

# SKILL-0072 — Kelly Sizing Assessment

## Purpose

Estimate Kelly only as an uncertainty-bounded growth reference for a correlated, path-dependent strategy.

## When to use

Use for: calculate Kelly sizing; assess fractional Kelly; estimate growth-optimal risk.

## Method

1. Build a representative distribution of completed strategy outcomes including costs and tails.
2. Estimate edge and payoff with sensitivity to plausible error.
3. Calculate full and fractional Kelly references.
4. Compare them with survivability, drawdown and margin constraints; do not promote Kelly directly to live size.


### Application checks

State the completed-outcome population, cost/tail treatment and assumptions used by the Kelly calculation. Vary uncertain edge and payoff inputs and retain the resulting reference range alongside the independent survivability constraints. If a representative strategy-outcome distribution cannot be established, return that evidence gap rather than inferring a growth-optimal allocation from isolated tickets.

## Benchmark case

Given uncertain win-rate and payoff estimates, show how full and fractional Kelly change across sensitivity bounds and why the survivable size may be lower.

Boundary design case: the sample contains individual tickets from unfinished grids rather than completed strategy outcomes. Report the distribution gap and withhold the Kelly reference; do not treat those dependent tickets as independent completed wins and losses or prescribe a live size.

## Anti-patterns

- Using isolated tickets instead of strategy outcomes.
- Ignoring correlation, path dependence or tail losses.
- Presenting Kelly as an exact live prescription.

## Stop

Stop with a bounded reference range, sensitivity table and explicit non-Kelly constraints.
