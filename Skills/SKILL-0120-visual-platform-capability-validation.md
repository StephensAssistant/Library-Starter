---
id: SKILL-0120
type: skill
title: Visual Platform-Capability Validation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0020]
tags: [visual-design, platform-capability, verification]
trigger_phrases: ["can this design be built", "verify visual control", "platform design capability"]
---

# SKILL-0120 — Visual Platform-Capability Validation

## Purpose

Verify that every primitive required by a visual concept exists in the named implementation platform or has a proven composition fallback.

## Intent routing contract

Activate only for can this design be built, verify visual control, platform design capability or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. List required chart, KPI, image, layout, text, control, action, formatting, responsive and interaction primitives.
2. Check the current target platform or authoritative current documentation.
3. Separate directly supported, composition-supported, unverified and unsupported primitives.
4. Replace absent controls with verified compositions that preserve the design goal.
5. Label unverified elements concept-only and keep implementation instructions out of them.

## Anti-patterns

- Inventing menu paths from another product or version.
- Treating a mock-up as capability evidence.
- Hiding an unsupported primitive inside vague build instructions.

## Decision and evidence details

Retain a requirement-to-primitive map with platform/version or tenant, inspected source/date, observed capability and fallback evidence. A supported composition must preserve the required information and interaction, not merely resemble the concept.

Boundary design case: documentation shows a control but the target tenant does not expose it. Keep account availability unverified and block dependent implementation guidance until it or an agreed composition is proven.

## Benchmark case

When a KPI lacks an icon property, a passing validation proves a container plus KPI plus image composition and removes the fictional icon-setting instruction.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop implementation guidance when an unverified primitive materially changes the build.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
