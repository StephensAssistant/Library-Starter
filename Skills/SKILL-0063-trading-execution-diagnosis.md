---
id: SKILL-0063
type: skill
title: Trading Execution Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal]
trigger_phrases: [one sided trading, missing buy trade, trading bot diagnosis]
---

# Trading Execution Diagnosis

Diagnose asymmetric, missing or duplicated trade execution from evidence across signals, gates and platform state.

## When to use

Use when a bot buys but does not sell, skips valid entries or behaves differently by symbol or direction.

## Method

1. Confirm the strategy invariant, platform state and observable acceptance criteria relevant to this job.
2. Work only inside this capability boundary; route architecture, risk sizing and unrelated responsibilities to their owning Skills.
3. Preserve deterministic controls and record evidence for every material outcome.
4. Test the representative success, rejection and failure paths.
5. Compare the resulting object or trace with the declared expected behaviour.


### Application checks

Trace the affected signal through eligibility, risk/session/spread gates, order request, acknowledgement and position state. Compare long/short or symbol paths under matched conditions and isolate the first expected event missing or changed. If the signal did not qualify, retain that finding instead of repairing execution. Return the failing boundary, direct evidence and smallest discriminating next check before proposing a causal implementation fix.

## Benchmark case

A sell-side failure is isolated to one gate with trace evidence and a reproducible case before repair.

Near-miss design case: the short signal never qualified under the verified strategy rule. Report the no-signal boundary instead of repairing the sell-order path or loosening entry controls; a lack of orders alone does not prove execution asymmetry.

## Anti-patterns

- Inferring live behaviour from a backtest alone.
- Changing strategy meaning while repairing implementation.
- Claiming success without reproducible evidence.

## Stop

Stop after the capability-specific outcome is evidenced, or the precise strategy, platform, data or authority gap.
