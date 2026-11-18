---
id: SKILL-0061
type: skill
title: Trading System Telemetry
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal]
trigger_phrases: [trading bot telemetry, signal export, trading observability]
---

# Trading System Telemetry

Instrument trading decisions, risk gates, orders, positions and failures so behaviour can be reconstructed.

## When to use

Use when adding logs, counters, signal exports or diagnostic state to a trading system.

## Method

1. Confirm the strategy invariant, platform state and observable acceptance criteria relevant to this job.
2. Work only inside this capability boundary; route architecture, risk sizing and unrelated responsibilities to their owning Skills.
3. Preserve deterministic controls and record evidence for every material outcome.
4. Test the representative success, rejection and failure paths.
5. Compare the resulting object or trace with the declared expected behaviour.


### Application checks

Choose fields that connect one signal to its risk-gate outcome, request, acknowledgement, fill, position and exit. Include symbol, direction, volume and timestamps with the applicable configuration identity so another check can reconstruct a skipped or executed trade. Distinguish “not observed” from “did not happen”. Verify instrumentation against a known accepted, rejected and failed path without allowing logging to alter the deterministic decision or become the sole proof of platform execution.

## Benchmark case

A skipped trade can be reconstructed from signal, gate, spread, session and order-state evidence.

Boundary design case: an order rejection lacks the signal identifier or gate result needed to reconstruct the decision. Report the broken trace boundary and add only the missing instrumentation; absence from the log does not prove the signal never occurred.

## Anti-patterns

- Inferring live behaviour from a backtest alone.
- Changing strategy meaning while repairing implementation.
- Claiming success without reproducible evidence.

## Stop

Stop after the capability-specific outcome is evidenced, or the precise strategy, platform, data or authority gap.
