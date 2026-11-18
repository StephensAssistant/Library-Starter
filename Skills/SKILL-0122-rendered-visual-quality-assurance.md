---
id: SKILL-0122
type: skill
title: Rendered Visual Quality Assurance
status: current
created: 2026-09-20
updated: 2026-10-19
links: [HAT-0005, PLAY-0006, PLAY-0048, PLAY-0060, SKILL-0020]
tags: [visual-design, visual-qa, accessibility]
trigger_phrases: ["visual QA", "inspect rendered output", "validate visual artifact", "web design guidelines", "Playwright CLI", "check design accessibility"]
---

# SKILL-0122 — Rendered Visual Quality Assurance

## Purpose

Inspect an actual rendered visual artifact and repair visible, behavioural and accessibility defects.

## Intent routing contract

Activate only for visual QA, inspect rendered output, validate visual artifact or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Render the artifact at relevant sizes, pages and interaction states.
2. Check hierarchy, focal point, spacing, alignment, typography, colour, imagery and data fidelity.
3. Check contrast, legibility, responsive behaviour, reduced motion and keyboard/interaction behaviour where applicable.
4. Inspect useful empty, loading, error and selected states.
5. Repair defects and re-render the changed surfaces.
6. Hand final validation to an independent Tester or Validator.

## Anti-patterns

- Approving from source code alone.
- Checking only one viewport.
- Ignoring empty, error or interaction states.

## Benchmark case

A passing dashboard QA catches a clipped label at mobile width, low-contrast secondary text and an unclear selected state, repairs them and verifies both target viewports.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop release when a material rendered defect or accessibility failure remains.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.

## Web Design Guidelines integration — verified 2026-10-04

Canonical skill: https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines.
Current rule source: https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md.

Fetch the current rules before a web-interface review. Check semantic controls, accessible labels, keyboard/focus, forms/errors, reduced motion, typography/content overflow, imagery, responsive layout, performance, navigation/state and touch behaviour. Report concrete defects with source location or an exact native element reference.

For Sigma, documents, spreadsheets, slides and diagrams, apply the transferable legibility, contrast, hierarchy, meaningful labels, state clarity and layout checks through native rendering and platform controls. DOM/ARIA/CSS-specific rules apply only where that surface exists. Automated checks do not replace rendered inspection or manual accessibility checks that the claim requires.

## Playwright CLI integration — verified 2026-10-04

Source: https://github.com/microsoft/playwright-cli.
Package: `@playwright/cli`; documented prerequisites include Node.js 18+ and local browser setup.

For permitted local web-project QA, verify the available CLI/version, then use documented snapshot, viewport, screenshot and interaction commands to inspect representative pages and states. Select elements from observed snapshots/locators, exercise actual navigation/forms/controls, inspect console/network issues when material, and repair/recheck changed surfaces. Record the exact build, browser, viewport, state/journey and observed result. Read current command documentation; do not guess commands or selectors.

Respect the active environment's authorized browser mechanism. A Library Skill does not grant browser/session access, permission to install tooling, disclose data, perform external writes or incur paid services. Use the approved browser tools for authenticated surfaces when required; report a missing capability and complete independent native/render checks.

For a non-browser artefact, inspect its native render. For a browser-hosted Sigma workbook, browser evidence covers only the reachable rendered interactions tested; it does not prove metric correctness or permissions outside the tested identity. CLI availability, a screenshot or a successful command is never a complete usability, accessibility or functional-parity pass.

## Change Log — 2026-10-04

Integrated Vercel Web Design Guidelines and Microsoft Playwright CLI with explicit native-platform adaptation and evidence/authority boundaries.


## Operational alert templates

When the Library has an approved operational-alert template, use its native HTML and field/rendering contract. Apply this Skill to rendered and actual-output verification. Template selection creates no send, deployment or scheduling authority.

RELATIONSHIP-EVIDENCE: PLAY-0070--SKILL-0122 | related_to | undirected | authoritative_record | supporting capability declared by the reusable email procedure

## Contextual links

- `SKILL-0327` — `shared_method` — Sprite review extends rendered checks to frame alignment and motion at game scale.
