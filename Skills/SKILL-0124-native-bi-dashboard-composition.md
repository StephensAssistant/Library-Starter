---
id: SKILL-0124
type: skill
title: Native BI Dashboard Composition
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0020]
tags: [visual-design, bi-dashboard, composition]
trigger_phrases: ["design BI dashboard", "dashboard composition", "premium report layout"]
---

# SKILL-0124 — Native BI Dashboard Composition

## Purpose

Compose a native BI dashboard around business decisions using verified platform primitives.

## Intent routing contract

Activate only for design BI dashboard, dashboard composition, premium report layout or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Define the five-second decision or understanding.
2. Create a deliberate reading path: headline/context, primary KPIs, main analytical question, supporting comparison, exceptions and detail.
3. Use whitespace, typography, restrained colour and grouping before decorative containers.
4. Set density to the audience and expected interaction speed.
5. Use compound containers only when they improve hierarchy or provide a verified missing treatment.
6. Do not transfer conventions across BI products without capability validation.

## Anti-patterns

- Filling a generic grid with unrelated charts.
- Adding cards before hierarchy is established.
- Assuming web CSS or another BI platform's controls exist natively.

## Decision and evidence details

Record the business decision, audience, verified native objects and intended reading path alongside the rendered composition. For each main element, explain which question or exception it supports; remove or defer elements whose role is unresolved rather than filling available space.

Boundary design case: the requested dashboard has charts and branding but no agreed primary decision. Return that decision gap before committing the hierarchy; a visually complete grid does not establish a useful composition.

## Benchmark case

For a loyalty health dashboard, a passing composition surfaces membership growth and engagement first, follows with trend and exceptions, and implements the premium treatment using verified native objects.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the primary decision, audience or platform capability is unresolved.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
