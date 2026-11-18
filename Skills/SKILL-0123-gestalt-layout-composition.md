---
id: SKILL-0123
type: skill
title: Gestalt Layout Composition
status: current
created: 2026-09-20
updated: 2026-10-31
links: [HAT-0005, PLAY-0006, PLAY-0048, PLAY-0060, SKILL-0020]
tags: [visual-design, gestalt, layout]
trigger_phrases: ["improve visual grouping", "Gestalt layout", "clarify visual hierarchy"]
---

# SKILL-0123 — Gestalt Layout Composition

## Purpose

Compose layouts whose grouping, hierarchy, sequence and shared behaviour are perceptually unambiguous.

## Intent routing contract

Activate only for improve visual grouping, Gestalt layout, clarify visual hierarchy or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Use proximity so internal gaps are smaller than section gaps.
2. Use similarity only for elements sharing role or meaning.
3. Use common fate only for controls and objects that genuinely change together.
4. Align edges and baselines for good continuation; break alignment only for meaningful hierarchy.
5. Use closure and figure-ground to separate groups without excessive boxes.
6. Use symmetry for comparable stable content and deliberate asymmetry for emphasis.
7. Run a five-second test for grouping, primary focus, sequence, shared behaviour and section boundaries.

## Anti-patterns

- Using decorative consistency to imply false relationships.
- Letting enclosure contradict filter or interaction scope.
- Applying symmetry through accidental sameness.

## Decision and evidence details

Before layout changes, identify which elements share meaning or control scope. In the five-second test, retain the rendered version and the viewer's actual grouping, focus, sequence and scope interpretation; do not replace that observation with the author's intended grouping.

Boundary design case: enclosure makes a filter appear to affect all cards although it changes one. Revise the grouping or scope cue and repeat the check; decorative consistency is not a pass.

## Benchmark case

For a dashboard landing page, a passing composition lets a viewer identify the health headline, related KPIs, filter scope and exception area within five seconds.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when two principles imply conflicting groupings; change the layout until meaning is unambiguous.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.


## Operational alert templates

When the Library has an approved operational-alert template, use its native HTML and field/rendering contract. Apply this Skill to the layout hierarchy. Template selection creates no send, deployment or scheduling authority.

RELATIONSHIP-EVIDENCE: PLAY-0070--SKILL-0123 | related_to | undirected | authoritative_record | supporting capability declared by the reusable email procedure
