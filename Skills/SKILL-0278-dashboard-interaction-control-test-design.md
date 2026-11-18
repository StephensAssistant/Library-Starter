---
id: SKILL-0278
type: skill
title: Dashboard Interaction and Control Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [skill, testing, bi, dashboard-controls]
trigger_phrases: ["design dashboard interaction tests", "test BI controls", "validate dashboard filters"]
---

# Dashboard Interaction and Control Test Design

Design tests for dashboard controls, filters, navigation and interactive behaviour.

## Intent-routing contract

This Skill owns dashboard interaction and control test design only. Semantic correctness, security visibility, performance and export/presentation testing are separate actions.

## When to use

Use when filters, controls, defaults, scope, parent-child behaviour, selections or navigation must be tested.

## Method

1. Inventory every control, target, default, dependency and intended scope.
2. Test initial state, valid selections, empty selections, resets and boundary values.
3. Verify page, element and shared-filter scope against the stated contract.
4. Test parent-child controls, incompatible selections and no-data behaviour.
5. Verify representative navigation and interaction sequences preserve the intended state.
6. Record expected and observed behaviour separately from metric correctness.

## Benchmark case

A sales dashboard's store and department controls are tested for defaults, parent-child filtering, shared scope, reset behaviour and a valid no-data state without using visual agreement as data proof.

Boundary design case: The control exists but its intended page/element scope is undocumented. Mark the expected result unresolved and obtain the contract; observed behaviour cannot alone define correctness. A completed design does not claim test execution.

## Anti-patterns

- Testing only one happy-path selection.
- Assuming every control should affect every element.
- Treating correct totals as proof that interaction state is correct.
- Omitting reset, empty or incompatible selections.

## Stop

Stop when each control and representative interaction path has an explicit expected result and coverage for default, boundary, reset and no-data states.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0278 | related_to | undirected | inherited_from_source_split | supports
