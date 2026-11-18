---
id: PLAY-0010
type: playbook
title: Pipeline Architect — Data Pipeline Design
status: current
created: 2026-08-14
updated: 2026-10-13
owner: the Library owner
links: [HAT-0003, PLAY-0006, PLAY-0007, PLAY-0008, SKILL-0318, PLAY-0018, PLAY-0032]
tags: [playbook, pipeline-architect, data-pipeline, design, mission-control, l3-design]
migrated_from: PLAY-0010-old-library
---
# Pipeline Architect — Data Pipeline Design

## Trigger

A new or materially changed data pipeline needs design.

## Method

Reuse the current outcome. Inspect real source, row grain, keys, volume, refresh and consumers. Choose the simplest architecture consistent with approved domain constraints. Define mappings, incremental/delete behavior, quality/security checks and recovery. Verify material design assumptions before implementation.

## Stop

A sufficient design and next step, or one concrete source/architecture blocker. No automatic full research/interview cycle.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

A Design-level (L3) workflow for a new data pipeline, source integration, platform change, migration strategy, or material data-flow change. It runs before implementation SQL. the Library owner owns every pipeline and decides material action with the AI in the active Ticket or Project. The workflow must not invent SLAs, ownership, approvals, production actions, or acceptance thresholds.

## Trigger / entry condition

Start when the Library owner or an active Ticket/Project asks to design, plan, scope, architect, or materially change a data pipeline, source integration, platform, migration, or data flow before implementation begins.

## Stages

### Stage 1 — Specify

**Goal:** Establish a confirmed problem definition and unambiguous grain.

**Action:** Determine the source system; data volume, frequency, format, and schema stability; consumer; one-row grain; freshness or SLA where already known; and known pain points. Use a PLAY-0007 brief as input but perform a lightweight completeness check.

**Exit:** the Library owner confirms a one-paragraph problem statement and the grain can be stated clearly. Undefined grain blocks progression.

### Stage 2 — Research

**Goal:** Ground the design in existing patterns, evidence, and constraints.

**Action:** Search for similar pipelines and governed patterns rather than assuming none exist. Inspect dependencies such as new stages, file formats, and databases; research unfamiliar source export capabilities; and record ML or analytics implications.

**Exit:** A five-to-eight-bullet constraints-and-considerations summary is complete, or the simple-path branch records why a full research stage is unnecessary.

### Stage 3 — Architect

**Goal:** Produce an implementable data-flow and layer design.

**Action:** Create a text flow — Source → Ingestion Method → RAW → STG → INGESTED → FACT/DIM → Consumer. For every layer, define table name, grain/key columns, transformation logic, and load strategy. Record a Key Decisions table with choice and reasoning, plus material open questions.

**Exit:** The design is internally coherent, aligns with the owner-approved ingestion architecture and naming standard, and exposes every material open question.

### Stage 4 — Validate

**Goal:** Demonstrate that the design is robust before implementation.

**Action:** Check grain; natural-key reliability; null and duplicate handling; rebuild from scratch; late, empty, malformed, and duplicated-source failure modes; ten-times-current-volume scale; and governed architecture alignment. Surface every issue rather than glossing over it.

**Exit:** Findings are resolved, explicitly accepted by the Library owner, or returned to Stage 3. The simple-path branch may reuse applicable verified template evidence; it does not waive material design checks or unresolved prerequisites.

### Stage 5 — Document and approve

**Goal:** Make the approved design durable and ready for implementation handoff.

**Action:** Record the Library owner's decision, current position, evidence, constraints, risks, and unresolved items. Pass the Phase 3 design and validation outcome to the Data Documentation playbook for a formal technical specification.

**Exit:** The design is approved and a durable specification or explicit documentation handoff exists.

## Overall exit condition

An approved design has been documented and handed to an implementation Ticket or Project with evidence, decisions, risks, and unresolved items stated. Writing implementation SQL is outside this playbook.

## Hand-offs

- **From PLAY-0006 and PLAY-0007:** Receive route, size, Knowns, resolved decisions, and remaining gaps.
- **To SKILL-0318:** Send only material judgment gaps that cannot be resolved through exploration; receive the confirmed decision log.
- **To the owner-approved ingestion architecture and naming standard:** Use it as the authoritative Snowflake ingestion architecture and naming reference; do not duplicate or override it.
- **To related ML, dashboard, or Sigma migration playbooks:** Pass the approved data flow, grain, dependencies, decisions, and constraints when those outputs are in scope.
- **To PLAY-0018:** Pass the approved layer design, validation evidence, decision table, and open risks for the formal specification.
- **To the implementation Ticket or Project:** Pass the approved specification; implementation starts only after this design exit.

## Decision gates / branches

- **Simple:** A standard-pattern, single-table source may run Stages 1 and 3 tightly and record how the relevant research, validation, and documentation requirements are satisfied by an existing verified governed template. Missing or inapplicable evidence still requires the affected check or hand-off.
- **Medium:** A new source, multiple tables, or data-quality concerns runs all five stages at moderate depth.
- **Complex:** A new architecture pattern, cross-system joins, ML integration, or SCD2 runs all five stages at full depth and may require multiple rounds.
- A complete framing brief can satisfy Stage 1 questions subject to a lightweight backstop; do not repeat settled intake.
- Undefined grain, an unverified source assumption, or an unresolved material decision blocks architecture approval.
- the Library owner decides material thresholds, acceptance, and production action in the active conversation; the playbook does not guess.

## Loop-back rules

- A new judgment gap returns through Grill Me and then to the earliest affected stage.
- A missing fact or unfamiliar dependency returns to Stage 2.
- A validation issue returns to Stage 3 for redesign.
- A material scope or consumer change returns to Stage 1.
- Repeated unresolved loops are escalated to the Library owner and recorded rather than silently cycled.

## Anti-Patterns to Flag

| Anti-pattern | Instead |
|---|---|
| Skipping straight to SQL | Define grain, keys, flow, and load strategy first |
| Merging RAW/STG or STG/INGESTED casually | Follow the owner-approved ingestion architecture and naming standard unless the Library owner records an approved exception |
| Premature optimisation | Validate the architecture before tuning |
| Undefined grain | Stop until one row is clearly stated |
| Assumption stacking | Verify source assumptions before building on them |
| Hiding a validation problem to preserve momentum | Surface it and loop back explicitly |

</details>

## Guardrail correction — 2026-10-13

Architect and Tester: a simple pipeline may reuse verified template evidence, but cannot waive material validation or documentation prerequisites.
