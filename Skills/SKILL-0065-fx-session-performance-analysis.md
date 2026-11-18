---
id: SKILL-0065
type: skill
title: FX Session Performance Analysis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [fx, session-analysis, trading]
trigger_phrases: ["compare FX session performance", "analyse entries by trading session", "assess session risk"]
---

# SKILL-0065 — FX Session Performance Analysis

## Purpose

Measure how the active strategy behaves across Asia, London, New York and overlap periods without assigning fixed quality labels.

## When to use

Use when asked to compare FX session performance. Use when asked to analyse entries by trading session. Use when asked to assess session risk.

## Method

1. Confirm the current session definitions and analysis window.
2. Measure entry frequency, completion duration, adverse excursion, sequence depth, spread, slippage and realised P&L by session.
3. Compare each session with a representative baseline and separate time-of-day effects from regime and event effects.
4. State evidence, uncertainty and any testable session-policy hypothesis; do not change live blocks without validation.

## Benchmark case

Given trade and sequence data spanning several regimes, compare session outcomes on like-for-like measures and show whether a suspected weak session remains weak after controlling for regime and costs.

Missing-input design case: trade timestamps lack the timezone needed for session assignment. Identify the timezone gap and withhold session attribution for those records; do not assign a conventional timezone or infer a weak session from a biased partial population.

## Anti-patterns

- Calling Asia inherently favourable or an overlap inherently harmful.
- Changing a session block from conventional market lore.
- Comparing unequal periods without stating the bias.

## Stop

Stop with an evidenced session comparison and a falsifiable next test, or record that the data cannot isolate a session effect.
