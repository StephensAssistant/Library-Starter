---
id: SKILL-0128
type: skill
title: Assumption Management
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [project-management, assumptions, validation]
trigger_phrases: ["record assumption", "validate assumption", "assumption register"]
---

# SKILL-0128 — Assumption Management

## Purpose

Manage unproven statements currently relied upon for delivery or acceptance.

## Intent routing contract

Activate only for record assumption, validate assumption, assumption register or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. State the assumption precisely and the outcome that relies on it.
2. Record its evidence, owner or validation authority and current date.
3. Define the test, source or event that will prove or disprove it.
4. Set a review or expiry trigger.
5. Promote a proven assumption to fact and remove it from the register.
6. Convert a disproven assumption to the appropriate issue, risk, dependency or plan change.

## Anti-patterns

- Leaving resolved assumptions open.
- Treating hope as evidence.
- Failing to name the outcome exposed if the assumption is false.

## Decision and evidence details

Keep the assumption's original wording and dependent outcome traceable when recording its validation result. A failed or unavailable test leaves the statement unproven; do not promote it to fact from the absence of a contradiction. Record which reliance must stop and the next evidence source.

Boundary design case: an API field is not visible because access is missing. Retain the assumption and access gap rather than declaring the field absent or confirmed.

## Benchmark case

For an assumed API field, a passing record names the dependent report metric, verification call, owner and deadline, then converts the item to fact or issue from the result.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop reliance when a material assumption lacks a validation route or authority.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
