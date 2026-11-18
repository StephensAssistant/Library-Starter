---
id: SKILL-0097
type: skill
title: Semantic Domain Boundary Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [data-modelling, semantic-domain]
trigger_phrases: ["design semantic model boundaries", "split or combine semantic domains", "decide semantic model scope"]
---

# SKILL-0097 — Semantic Domain Boundary Design

## Purpose

Define semantic-domain boundaries from business process, grain, reuse, security, ownership and topology.

## When to use

Use for: design semantic model boundaries; split or combine semantic domains; decide semantic model scope.

## Method

1. List processes, grains, measures, dimensions, audiences, security and change owners.
2. Identify reusable conformed dimensions and shared metrics.
3. Separate domains where grain, security or ownership creates incompatible contracts.
4. Combine only when relationships remain unambiguous and reusable.
5. Document composition keys and avoided duplication.

## Benchmark case

Separate sales and inventory snapshots while sharing conformed date, product and store meanings, rather than building one mega-model.

Missing-input design case: two candidate domains share dimensions but their security or ownership contract is unknown. Keep the boundary decision unresolved and identify the missing authority; shared terminology alone does not justify combining incompatible grains or duplicating a governed metric.

## Anti-patterns

- Choosing a model count by quota.
- Building report-specific micro-models that duplicate metrics.
- Combining incompatible grains.

## Stop

Stop with domain boundaries, shared contracts and rationale.
