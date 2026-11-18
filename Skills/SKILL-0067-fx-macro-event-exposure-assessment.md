---
id: SKILL-0067
type: skill
title: FX Macro-Event Exposure Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [fx, macro-events, event-risk, trading]
trigger_phrases: ["assess FX event exposure", "evaluate a news blackout window", "analyse central bank risk"]
---

# SKILL-0067 — FX Macro-Event Exposure Assessment

## Purpose

Assess portfolio exposure to scheduled and unscheduled macro events using current event data and tested strategy behaviour.

## When to use

Use when asked to assess FX event exposure. Use when asked to evaluate a news blackout window. Use when asked to analyse central bank risk.

## Method

1. Verify the current event calendar, policy expectations and configured event rules.
2. Map affected currencies, simultaneous pair exposure, liquidity/spread risk and relevant historical strategy outcomes.
3. If a blackout change is proposed, test multiple windows against missed opportunity, tail loss, depth and slippage.
4. Separate verified current facts from scenario assumptions and state the decision expiry.

## Benchmark case

Before a central-bank decision, map affected pair concentration and evaluate whether the configured block is supported without inventing a universal pre/post-event window.

Boundary design case: the event calendar is stale or the event time conflicts across sources. Preserve the conflict and block the timing-dependent blackout assessment until verified; do not infer a current event window from an earlier release or alter live controls.

## Anti-patterns

- Using a stale calendar.
- Applying a universal blackout duration.
- Changing parameters because a narrative sounds convincing.

## Stop

Stop with an evidenced exposure assessment or a test plan; do not alter live event controls without authorised evidence.
