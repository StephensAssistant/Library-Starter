---
id: SKILL-0074
type: skill
title: Trading Risk Telemetry Reconciliation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0001, SKILL-0004]
tags: [trading, telemetry, execution-reconciliation]
trigger_phrases: ["reconcile trading execution telemetry", "trace risk fields through an order", "check signal to exit consistency"]
---

# SKILL-0074 — Trading Risk Telemetry Reconciliation

## Purpose

Prove that direction, volume, stops, targets, symbol and timestamps remain consistent from signal through exit.

## When to use

Use for: reconcile trading execution telemetry; trace risk fields through an order; check signal to exit consistency.

## Method

1. Select one canonical signal and capture signal log, marker, order request, fill and close/TP/SL evidence.
2. Normalize identifiers and timestamps.
3. Compare direction, volume, stop/target distance, symbol and event sequence at each boundary.
4. Classify the earliest divergence as execution defect or confirmed behaviour.

## Benchmark case

Trace both a long and short signal and identify a missing short order as an execution defect rather than evidence for lower strategy risk.

Missing-input design case: a fill cannot be matched to its canonical signal after identifier/timezone normalization. Mark that boundary unresolved and request the missing trace evidence; do not infer direction consistency, an execution defect, or reduced risk from the unmatched chain.

## Anti-patterns

- Using chart appearance alone.
- Treating one-sided execution as market evidence.
- Sizing from telemetry that has not been reconciled.

## Stop

Stop when the chain reconciles or the earliest execution divergence is isolated.
