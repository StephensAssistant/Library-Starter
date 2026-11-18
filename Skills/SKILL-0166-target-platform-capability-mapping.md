---
id: SKILL-0166
type: skill
title: Target-platform Capability Mapping
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0013]
tags: [skill, visual-design, platform-capability, interface]
trigger_phrases: [map design to platform, verify interface capability, constrained platform design]
---

# Target-platform Capability Mapping

Map proposed interface elements to verified primitives in the target platform.

## When to use

Use before promising or implementing a design in Sigma, Qlik, Streamlit or another constrained platform.

## Method

1. Identify every material visual and interaction requirement.
2. Verify the platform primitive, composition or supported alternative.
3. Separate exact support, supported approximation and unsupported detail.
4. Preserve information hierarchy, decision flow, semantics and customer experience.
5. Record deliberate deviations and their effect.

## Decision and evidence details

For each material requirement, retain the target platform/tenant, verified primitive or composition, evidence/date and exact deviation. Keep unsupported distinct from unverified. An approximation must preserve information and interaction meaning before it is presented as capability-equivalent.

Boundary design case: the mock-up requires an interaction visible only in another product. Record the target-platform evidence gap and hold the dependent promise; a similar screenshot cannot verify that interaction.

## Benchmark case

A mock-up uses a control unavailable in Sigma. A passing application verifies the limitation and maps the need to the closest supported composition without claiming native support.

## Anti-patterns

- Inventing platform capabilities.
- Using pixel similarity to override semantics.
- Hiding unsupported details.

## Stop

Stop with a verified capability map and explicit approximations or blockers.
