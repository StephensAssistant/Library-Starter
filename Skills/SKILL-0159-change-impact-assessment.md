---
id: SKILL-0159
type: skill
title: Change Impact Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, change-control, impact]
trigger_phrases: [assess change impact, scope change impact, evaluate requested change]
---

# Change Impact Assessment

Assess the consequences of a proposed or authorised change.

## When to use

Use when a change may affect behaviour, components, dependencies, testing, customer experience, time, cost, risk or forecast.

## Method

1. Compare previous and requested behaviour.
2. Identify affected components, data, contracts and consumers.
3. Assess sequence, dependency, validation, customer, time, cost, risk and forecast effects.
4. Separate evidenced effects from assumptions and gaps.
5. Record the impact receipt before implementation or approval.

## Decision and evidence details

For each changed behaviour or contract, record the prior/requested state, affected consumer, evidence, necessary validation and known forecast effect. Label unknown consumer coverage explicitly and identify the source needed to resolve it; assessment does not authorise implementation.

Boundary design case: the edited metric has known report consumers but unverified exports. Keep export impact unresolved and the dependent acceptance open rather than describing the assessed reports as complete coverage.

## Benchmark case

A late metric change affects a semantic model and three reports. A passing application identifies each consumer, required retesting and forecast effect without guessing cost or approval.

## Anti-patterns

- Assessing only the edited component.
- Hiding unknown impacts.
- Treating an impact assessment as approval.

## Stop

Stop with a traceable impact receipt or the precise evidence gap.
