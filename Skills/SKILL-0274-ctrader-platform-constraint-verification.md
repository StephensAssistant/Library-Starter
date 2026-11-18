---
id: SKILL-0274
type: skill
title: cTrader Platform-Constraint Verification
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, trading, personal, ctrader, constraints]
trigger_phrases: ["verify cTrader constraint", "cBot platform limitation", "backtest versus live cTrader"]
---

# cTrader Platform-Constraint Verification

Verify whether a required behaviour is supported in the intended cTrader runtime and execution context.

## When to use

Use before relying on a platform feature, callback, permission, threading behaviour, data source or live/backtest equivalence.

## Method

1. State the required behaviour and target context: live, demo, backtest, optimisation or cloud execution.
2. Check current authoritative platform documentation for availability, permissions and lifecycle/thread restrictions.
3. Build the smallest reproducible probe when documentation does not prove behaviour.
4. Record platform version, context, inputs, trace and observed result.
5. Distinguish unsupported behaviour from missing permission, unavailable data and code defects.
6. Keep unverified assumptions out of production acceptance criteria.

## Benchmark case

A file-access feature works locally but not in cloud execution; the constraint is reproduced and documented before architecture depends on it.

Boundary design case: Cloud execution is the target but only a local probe is available. Report local observations and the unresolved cloud behaviour; a probe must stay within authorised effects and cannot supply a live trading or production permission.

## Anti-patterns

- Assuming backtest behaviour proves live support
- Generalising one runtime result to every execution context
- Treating missing permission as an API defect
- Claiming a constraint without documentation or a reproducible probe

## Stop

Stop with an evidenced supported, unsupported or context-dependent result, or when the platform version/context cannot be established.
