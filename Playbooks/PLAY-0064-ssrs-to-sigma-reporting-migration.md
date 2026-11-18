---
id: PLAY-0064
type: playbook
title: SSRS-to-Sigma Reporting Migration
status: current
created: 2026-09-20
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [PLAY-0022, PLAY-0053]
tags: [playbook, ssrs, sigma-computing, migration, snowflake, reporting]
---
# SSRS-to-Sigma Reporting Migration

## Trigger

An in-scope SSRS report must be rebuilt in Sigma under the recorded 2026-10-31 SQL Server exit target. Verify the current project scope/target before using it as a commitment; the date does not waive any migration gate.

## Intent routing

Use this playbook for the SSRS-to-Sigma route only. Use PLAY-0063 for a Qlik app whose SQL Server source is being changed to Snowflake while the Qlik front end remains intact. Use the later Qlik-to-Sigma route playbook when the Qlik front end itself is replaced.

This playbook owns SSRS discovery, Snowflake modelling, Sigma construction and route-specific acceptance. It inherits shared parity, access, grants, ownership, cutover, hypercare and decommission controls from PLAY-0022 and the governed reporting-platform workflow from PLAY-0053.

## Required outcome

For each report, preserve every existing required metric and business task while replacing the presentation layer with Sigma. Production modelling remains in Snowflake:

1. Facts and dimensions.
2. Snowflake Semantic View, including required metric logic until the separate metrics-model decision is resolved.
3. Per-report golden dynamic table built from the Semantic View.
4. Sigma workbook as the presentation layer.

Use a golden view only when the Library owner explicitly directs it or evidenced requirements or technical constraints prevent the dynamic-table path. Record the exception.

## Method

### 1. Inventory the SSRS report

Capture the RDL/report identity, consumers, owner, business purpose, schedules, subscriptions, parameters, filters, drill paths, exports, security, source objects, calculations, metrics and every business task the replacement must support. Record the baseline output and a comparison cutoff.

Every metric present in the SSRS report is mandatory in the replacement unless the business owner explicitly approves its removal.

### 2. Map and build the Snowflake model

Map the report grain and logic into governed Snowflake facts and dimensions. Reuse approved facts, dimensions, relationships and semantic definitions before creating anything new. If a required source or model object is missing, build or extend it through the applicable data-source and modelling controls before continuing.

Add required business logic and metrics to the Snowflake Semantic View. Until the boss defines a separate metrics model, do not invent a parallel metric store or duplicate canonical metric logic.

For every object and layer, identify and verify required system, service-identity, developer and user access. Apply both current-object and future schema grants for applicable object types, including tables, views and dynamic tables, unless an explicit narrower control is required. Determine ownership from verified current rules and comparable governed objects, then verify ownership and effective grants after every create or replace.

### 3. Build the report-serving object

Build one golden dynamic table per report from the Snowflake Semantic View. Validate refresh behaviour, freshness, grain, key uniqueness, required columns, metric results, performance and cost before using it in Sigma.

### 4. Build the Sigma replacement

Use Sigma only as the presentation and interaction layer; do not place production modelling or canonical metric logic in Sigma. Temporary test calculations are allowed only while validating and must not become an undeclared production dependency. Sigma-specific capabilities such as write-back may be used when explicitly required.

Until the boss defines the BI team's redesign authority, keep the replacement recognisably close to the SSRS report's structure and behaviour while applying measured usability, accessibility and premium-design improvements. A broader redesign requires explicit approval.

### 5. Prove route parity

Compare SSRS and Sigma at an aligned data cutoff. Retain evidence for:

- every mandatory metric;
- row, grain and key checks appropriate to the report;
- parameters, filters, selections and drill behaviour;
- schedules, subscriptions or replacement distribution needs;
- exports and every required business task;
- user and system access, with representative allowed and denied scenarios for every applicable source/report security restriction;
- refresh freshness and acceptable representative performance;
- known, explained exceptions.

The Sigma layout need not be a pixel copy, but the user must be able to complete every required business task. Unexplained material differences fail the gate.

### 6. Complete sequential validation

An identified non-author BI Analyst validates first. Correct and retest every evidenced defect. The report's business owner then reviews and accepts the corrected replacement. Both approvals are required before production promotion.

### 7. Promote and hypercare

Keep SSRS live throughout development, validation and production promotion. After both approvals, promote the Sigma replacement through PLAY-0053 and begin seven calendar days of hypercare.

the Library owner owns technical monitoring and remediation. The BI Analyst and business owner report behavioural defects. Monitor refreshes, dynamic-table state and lag, metric parity, access, performance and required business tasks. Fix forward, then retest every material defect.

### 8. Retire SSRS

Retire the SSRS report only after seven calendar days have elapsed with no unresolved or unverified material defect, the consumer search is complete, and the required retirement authority exists. Record residual consumers or dependencies instead of silently decommissioning around them.

## Branches

| Condition | Required path |
|---|---|
| Required source, fact or dimension is missing | Build or onboard it under the governed Snowflake path, then resume Step 2 |
| Source, owner, access or business owner is unknown | Record a blocker; do not infer or pass the gate |
| Boss authorises broader redesign | Record the authority and apply the agreed scope while preserving metrics and business tasks |
| A separate metrics model is later defined | Reconcile it with the Semantic View under the boss's decision; do not create duplicate authorities |
| Golden dynamic table is technically unsuitable | Use a golden view only with the Library owner's direction or evidenced constraint; record the exception |
| BI Analyst finds a defect | Fix and retest before business-owner review |
| Business owner rejects the replacement | Return to the failed build or validation step; SSRS remains live |
| Material defect appears in hypercare | Fix forward and retest; hypercare cannot exit with the defect unresolved or unverified |
| Consumer remains on SSRS | Record owner and dependency; do not retire that report |

## Acceptance benchmark

Given an SSRS report with named metrics, filters, parameters, exports, security and business tasks, an acceptable migration produces:

- a complete inventory and baseline;
- governed Snowflake facts and dimensions;
- one Snowflake Semantic View containing required metric logic pending the metrics-model decision;
- one per-report golden dynamic table, or a recorded authorised exception;
- a Sigma workbook with no undeclared production modelling;
- aligned-cutoff parity evidence covering every mandatory metric and business task;
- BI Analyst approval followed by business-owner acceptance;
- production promotion and seven-calendar-day hypercare evidence;
- retirement evidence only after the exit conditions pass.

A migration missing any mandatory item does not meet the 95-point operational-confidence gate.

## Stop

Stop successfully when the Sigma report is accepted, promoted, has completed seven calendar days of clean hypercare, and SSRS is retired or has a documented authorised retention. Stop as blocked when a required source, access, owner, decision or material parity defect prevents the next safe state; name the missing evidence and owner.
