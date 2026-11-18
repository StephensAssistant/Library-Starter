---
id: SKILL-0064
type: skill
title: Trading Bot Performance Benchmarking
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal]
trigger_phrases: [trading bot performance, trading execution benchmark, cBot resource use]
---

# Trading Bot Performance Benchmarking

Measure trading-bot runtime, throughput and resource behaviour under representative market and symbol loads.

## When to use

Use when evaluating whether implementation performance could affect signals, execution or platform stability.

## Method

1. Confirm the strategy invariant, platform state and observable acceptance criteria relevant to this job.
2. Work only inside this capability boundary; route architecture, risk sizing and unrelated responsibilities to their owning Skills.
3. Preserve deterministic controls and record evidence for every material outcome.
4. Test the representative success, rejection and failure paths.
5. Compare the resulting object or trace with the declared expected behaviour.


### Application checks

Fix the bot/configuration version, symbol set, event load, environment and observation window for comparison. Measure event latency, order-processing time and resource use under the same representative conditions, recording failures and throughput as well as timings. Check that signal/order traces still meet the strategy contract. Report comparable before/after evidence and remaining load limits; runtime efficiency alone says nothing about trading profitability or live execution correctness.

## Benchmark case

A multi-symbol benchmark reports event latency, order-processing time and resource use under a declared load.

Boundary design case: the revised bot is timed on fewer symbols or a different event load. Report the runs as incomparable until a representative common workload is available; do not claim a speedup or infer trading profitability from resource measurements.

## Anti-patterns

- Inferring live behaviour from a backtest alone.
- Changing strategy meaning while repairing implementation.
- Claiming success without reproducible evidence.

## Stop

Stop after the capability-specific outcome is evidenced, or the precise strategy, platform, data or authority gap.
