---
id: SKILL-0280
type: skill
title: BI Performance Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [skill, testing, bi, performance]
trigger_phrases: ["design BI performance tests", "test dashboard latency", "measure report interaction performance"]
---

# BI Performance Test Design

Design reproducible performance tests for BI loading, filtering and interaction.

## Intent-routing contract

This Skill owns BI performance test design only. Performance remediation, semantic correctness, controls, security and export testing are separate actions.

## When to use

Use when first-load, cached-load, filter, control, drill or other representative BI interaction latency must be measured.

## Method

1. Define representative users, data volumes, date ranges, filters, concurrency and acceptance thresholds.
2. Separate first-load, cached-load and individual interaction timings.
3. Use repeatable scenarios and record client, BI-platform and warehouse evidence where available.
4. Run enough repetitions to distinguish normal variation from a persistent regression.
5. Compare like-for-like source, cache and workload conditions.
6. Record correctness failures separately from latency results.

## Benchmark case

A sales dashboard is tested for cold first load, warm reload and store-filter response over the same date range, with repeatable timings and an agreed latency threshold.

Boundary design case: Representative timing scenarios exist but no latency target is agreed. Preserve the measurement design and target gap; do not invent a threshold or declare a pass from one timing observation.

## Anti-patterns

- Comparing cold and cached runs as equivalents.
- Timing different data scopes without disclosure.
- Reporting one run as representative performance.
- Optimising before confirming the result is correct.

## Stop

Stop when representative scenarios, controlled conditions, thresholds and repeatable measurements are defined well enough to produce a defensible verdict.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0280 | related_to | undirected | inherited_from_source_split | supports
