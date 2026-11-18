---
id: SKILL-0062
type: skill
title: Trading Forward-Test Validation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal]
trigger_phrases: [forward test trading bot, backtest vs forward test, paper trading validation]
---

# Trading Forward-Test Validation

Validate an automated strategy through controlled forward testing without treating backtests as live proof.

## When to use

Use when moving a bot from historical testing toward demo or constrained live evaluation.

## Method

1. Confirm the strategy invariant, platform state and observable acceptance criteria relevant to this job.
2. Work only inside this capability boundary; route architecture, risk sizing and unrelated responsibilities to their owning Skills.
3. Preserve deterministic controls and record evidence for every material outcome.
4. Test the representative success, rejection and failure paths.
5. Compare the resulting object or trace with the declared expected behaviour.


### Application checks

Pin the executable configuration, environment and approved test scope before collecting observations. Compare expected signals with actual requests, fills, spread/slippage, timing, protection and exits over the declared window. Separate a strategy-rule deviation from a platform/execution discrepancy and retain uncovered conditions. Return criterion-by-criterion evidence and unexercised paths; moving from demo to constrained live evaluation requires its own existing authority, not a profitable test result.

## Benchmark case

A forward test records expected signals, fills, spread, timing and risk behaviour against declared acceptance criteria.

Missing-input design case: forward fills are recorded but the tested configuration revision is unknown. Retain those observations with the configuration gap and withhold a strategy-validation verdict; a profitable sample or an older backtest cannot establish which runtime behaviour was exercised.

## Anti-patterns

- Inferring live behaviour from a backtest alone.
- Changing strategy meaning while repairing implementation.
- Claiming success without reproducible evidence.

## Stop

Stop after the capability-specific outcome is evidenced, or the precise strategy, platform, data or authority gap.
