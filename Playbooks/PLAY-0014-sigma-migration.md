---
id: PLAY-0014
type: playbook
title: Sigma Migration — Qlik to Sigma
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0003, PLAY-0018, PLAY-0022, PLAY-0053, PLAY-0065]
tags: [playbook, sigma-migration, qlik, sigma, design, mission-control]
migrated_from: PLAY-0014-old-library
---
# Sigma Migration — Qlik to Sigma

## Trigger

Qlik content is being replaced with Sigma.

## Method

Use [[PLAY-0022]] for migration. Inventory usage and consumers before choosing migrate/retire/consolidate. Map measures, selections, Set Analysis/Aggr and Section Access to verified target patterns. Keep transformation in governed data pipelines; prove metric, filter, access and usability behavior.

## Stop

Validated replacement or a specific gap; retain approved cutover, rollback and retirement decisions.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

Assess, redesign, validate, and control the migration or retirement of a Qlik application in Sigma. Transformation belongs in the Library owner-owned pipelines; the live conversation selects every material cutover, approval, tolerance, and communication action.

## Trigger / entry condition

Mission Control routes work here when a Qlik app/report may be migrated, rebuilt, consolidated, or retired in favour of Sigma.

## Stages

### Stage 1 — Inventory and triage

**Goal:** Establish the current position and decide whether migration is justified.

**Action:** Capture app name, owner, audience, observed usage, business decisions, sources and load scripts, QVD dependencies, measures, dimensions, complex expressions, security, reloads, downstream consumers, and existing documentation. the Library owner and the AI choose migrate, retire, consolidate, defer, or investigate.

**Exit:** A disposition, priority rationale, and evidence are recorded in a Ticket or Project.

### Stage 2 — Map concepts and gaps

**Goal:** Translate the Qlik design into an appropriate Sigma/Snowflake architecture rather than copying it.

**Action:** Map app to workbook; sheets to pages; master measures to governed metrics; dimensions to model columns/relationships; selections to targeted controls; Section Access to Sigma permissions plus Snowflake RBAC; reloads to pipeline/materialisation needs; Set Analysis and Aggr() to reviewed Sigma patterns. Move transformation out of the BI layer and identify unsupported concepts requiring redesign.

**Exit:** The mapping, redesign decisions, risks, and unresolved gaps are reviewable.

### Stage 3 — Establish data-model readiness

**Goal:** Confirm governed FACT/DIM data and a secure, maintainable Sigma model.

**Action:** Verify facts/dimensions, the Snowflake Semantic View and the per-report golden dynamic table, along with grain, lineage, freshness, relationships, metrics, descriptions, visibility, security, and materialisation needs. AGENTS.md governs any golden-view exception. Route missing or unsuitable tables to Pipeline Architect. Use the owner-approved reporting platform reference for current Sigma reference patterns.

**Exit:** The data model is ready for workbook work, or documented pipeline/security dependencies pause the affected branch.

### Stage 4 — Design and plan the workbook

**Goal:** Build a decision-led replacement plan rather than a lift-and-shift replica.

**Action:** Invoke Dashboard Ideation to confirm audience, decisions, measures, navigation, controls, and acceptance. Create dependency-ordered Ticket/Project tasks for model, workbook, validation, documentation, training, communication, cutover, and rollback readiness.

**Exit:** A candidate workbook and evidence-based validation plan are ready.

### Stage 5 — Validate and choose cutover

**Goal:** Prove equivalence or approved improvement and make a controlled human decision.

**Action:** Compare key metrics, filters, selections, security, performance, usability, lineage, and documentation side by side. the Library owner confirms unresolved tolerances, approver, freeze window, cutover style, communications, and rollback conditions in the live conversation. Apply PLAY-0022's route-specific acceptance and seven-calendar-day hypercare; do not reopen its settled controls as optional choices.

When serving-layer performance is disputed, run a controlled view-versus-Dynamic-Table comparison on representative small and large reports. Require identical logic and filters, result parity, repeated cold/warm runs, query runtime and scan evidence, refresh credits, and observed page/filter response. Keep proof-of-concept evidence distinct from an estate-wide architecture decision.

**Exit:** the Library owner approves hard, parallel, phased, retire-only, defer, or rollback action and its evidence/communications are recorded.

## Decision gates / branches

- Rarely used, redundant, or superseded app: take the documented retirement path rather than migrate by default.
- Missing or unsuitable Snowflake data: hand off to Pipeline Architect, then return to Stage 3.
- Metric mismatch: return to Stage 2, 3, or 4 according to cause.
- Security failure: stop the release branch and return to Stage 2 or 3.
- Audience/design failure: return to Dashboard Ideation and Stage 4.
- Missing case-specific tolerance, approver, freeze, cutover, communication, or rollback rule: read PLAY-0022 and settled decisions first, then ask the Library owner only about remaining material choices.
- Post-cutover failure: record current state and invoke the explicitly approved rollback/next action; do not improvise a production mutation.

## Loop-back rules

- New dependency returns to Stage 1 or 2.
- Data-model defects return to Stage 3.
- User-acceptance feedback returns to Stage 4.
- Validation failures return to the earliest stage that owns the cause.
- Changed business priority returns to Stage 1 while preserving completed evidence.

## Overall exit condition

The migration, retirement, deferment, or rollback decision is supported by validation evidence, documentation, chosen communications, and an explicit Ticket/Project next action. No production mutation is authorized by the playbook alone.

## Hand-offs

- **From Session Intake:** receive the framed migration question and known constraints.
- **To Pipeline Architect:** send missing table, grain, lineage, refresh, quality, and dependency requirements.
- **To Dashboard Ideation:** send audience, decisions, measures, current layout/usage, and redesign opportunities.
- **To ML Model Design:** send prediction outputs, grain, explanation, refresh, and monitoring requirements when applicable.
- **To the owner-approved reporting platform reference:** use the retained Sigma reference for capability and implementation facts.
- **To Data Documentation:** send current-state inventory, mappings, lineage, security, validation, cutover decision, rollback state, and customer/stakeholder communication record.

## Nonbinding historical heuristics and reference

Historical examples include page-load performance below five seconds and a two-to-four-week parallel run. These are unverified historical heuristics, not canonical tolerances or durations. the Library owner must confirm unresolved case-specific performance, equivalence, cutover, and approval choices; PLAY-0022 and AGENTS.md supply the settled seven-calendar-day hypercare gate. Preserve the source's useful concept and expression mappings as provenance, but verify current Sigma capabilities and syntax against the owner-approved reporting platform reference or live documentation.

## Anti-Patterns

- Copying Qlik layout without reassessing audience and decisions.
- Recreating Qlik load scripts inside Sigma.
- Replacing an associative model with one oversized relational model.
- Pointing Sigma at raw or QVD-shaped data instead of governed tables.
- Skipping metric, security, usability, or performance validation.
- Declaring a serving-layer winner from one report, one cache state or one best runtime.
- Migrating an unused app without an evidence-based reason.

</details>

## Guardrail correction — 2026-10-13

Architect and Data & BI Lead: inherited the settled reporting architecture, route-specific acceptance, and seven-calendar-day hypercare rather than asking to select these anew.
