---
id: SKILL-0059
type: skill
title: cTrader Lifecycle-Callback Engineering
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal, ctrader, lifecycle]
trigger_phrases: ["cBot lifecycle", "cTrader callback", "OnStart OnTick OnBar OnStop"]
---

# cTrader Lifecycle-Callback Engineering

Implement cTrader/cAlgo lifecycle callbacks and state transitions without changing strategy intent.

## When to use

Use when structuring or repairing cBot startup, event callbacks, state restoration, shutdown and callback ordering. Route API operations, symbol handling and platform-constraint verification to their focused Skills.

## Method

1. Define the state each callback may read, initialise, mutate and release.
2. Initialise dependencies and restore validated persistent state during startup before trading callbacks can use them.
3. Keep tick, bar, timer, position and error callbacks bounded to their documented event responsibilities.
4. Make repeated or reordered events safe where the platform may legitimately deliver them.
5. Prevent duplicate subscriptions, repeated initialisation and duplicate strategy state.
6. Release resources and persist only valid state during shutdown.
7. Trace callback order, state transitions and material failures for verification.

## Benchmark case

A multi-symbol cBot starts once, restores valid state, subscribes once, processes platform events without duplicating strategy state and shuts down cleanly.

Boundary design case: restored state has an unknown version or cannot be validated against the callback contract. Keep dependent trading callbacks from using it and report the restoration gap; do not initialise a guessed position state or claim restart safety from a backtest.

## Anti-patterns

- Initialising required state lazily after trading callbacks begin
- Duplicating subscriptions or strategy state
- Assuming one callback order without evidence
- Changing strategy meaning while repairing lifecycle code
- Claiming live behaviour from a backtest alone

## Stop

Stop when startup, callback transitions and shutdown are reproducibly evidenced, or when the required lifecycle contract or platform context is unresolved.
