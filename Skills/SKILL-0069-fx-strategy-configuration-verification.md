---
id: SKILL-0069
type: skill
title: FX Strategy Configuration Verification
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [fx, configuration, trading-controls]
trigger_phrases: ["verify FX strategy configuration", "check current pair bands", "confirm session blocks and protections"]
---

# SKILL-0069 — FX Strategy Configuration Verification

## Purpose

Verify the current executable FX strategy configuration before another Skill relies on pair sets, thresholds, session blocks or protection settings.

## When to use

Use when asked to verify FX strategy configuration. Use when asked to check current pair bands. Use when asked to confirm session blocks and protections.

## Method

1. Read the current bot/configuration or canonical deployed record.
2. Capture pair universe, pair-specific bands, session/event blocks, grid limits, protections and version/date.
3. Compare cited historical values with current values and label discrepancies.
4. Return verified facts, unavailable fields and source provenance; make no parameter recommendation.

## Benchmark case

When an analysis cites historical JPY and non-JPY deviation bands, inspect the current configuration and state whether each value still applies before sizing or optimisation proceeds.

Boundary design case: a saved configuration differs from the executable instance and neither is established as deployed authority. Return both revisions and the exact discrepancy; do not choose the remembered value or supply downstream sizing as if configuration were verified.

## Anti-patterns

- Using remembered settings as current.
- Inferring configuration from historical performance.
- Filling missing settings with conventional defaults.

## Stop

Stop when the required settings are source-verified or explicitly recorded as gaps.
