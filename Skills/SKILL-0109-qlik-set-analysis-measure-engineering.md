---
id: SKILL-0109
type: skill
title: Qlik Set-Analysis Expression Engineering
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["Qlik set analysis", "engineer Qlik expression", "Qlik Aggr expression"]
links: []
tags: [qlik, set-analysis, expression-engineering]
---

# Qlik Set-Analysis Expression Engineering

Construct or change a Qlik set-analysis or nested aggregation expression against explicit selection and grain contracts.

## Intent routing contract

Activate only for Qlik set analysis, engineer Qlik expression, Qlik Aggr expression or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to construct or change a Qlik set-analysis or nested aggregation expression against explicit selection and grain contracts.

## Method

1. State the accepted metric definition, expression grain and expected selection behaviour.
2. List every field, modifier, retained/ignored selection and nested aggregation before authoring.
3. Build from verified inner aggregations outward; keep modifier values, quoting, dates, nulls, case and alternate state explicit.
4. Reconcile the final numeric result and representative edge populations against the accepted baseline.

## Decision and evidence details

Before accepting the expression, retain the exact expression, field population, selected/ignored fields, alternate state and baseline result for each checked population. Compare the inner aggregation separately from the final value so a matching total cannot hide a grain error.

Boundary design case: a total agrees with the baseline but changes incorrectly under a required selection. Keep the selection-contract failure open; do not accept the expression from the total alone.

## Benchmark case

A five-week-cover expression is built by proving field population, modifiers and inner aggregation grain before its final value is accepted.

## Anti-patterns

- Expanding this Skill into an adjacent diagnosis, execution or verification job.
- Treating one inconsistent precedent or assumption as authority.
- Proceeding through an unresolved evidence or authority gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the selection contract, source population, aggregation grain or accepted metric definition is unknown.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; adjacent jobs moved to independent Skills.
