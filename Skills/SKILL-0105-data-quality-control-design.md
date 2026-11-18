---
id: SKILL-0105
type: skill
title: Data Quality Control Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [data-quality, control-design]
trigger_phrases: ["design a data quality control", "create freshness and volume checks", "define reconciliation alerts"]
---

# SKILL-0105 — Data Quality Control Design

## Purpose

Design preventive or detective controls with predeclared thresholds, routing and retained evidence.

## When to use

Use for: design a data quality control; create freshness and volume checks; define reconciliation alerts.

## Method

1. Define the decision, grain, owner, material fields, freshness contract and normal exceptions.
2. Choose the discriminating check: freshness, volume, distinct/duplicate/null keys, orphans, sums or segmented reconciliation.
3. Set severity and threshold before incident results, or record later authorised change.
4. Define routing, suppression, retry/backfill, evidence retention and resolution test.
5. Test the control against representative normal and failure cases.

## Benchmark case

Design a daily source-to-landed volume control with weekday-aware bounds, last-source-data timestamp, severity, suppression and escalation owner.

Missing-input design case: a proposed volume alert has no accepted normal range or routing owner. Specify the check and unresolved threshold/owner decisions, then withhold activation; do not derive a convenient threshold from the incident being assessed or emit an unowned alert.

## Anti-patterns

- Moving thresholds after seeing an incident.
- Alerting without ownership.
- Using totals where segmented allocation matters.

## Stop

Stop with an implementable control contract and test evidence.
