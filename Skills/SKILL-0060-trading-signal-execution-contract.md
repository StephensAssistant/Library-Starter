---
id: SKILL-0060
type: skill
title: Trading Signal-to-Execution Contract
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal]
trigger_phrases: [trading signal execution, order decision contract, entry to order]
---

# Trading Signal-to-Execution Contract

Translate an approved trading signal into deterministic order decisions and managed position state.

## When to use

Use when defining or implementing the boundary from strategy signal through order placement and exit handling.

## Method

1. Confirm the strategy invariant, platform state and observable acceptance criteria relevant to this job.
2. Work only inside this capability boundary; route architecture, risk sizing and unrelated responsibilities to their owning Skills.
3. Preserve deterministic controls and record evidence for every material outcome.
4. Test the representative success, rejection and failure paths.
5. Compare the resulting object or trace with the declared expected behaviour.


### Application checks

For each signal, record its identity, direction and approved risk/order inputs; inspect current orders and positions before deciding entry or exit. Make the gate result and rejection reason explicit and map a submitted request to its acknowledgement, fill and managed position state. On uncertain submission, reconcile platform evidence before another request. Compare the trace with the approved single-signal outcome without changing entry rules, sizing authority or exit intent.

## Benchmark case

One qualifying signal creates one authorised order with traceable rejection reasons and no duplicate entry.

Failure design case: submission times out after a qualifying signal. Preserve signal/request identity and inspect platform order/position evidence before resubmitting; an unknown acknowledgement is neither a rejection nor permission to place a duplicate order.

## Anti-patterns

- Inferring live behaviour from a backtest alone.
- Changing strategy meaning while repairing implementation.
- Claiming success without reproducible evidence.

## Stop

Stop after the capability-specific outcome is evidenced, or the precise strategy, platform, data or authority gap.
