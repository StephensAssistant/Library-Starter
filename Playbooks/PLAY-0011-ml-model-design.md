---
id: PLAY-0011
type: playbook
title: ML Model Design — Problem-First Modelling
status: current
created: 2026-08-17
updated: 2026-09-06
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0003, PLAY-0007, PLAY-0018]
tags: [playbook, ml-model-design, machine-learning, cortex, design, mission-control]
migrated_from: PLAY-0011-old-library
---
# ML Model Design — Problem-First Modelling

## Trigger

A predictive/ML decision is requested.

## Method

Define actionable target/entity, available-at-decision-time inputs and baseline. Check data readiness and leakage. Prefer rules/SQL or existing governed capability before custom ML. Choose appropriate temporal/holdout evaluation, relevant segments and monitoring. Verify current capability facts before relying on them.

## Stop

Evidence-backed recommendation or insufficient-evidence statement. No invented metric threshold or automatic deployment.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

Design an ML or advanced-analytics solution from an actionable business problem, not from a preferred algorithm. the Library owner owns the pipelines and chooses material actions with the AI through the live Ticket or Project conversation. This playbook never authorizes a production change or invents a threshold.

## Trigger / entry condition

Mission Control routes a Ticket, Project, or conversation here when it needs prediction, forecasting, classification, clustering, anomaly detection, or another advanced-analytics design. Start after the ask has been framed by Session Intake where needed.

## Stages

### Stage 1 — Frame the problem

**Goal:** Establish a falsifiable business problem whose output supports a real decision.

**Action:** Record the decision and audience; target and entity; prediction type; success measure and current or naive baseline; inputs available at decision time; intended action; and deployment context. Use the form: "Predict [target] for [entity] from [available data] so [user] can [action]; success is judged against [baseline]." the Library owner resolves material choices.

**Exit:** The problem statement is confirmed, or the work stops because no meaningful action follows the output.

### Stage 2 — Assess data readiness

**Goal:** Prove that the available evidence can support the proposed test.

**Action:** Inventory sources, grain, history, volume, target availability, nulls, duplicates, skew, imbalance, temporal gaps, and leakage. Record a Green, Amber, or Red assessment with evidence rather than intuition.

**Exit:** Readiness is Green, the Library owner explicitly accepts documented Amber caveats, or Red blockers are handed to pipeline/data work and this playbook pauses.

### Stage 3 — Architect the solution

**Goal:** Choose the simplest adequate governed approach.

**Action:** Compare, in order, rules/SQL, currently available Snowflake built-ins, custom work inside Snowflake, and an external framework only when the earlier options are inadequate. Design features and their sources, transformations, training and serving, prediction storage, batch or real-time operation, and retraining signals. Record rejected alternatives and reasons.

**Exit:** the Library owner and the AI record the chosen design, assumptions, dependencies, and rejected alternatives in the Ticket or Project.

### Stage 4 — Design validation and monitoring

**Goal:** Precommit how the design will be judged before results are seen.

**Action:** Select an appropriate holdout strategy; use a time-based split for temporal problems. Define a primary measure, a business-readable secondary measure, current and naive comparisons, applicable segment or fairness checks, and drift/degradation monitoring. Ask the Library owner for any material tolerance or approval rule not already governed.

**Exit:** A reproducible evaluation and monitoring plan is recorded without invented thresholds.

### Stage 5 — Build the execution plan

**Goal:** Turn the approved design into dependency-ordered work.

**Action:** Create or update Ticket/Project tasks for feature pipelines, training data, baseline, model iteration, prediction serving, monitoring or dashboard work, and documentation. Record owners, dependencies, evidence required, and the next action chosen in conversation.

**Exit:** The implementation plan is actionable, or the no-build decision and rationale are recorded.

## Decision gates / branches

- No actionable decision or user action: exit as no-build or return to framing.
- Red data readiness: hand off missing data work, then return to Stage 2.
- Missing feature pipeline: hand off its target, grain, sources, transformations, and quality evidence to Pipeline Architect.
- External framework proposed: require evidence that simpler governed options are inadequate.
- Material metric, tolerance, approver, or retraining decision absent: ask the Library owner in the live conversation and pause only that branch.

## Loop-back rules

- New leakage, target ambiguity, or decision mismatch returns to Stage 1 or 2.
- Implementation constraints that invalidate the architecture return to Stage 3.
- Failed validation returns to Stage 3, or Stage 1 when the problem itself is wrong.
- A changed business action returns to the earliest affected stage and preserves the decision trail.

## Overall exit condition

The Ticket or Project contains a confirmed problem, evidence-backed data assessment, approved design, validation/monitoring plan, and chosen next action — or a documented no-build decision.

## Hand-offs

- **From PLAY-0007 Session Intake:** receive the framed goal, knowns, resolved decisions, and remaining scoped gaps.
- **To Pipeline Architect:** send missing source/feature requirements, grain, transformations, quality expectations, and dependencies.
- **To Dashboard Ideation:** send audience, decisions, prediction grain, measures, monitoring needs, and caveats.
- **To Data Documentation:** send the problem statement, data lineage, design decisions, evaluation evidence, monitoring plan, and current operational state.
- **To retained Knowledge:** use the owner’s historical design reference for historical provenance only; use current technical references for capability facts.

## Guard rails and useful reference

Prefer simple rules or SQL before custom ML. Check for leakage, imbalance, naive baselines, temporal splitting, and monitoring before deployment. Snowflake Cortex and Snowpark capabilities change; verify current availability instead of treating the historical function list in the owner’s historical design reference as authoritative.

## Anti-Patterns

- Choosing a model before defining the problem.
- Skipping the current and naive baselines.
- Using data unavailable at prediction time.
- Ignoring imbalance, segment performance, or temporal structure.
- Reaching for external/custom ML without testing simpler options.
- Deploying without an explicit monitoring and response plan.

</details>
