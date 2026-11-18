---
id: SKILL-0272
type: skill
title: cTrader API Integration
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal, ctrader, api]
trigger_phrases: ["integrate cTrader API", "call cTrader Automate API", "cAlgo API interaction"]
---

# cTrader API Integration

Implement one bounded interaction with the cTrader Automate API without changing strategy intent.

## When to use

Use when a cBot must read platform state or call a documented trading, position, order, account, storage, chart or market-data API.

## Method

1. Define the required API operation, inputs, output and failure behaviour.
2. Verify the current cTrader API member, signature, availability and returned units before coding.
3. Keep strategy decisions and risk policy outside the integration boundary.
4. Handle rejected, unavailable, null and asynchronous outcomes explicitly. If a state-changing request times out or its outcome is unknown, reconcile the actual order, position or account state through the documented correlation mechanism before retry; do not submit a duplicate or change strategy/risk policy to recover.
5. Record the request, platform response and observable state change needed for verification.
6. Test one success path and each material rejection or service-failure path.

## Benchmark case

A cBot submits a bounded order request, records the returned result, and handles platform rejection without assuming execution or altering the strategy signal.

Boundary design case: An asynchronous order request times out without a confirmed result. Reconcile the correlated order/position state before retry; lack of a response is not proof that no order executed.

## Anti-patterns

- Coding from remembered API signatures
- Treating submission as execution
- Hiding platform errors behind a successful method return
- Moving strategy policy into API adapter code

## Stop

Stop when the documented API interaction and its failure paths are evidenced, or when the current API contract is unavailable or ambiguous.

