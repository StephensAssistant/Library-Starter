---
id: SKILL-0001
type: skill
title: Trading System Architecture
status: current
created: 2026-08-22
updated: 2026-10-31
owner: Library owner

links: [SKILL-0070, SKILL-0071, SKILL-0072, SKILL-0073, SKILL-0074]
tags: [skill, trading, system-architecture, personal]
trigger_phrases: [trading system architecture, trading bot architecture, trading system architecture]
source_skill: trading-system-design
migrated_from: SKILL-0001-old-library
---

# Trading System Architecture

Define component boundaries, state, control flow and non-negotiable invariants for an automated trading system. This Skill owns architecture only; platform implementation, execution, telemetry, testing, diagnosis and performance measurement use their independent Skills.

## When to use

Use when designing or materially restructuring a trading bot or automated strategy system.

## Method

1. Define signal, risk, execution, position-state, session-control and shutdown boundaries.
2. Specify authoritative state, event ordering and restart behaviour.
3. Separate deterministic risk controls from optional entry logic.
4. Make failure containment, observability and test seams explicit.
5. Preserve confirmed strategy invariants; label unported or unresolved behaviour.

## Benchmark case

A multi-symbol cBot is redesigned. A passing application isolates shared risk controls from symbol-specific signals and execution state, with deterministic restart and halt behaviour.

Missing-input design case: restart state has no agreed authority. Identify which component would restore it and leave that transition unresolved; do not invent a recovery ordering or claim an implementable architecture until the state owner resolves the gap.

## Anti-patterns

- Mixing architecture with platform syntax or tuning.
- Allowing entry logic to bypass risk controls.
- Treating backtest behaviour as live-platform proof.

## Stop

Stop after the component contract and invariants are explicit, or the precise strategy, state or authority gap.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0013--SKILL-0001 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0016--SKILL-0001 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0017--SKILL-0001 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: SKILL-0001--SKILL-0005 | related_to | undirected | authoritative_record | supports
