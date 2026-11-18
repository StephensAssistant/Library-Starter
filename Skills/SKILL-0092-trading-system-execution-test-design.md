---
id: SKILL-0092
type: skill
title: Trading-System Execution Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [testing, trading-system]
trigger_phrases: ["design cBot tests", "test long and short execution", "validate signal to exit chain"]
---

# SKILL-0092 — Trading-System Execution Test Design

## Purpose

Design tests that prove a trading signal remains consistent through visual, order, fill and exit behaviour.

## When to use

Use for: design cBot tests; test long and short execution; validate signal to exit chain.

## Method

1. Select canonical long and short cases.
2. Trace signal log, marker, order request, fill and TP/SL/exit.
3. Test rejection, error and protection paths.
4. Use forward tests for runtime behaviour backtests cannot establish.
5. Compare signal counts and directions, not chart appearance alone.

## Benchmark case

Design separate long and short cases that expose a system producing both signals but only one order direction.

Boundary design case: both signal directions are present but only long orders are requested. Expect the execution-chain case to fail at the short request boundary; do not use overall backtest profit or chart markers to override the missing directional contract evidence.

## Anti-patterns

- Using backtest profit as execution proof.
- Testing one direction.
- Loosening filters before instrumenting no-trade decisions.

## Stop

Stop with execution-chain cases and expected boundary evidence.
