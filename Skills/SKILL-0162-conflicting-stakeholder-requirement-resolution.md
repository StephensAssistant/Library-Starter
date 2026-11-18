---
id: SKILL-0162
type: skill
title: Conflicting Stakeholder Requirement Resolution
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, stakeholders, decisions]
trigger_phrases: [resolve stakeholder conflict, conflicting requirements, stakeholders disagree]
---

# Conflicting Stakeholder Requirement Resolution

Surface incompatible stakeholder requirements and route the choice without guessing.

## When to use

Use when two or more stakeholder requests cannot all be satisfied within the same authorised behaviour.

## Method

1. State each requested behaviour and its evidence.
2. Identify the concrete conflict and viable options.
3. Preserve the last authorised state.
4. Identify the evidenced decision authority.
5. Route the options, effects and unresolved trade-offs for decision.
6. Record the authorised replacement when decided.

## Decision and evidence details

Before routing a conflict, check whether the requested behaviours apply to the same population, period and authorised output. Record each option's concrete effects and the current authorised baseline. Only an evidenced decision replaces that baseline.

Near-miss design case: Finance and Operations need different totals for separate clearly labelled outputs. If both can coexist within scope, record the distinction rather than forcing a false choice. Unresolved shared definitions still require the evidenced authority.

## Benchmark case

Operations requests daily totals while Finance requires transaction-date totals. A passing application shows the incompatible definitions and routes the choice rather than blending them.

## Anti-patterns

- Guessing intent or seniority.
- Quietly combining incompatible requirements.
- Changing the authorised state before decision.

## Stop

Stop with an authorised resolution or an explicit waiting-on-authority state.
