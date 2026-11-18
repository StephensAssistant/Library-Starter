---
id: SKILL-0106
type: skill
title: Data Quality Root-Cause Classification
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [data-quality, root-cause]
trigger_phrases: ["classify a data quality root cause", "identify the cause of a data anomaly", "categorise the earliest data failure"]
---

# SKILL-0106 — Data Quality Root-Cause Classification

## Purpose

Assign an evidence-backed root-cause class after the earliest failing boundary is known.

## When to use

Use for: classify a data quality root cause; identify the cause of a data anomaly; categorise the earliest data failure.

## Method

1. Take the earliest divergence and exclude earlier boundaries with evidence.
2. Test candidate classes: source absence/volume, extraction/auth/scope, timing/window, ingestion, mapping, grain/join, transformation, reference data, presentation or expectation.
3. Rank up to three plausible causes with confidence and one discriminating check each.
4. Assign a confirmed class only when direct evidence reaches the required confidence; otherwise return provisional classification.
5. Record correction owner and preventive opportunity.

## Benchmark case

Given correct source and landing populations but doubled totals after a join, classify grain/join failure and identify the duplicate-key evidence.

Missing-input design case: the final report differs but no earliest failing boundary is established. Return a provisional class and the next boundary-discriminating check; do not confirm a transformation cause from the symptom or invent a confidence threshold absent from the governing criterion.

## Anti-patterns

- Classifying from symptoms alone.
- Calling every zero-row outcome pipeline failure.
- Presenting a hypothesis as confirmed cause.

## Stop

Stop with confirmed or provisional cause, evidence and next discriminating action.
