---
id: PLAY-0060
type: playbook
title: Visual Design and Desirability Gate
status: current
created: 2026-08-28
updated: 2026-10-04
owner: the Library owner
links: [HAT-0005, PLAY-0006, PLAY-0012, PLAY-0019, SKILL-0013, SKILL-0020, SKILL-0120, SKILL-0121, SKILL-0122, SKILL-0123, SKILL-0124, SKILL-0166, SKILL-0167, SKILL-0168, SKILL-0169, SKILL-0170, SKILL-0171]
tags: [playbook, visual-design, desirability, rendered-preview, visual-qa, accessibility]
---
# Visual Design and Desirability Gate

## Trigger

A visible artifact is designed, creatively explored, created or materially redesigned on any platform, including websites/apps, Sigma dashboards/workbooks, spreadsheets, documents, presentations, reports, images and diagrams/flowcharts.

## Method

Activate HAT-0005's Visual Designer sub-role and use SKILL-0013, SKILL-0123 and SKILL-0122 plus every applicable platform/build/data capability. Assess Taste Skill, Awesome DESIGN.md, Image to Code, Vercel Web Design Guidelines and Playwright CLI through the canonical integrations in SKILL-0013, SKILL-0020 and SKILL-0122. Apply transferable principles everywhere; execute image-reference, web-code and browser methods only on surfaces for which they are appropriate and authorized. Read real content/data and relevant existing identity. Build a representative render, resolving only consequential uncertain direction with the Library owner. Complete and inspect applicable layout, accessibility, interactions and content fidelity. Reuse acceptance evidence.

### Qlik app-cover standard

When creating or revising a the owner’s Qlik app cover, the canonical design and quality reference is the owner-approved app cover quality reference. This reference is mandatory, not illustrative.

Preserve the reference image as the fixed visual template unless the Library owner explicitly asks for a wider redesign. The default operation is **template substitution, not redesign**.

Keep unchanged:

- 8:5 landscape composition and overall proportions.
- the owner’s wordmark at top-left.
- Snowflake branding at top-right for Snowflake-converted apps.
- Central Snowflake cloud, its arrows/connectors, their placement and visual treatment.
- Pale blue/green analytical background, restrained chart/database motifs, layered curved waves, palette, spacing, keylines and overall visual hierarchy.
- Dark the owner’s-green footer band, typography style and alignment.

Change only these app-specific elements:

- The large main app title in the footer.
- The concise parenthesised/sub-description directly beneath the title, describing what the app reports on.
- The subject icons and their short labels.
- The **number of subject icons must match the distinct data/reporting areas in that app**; do not force three icons when the app logically has more or fewer.

Subject icons must remain in the same circular/pill visual language as the reference and should depict the actual reported content rather than generic concepts. Do not add new logos, badges, slogans, decorative systems or alternative branding. Do not replace Snowflake with Qlik or another logo when the reference calls for Snowflake.

Before rendering, inspect the reference image itself. The candidate must visibly belong to the same app-cover family at comparable quality. If a proposed change affects anything beyond the title, sub-description, subject icon count/icons/labels, stop unless the Library owner has explicitly authorised the wider change.

For an existing application, keep visual and behavioural evidence separate:

- **Visual evidence:** approved source, exact viewport, rendered implementation, measured comparison, overflow and responsive checks.
- **Behavioural evidence:** a traceable inventory of existing actions, validations, dialogs, state, permissions, data mutations and failure paths, with each item exercised in the target runtime.
- **Platform evidence:** the deployed target environment, supported component boundary and any constraint that required an approved deviation.

A visual PASS never proves functional parity. A static code comparison never proves runtime interaction. The candidate is accepted only when every in-scope contract has its own evidence, or the unverified portion is named explicitly.

## Stop

Verified render plus verified in-scope behaviour for an existing interactive application, or an explicitly unverified visual/functional result. Minor copy edits need only affected checks; no design dossier or independent role chain for every document.

AGENTS.md owns shared authority, evidence reuse and task boundaries.
