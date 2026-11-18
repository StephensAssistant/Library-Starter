---
id: SKILL-0121
type: skill
title: Rendered Visual Anchor Approval
status: current
created: 2026-09-20
updated: 2026-10-31
links: [HAT-0005, PLAY-0006, PLAY-0048, PLAY-0060, SKILL-0020]
tags: [visual-design, prototype, approval]
trigger_phrases: ["visual anchor", "approve design direction", "representative design proof"]
---

# SKILL-0121 — Rendered Visual Anchor Approval

## Purpose

Produce and obtain direction approval on one complete representative visual anchor before scaling a consequential design.

## Intent routing contract

Activate only for visual anchor, approve design direction, representative design proof or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Choose the smallest screen, section, page or state that represents hierarchy and style.
2. Build it with real or clearly labelled representative content and verified primitives.
3. Render the actual artifact at the intended viewport or page size.
4. Show it to the Library owner when direction is consequential or uncertain.
5. Record preserve, revise or approve feedback.
6. Scale only the accepted direction.

## Anti-patterns

- Using prose, source code or wireframe boxes as the preview.
- Building the full artifact before resolving visual direction.
- Treating silence as approval.

## Decision and evidence details

Retain the rendered anchor revision, viewport/page size, representative content basis and the Library owner's exact direction feedback. Identify which hierarchy/style decisions the approval covers before scaling; material revisions need their own direction evidence under the existing condition.

Boundary design case: an earlier anchor was approved, then the hierarchy changes. Do not apply the earlier approval to the revised direction. Keep scale-out stopped until the required explicit feedback covers the current anchor.

## Benchmark case

For a six-card dashboard, a passing anchor renders one complete KPI card and surrounding context, captures the Library owner's feedback and only then duplicates the pattern.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop before scale-out until required direction feedback is explicit.

## Contextual links

- `SKILL-0327` — `shared_method` — A 2D animation seed is an example of approving a representative anchor before expanding an asset.
