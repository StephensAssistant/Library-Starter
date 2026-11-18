---
id: SKILL-0053
type: skill
title: Sigma Serving-Layer Selection
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [PLAY-0012, PLAY-0018, SKILL-0002, SKILL-0046, SKILL-0047, SKILL-0048, SKILL-0049, SKILL-0050, SKILL-0263, SKILL-0264, SKILL-0265]
tags: [skill, sigma]
trigger_phrases: [sigma materialization, dynamic table vs view, sigma serving layer]
---

# Sigma Serving-Layer Selection

Assess Sigma serving options using measured workload evidence within the governing Snowflake reporting architecture.

## When to use

Use when deciding how a Sigma workbook should consume repeated or expensive transformations.

## Method

1. Hold logic, date range, filters, grain and warehouse conditions constant.
2. Prove row and metric parity before performance comparison.
3. Measure cold and warm executions plus refresh duration, credits and freshness.
4. Separate Snowflake refresh cost from Sigma consumption cost.
5. Apply AGENTS.md's reporting baseline: Snowflake facts/dimensions → Semantic View → per-report golden Dynamic Table → Sigma. Keep reusable modelling upstream. A golden view requires the Library owner's direction or an evidenced constraint; temporary testing and explicit front-end capabilities such as writeback retain their stated exceptions. Measurements support the compliant choice or an evidenced exception proposal; they do not authorise a different architecture.

## Benchmark case

A small and large report compare a view and Dynamic Table; the decision uses parity, repeated timings, refresh cost and perceived interaction speed.

Boundary design case: a tested view is faster but no authorised architecture exception is evidenced. Retain the measurements and report the exception decision separately; performance evidence alone does not replace the governing golden Dynamic Table baseline or establish an approved cutover.

## Anti-patterns

- Inventing Sigma capabilities, identifiers, schemas or successful evidence.
- Duplicating governed logic without a measured reason.
- Treating a syntactically accepted change as verified behaviour.

## Stop

Stop after the named outcome is read back and verified, or the precise capability, access, source or evidence gap.
