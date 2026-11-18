---
id: SKILL-0170
type: skill
title: Sigma Interface Reconstruction
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0013]
tags: [skill, sigma, interface, visual-design]
trigger_phrases: [rebuild design in sigma, screenshot to sigma, recreate sigma dashboard]
---

# Sigma Interface Reconstruction

Reconstruct an approved interface with verified Sigma primitives and compositions.

## When to use

Use when implementing a screenshot or mock-up in Sigma Computing.

## Method

1. Verify each required control, format, layout primitive and interaction against current supported capability and tenant experience.
2. Use native containers, stacks, hierarchy and supported composition.
3. Preserve premium direction through spacing, typography, backgrounds, images, icons and restrained branding.
4. Treat early filters as performance or data controls only when evidence supports that need.
5. Validate real query and interaction behaviour, not only static appearance.
6. Record deliberate approximations.

## Decision and evidence details

Retain the approved reference, workbook/version, verified primitive map, deliberate approximations and observed query/interaction results. Check that the same information and selection semantics survive each composition; resemblance alone is insufficient.

Boundary design case: the recreated KPI card looks correct but its filter scope cannot be verified. Keep the runtime result unresolved and name the required interaction check; static appearance cannot satisfy the real-query requirement.

## Benchmark case

A premium KPI card mock-up requires unsupported subtitle treatment. A passing implementation uses verified native composition and records the approximation instead of inventing a control.

## Anti-patterns

- Claiming nonexistent Sigma settings.
- Treating a static mock-up as runtime proof.
- Moving governed modelling into Sigma for visual convenience.

## Stop

Stop with a capability-equivalent Sigma result and explicit deviations.
