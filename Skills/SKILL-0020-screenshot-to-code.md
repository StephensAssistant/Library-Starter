---
id: SKILL-0020
type: skill
title: Screenshot Interface Decomposition
status: current
created: 2026-08-31
updated: 2026-10-04
owner: Library owner

links: [SKILL-0013, SKILL-0120, SKILL-0122, SKILL-0123, SKILL-0124]
tags: [skill, screenshot-to-code, frontend, visual-design, interface-analysis]
trigger_phrases: [decompose this screenshot, inspect interface screenshot, map screenshot layout, image to code, analyse design reference]
---

# Screenshot Interface Decomposition

Convert a supplied screenshot or approved mock-up into observed interface facts that can guide implementation.

## When to use

Use before recreating a visual interface in any target stack.

## Method

1. Identify the source visual, intended viewport, device and use context.
2. Decompose hierarchy, regions, components, typography, spacing, colour, imagery, controls and visible states.
3. Separate observed facts from inferred behaviour and unknown runtime details.
4. Record responsive clues without presenting them as proven behaviour.
5. Produce a presentation map containing regions, component roles, visual relationships and unresolved interaction assumptions.
6. Hand off capability mapping, behaviour preservation, platform implementation and acceptance validation to separate action-specific Skills.

## Benchmark case

A dashboard screenshot contains six KPI cards, filters and a chart. A passing application records their measured hierarchy and relationships while labelling unshown interactions and responsive behaviour as unknown.

## Anti-patterns

- Treating inferred interaction as observed fact.
- Coding before identifying the viewport and hierarchy.
- Assuming a screenshot proves data, permissions or runtime behaviour.
- Using the screenshot itself as the implemented background.

## Stop

Stop with an inspectable interface decomposition and explicit observed, inferred and unknown fields.

## Image to Code integration — verified 2026-10-04

Source: https://github.com/Leonxlnx/taste-skill/tree/main/skills/image-to-code-skill (`image-to-code`). Use this capability whenever approved imagery or a mock-up should inform a design, including native BI, documents and diagrams. The upstream implementation workflow is web-focused; adapt its analysis rather than claiming other platforms support web code.

For visually important new web sections, use available authorized image generation to explore readable, section-specific references when that exploration serves the brief. Inspect typography, spacing, color, hierarchy, media and responsive clues before implementing native components. For an existing approved reference or fixed template, use that reference; generating a replacement is not permission to redesign it.

Do not render precise text, tables, formulas, scientific charts or diagram topology as a raster substitute for the deliverable. Use the respective native deterministic tools and inspect their rendered output. Preserve actual behaviour separately under SKILL-0167, verify target capabilities under SKILL-0166 and obtain scoped acceptance under SKILL-0171. An image proves appearance only.

This integration supplies reusable source guidance, not an installed-package or implementation-pass claim.
