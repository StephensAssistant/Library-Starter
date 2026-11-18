---
id: SKILL-0013
type: skill
title: Visual Direction Definition
status: current
created: 2026-08-28
updated: 2026-10-31
links: [HAT-0005, PLAY-0006, PLAY-0048, PLAY-0060, SKILL-0020, SKILL-0166, SKILL-0167, SKILL-0168, SKILL-0169, SKILL-0170, SKILL-0171]
tags: [visual-design, art-direction, design-brief]
trigger_phrases: ["design direction", "art direction", "redesign this", "creative direction", "Taste Skill", "Awesome DESIGN.md", "design a document", "design a flowchart", "design a workbook"]
---

# SKILL-0013 — Visual Direction Definition

## Purpose

Define a deliberate visual direction for a visible artefact before implementation.

## Intent routing contract

Activate for visual direction or creative design on any visible surface: websites/apps, Sigma dashboards/workbooks, spreadsheets, documents, presentations, reports, images and diagrams/flowcharts. HAT-0005's Visual Designer owns this direction. Use associated records for their own jobs; this Skill does not grant implementation or external-action authority.

## Method

1. Inspect audience, purpose, content, brand/context, target surface, device/page, existing design, real assets and downstream use.
2. Set five dials: variance, motion, density, asset dependence and brand fidelity.
3. Classify existing-artifact change as preserve, extend or overhaul; obtain the Library owner's approval for an unrequested overhaul.
4. Declare hierarchy, mood, palette, typography, spacing, imagery, interaction, accessibility and explicit anti-patterns.
5. Assess the approved external design sources below and use every applicable technique. Derive audience-led layout, meaningful variation, deliberate hierarchy and consistent design tokens; select density and motion for the job. Adapt web principles to native BI, documents and diagrams without inventing platform controls.
6. Hand the direction to the applicable platform/build Skill without inventing platform capability.

## Anti-patterns

- Starting decoration before content hierarchy is known.
- Inventing brand rules or presenting fabricated imagery as evidence.
- Treating a generic card grid as a design direction.

## Benchmark case

For a premium loyalty dashboard, a passing direction states the five-second message, restrained approved brand visual system, information density, image role, hierarchy and implementation constraints before charts are built.

Boundary design case: an existing approved dashboard needs one new element. Classify the change as preserve or extend where supported; retain its visual contract and do not treat an external landing-page reference as approval for a wholesale dashboard redesign.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the audience, purpose, brand boundary or requested degree of change is unresolved.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; former combined responsibilities moved to independent Skills while preserving existing links.

## Approved external design sources — verified 2026-10-04

| Source | Canonical location | Required use |
|---|---|---|
| Taste Skill | https://github.com/Leonxlnx/taste-skill — `skills/taste-skill/SKILL.md`, install name `design-taste-frontend` | Read the brief before styling; set context-appropriate variance, motion and density; avoid generic repeated compositions. |
| Awesome DESIGN.md | https://github.com/VoltAgent/awesome-design-md | Inspect selected design-system references; adapt palette, type, spacing, components and explicit rules to the actual product/brand. |
| Image to Code | https://github.com/Leonxlnx/taste-skill — `skills/image-to-code-skill/SKILL.md` | Use SKILL-0020 for source-image decomposition and image-first exploration when appropriate. |
| Web Design Guidelines | https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines | Use SKILL-0122 for applicable interface-quality and accessibility checks. |
| Playwright CLI | https://github.com/microsoft/playwright-cli | Use SKILL-0122 for permitted browser inspection, screenshots and interaction evidence. |

Assess all five for each design task, then apply the relevant methods through their canonical owners. Do not treat this source register as proof that a CLI or external skill is installed. Fetch current upstream guidance before applying a source-specific method; preserve the consulted revision and any material conflict in the work record.

Upstream Taste v2 is marked experimental and scopes itself to landing pages, portfolios and redesigns, expressly excluding dashboards/data tables/multistep product UI. the Library owner explicitly requires broader design use: transfer useful principles under this Library adaptation, while SKILL-0124 and the target-platform Skills govern BI density, metrics and native implementation. Do not blindly transfer a landing-page preset, React/GSAP requirement or decoration into Sigma, a workbook or a document.

Awesome DESIGN.md is a reference collection, not one executable Skill. Reuse its principles to define a product-specific design contract; do not substitute another company's identity for the approved brand. For diagrams, prioritize exact topology, readable labels and meaningful grouping. For documents/workbooks, prioritize reading order, legibility, consistent styles and faithful data.

## Change Log — 2026-10-04

Expanded mandatory direction routing to all visible design/creative work and integrated the Library owner's five approved design sources into existing canonical capabilities.


## Operational alert design

When the Library has an approved operational-alert template, reuse its native HTML and field/rendering contract. Preserve the accepted header, palette, type, spacing and section hierarchy. Vary system, status, real diagnostics and action fields. Escape dynamic values, retain literal diagnostic content, use the platform's HTML transport and inspect changed content in the actual email client. Establish each alert's source-state predicate, audience, grants, schedule and error handling. Template selection grants no send, deployment or scheduling authority.
