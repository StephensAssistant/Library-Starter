---
id: SKILL-0098
type: skill
title: Analytical Physicalization Pattern Selection
status: current
created: 2026-09-20
updated: 2026-10-31
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047]
tags: [data-modelling, serving-layer]
trigger_phrases: ["choose analytical physicalization pattern", "select view table or dynamic table", "compare BI materialisation options"]
---

# SKILL-0098 — Analytical Physicalization Pattern Selection

## Purpose

Choose a live view, persisted table, Dynamic Table or semantic materialisation from measured workload and governance evidence.

## Intent-routing contract

This Skill owns comparison, ranking and selection of the physicalization pattern. Implementing or cutting over an approved selection belongs to SKILL-0034.

## When to use

Use when the target physicalization has not yet been chosen and evidence must decide between live view, persisted table, Dynamic Table or semantic materialisation.

## Method

1. Confirm grain, reuse, freshness, ownership, security and consumer interaction. Apply the governing architecture before ranking: Snowflake-backed reporting uses facts/dimensions → Semantic View → per-report golden dynamic table. A golden view requires the Library owner's direction or an evidenced constraint; the initial source-only Qlik migration retains its explicit exception. Compare alternatives only within that authorised boundary.
2. Measure representative query cost, latency and transformation repetition.
3. Estimate refresh compute, storage and operational recovery for persisted options.
4. Verify platform constraints and actual refresh behaviour.
5. Rank options by total cost, latency, freshness and operability; recommend one and state the reassessment trigger.

## Benchmark case

A complex reused Snowflake view and Dynamic Table are compared using representative query history, refresh history, governance and required freshness; one pattern is approved before SKILL-0034 implements it.

Missing-input design case: candidate options have timings but no verified freshness or ownership requirement. Record which rankings depend on those gaps and withhold selection; a fast query cannot establish compliant refresh behaviour, operating ownership or an architecture exception.

## Anti-patterns

- Implementing or cutting over the selected object inside this Skill.
- Materialising every transform.
- Assuming Dynamic Tables always refresh incrementally.
- Claiming cost savings without comparable evidence.

## Stop

Stop with one ranked physicalization decision, its evidence and change conditions, or when a missing workload, governance or platform fact prevents selection.
