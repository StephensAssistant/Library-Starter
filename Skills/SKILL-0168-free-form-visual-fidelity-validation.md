---
id: SKILL-0168
type: skill
title: Free-form Visual Fidelity Validation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0013]
tags: [skill, frontend, visual-design, fidelity]
trigger_phrases: [validate screenshot fidelity, compare coded interface, visual similarity]
---

# Free-form Visual Fidelity Validation

Measure and repair visual fidelity for a free-form rendered interface.

## When to use

Use for HTML, CSS, JavaScript, React, Vue or another target where layout and styling are directly controllable.

## Method

1. Agree the source viewport and measurable acceptance threshold.
2. Render one representative anchor when direction is consequential.
3. Compare hierarchy, geometry, typography, spacing, colour, imagery and visible states systematically.
4. Repair the largest material mismatch first.
5. Repeat comparison until the threshold is met or a constraint is evidenced.
6. Keep visual and functional verdicts separate.

## Decision and evidence details

Retain the source image/revision, rendered build, matched viewport/state, agreed measurement and actual result. Separate measured differences from subjective observations; do not turn a visual estimate into a numeric fidelity claim.

Boundary design case: the source viewport or acceptance threshold is unknown. Resolve that comparison contract before asserting a measured pass. Native constrained-platform approximations need their own capability assessment rather than a free-form pixel-equivalence promise.

## Benchmark case

A React page is recreated from a desktop screenshot. A passing application compares both at the agreed viewport, measures material differences and does not claim pixel identity from inspection alone.

## Anti-patterns

- Claiming pixel identity without measurement.
- Comparing different viewports.
- Letting fidelity override functionality.

## Stop

Stop with the measured verdict, remaining deviations and separate functional status.
