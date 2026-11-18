---
id: PLAY-0065
type: playbook
title: Qlik-to-Sigma Reporting Migration
status: current
created: 2026-09-20
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [PLAY-0014, PLAY-0022, PLAY-0053]
tags: [playbook, qlik-sense, sigma-computing, migration, snowflake, reporting]
---
# Qlik-to-Sigma Reporting Migration

## Trigger

An existing Qlik app must be rebuilt in Sigma after, or independently of, its SQL Server-to-Snowflake source-only migration.

## Intent routing

Use this playbook when the Qlik front end itself is being replaced by Sigma. Use PLAY-0063 when only Qlik's SQL Server source queries are changed to Snowflake and the Qlik front end remains intact. Use PLAY-0064 for SSRS-to-Sigma migration.

This playbook owns Qlik discovery, semantic migration, Sigma construction, transition and route-specific acceptance. It inherits concept and expression discovery from PLAY-0014, shared parity/cutover/hypercare controls from PLAY-0022, and governed reporting-platform controls from PLAY-0053.

## Required outcome

For each Qlik app, replace the front end with a governed Sigma workbook while moving canonical modelling and metric logic into Snowflake:

1. Facts and dimensions.
2. Snowflake Semantic View containing or referencing the approved metric definitions.
3. Per-report golden dynamic table built from the Semantic View.
4. Sigma workbook as presentation and interaction only.

Use a golden view only when the Library owner explicitly directs it or evidenced requirements or technical constraints prevent the dynamic-table path. Record the exception.

## Method

### 1. Inventory the Qlik app

Capture the app identity, business purpose, owner, users, sheets, objects, dimensions, measures, variables, set analysis, load-script transformations, filters, selections, alternate states, drill paths, extensions, exports, schedules and every business task the Sigma replacement must support.

Discover Section Access, row-level restrictions and all other security rules. Inventory bookmarks, alerts, subscriptions, scheduled exports, user-created content and downstream dependencies. Identify a business owner; when none is recorded, identify an appropriate customer business user where possible.

Keep the existing production Qlik app live throughout build, validation and seven-calendar-day hypercare.

### 2. Map logic to governed Snowflake objects

Map Qlik data transformations, relationships and calculations to governed Snowflake facts and dimensions. Reuse approved objects before creating new ones. Do not reproduce production modelling or canonical metric logic in Sigma.

Treat the Snowflake Semantic View as the canonical metric source:

- when an approved required metric already exists, use it instead of recreating the Qlik expression in Sigma;
- when a required Qlik metric is absent, build and validate it in the Semantic View before constructing the Sigma output;
- when the Qlik result conflicts with an existing Semantic View definition, present both definitions and evidenced result differences to the Qlik app's business owner for a recorded decision;
- when no business owner is recorded, discuss the conflict within the BI team and try to obtain agreement from an identified customer business user; record the selected definition and approver before continuing.

For every object and layer, identify and verify required system, service-identity, developer and user access. Apply current-object and future schema grants for applicable object types unless an explicit narrower control is required. Determine ownership from verified current rules and comparable governed objects, then verify ownership and effective grants after every create or replace.

### 3. Build the report-serving object

Build one golden dynamic table per reporting purpose from the Snowflake Semantic View. Validate refresh behaviour, freshness, grain, keys, required fields, approved metric results, performance and cost.

### 4. Build the Sigma replacement

Use Sigma as the presentation and interaction layer only. Temporary test calculations must not become undeclared production dependencies; Sigma-specific capabilities such as write-back may be used only when explicitly required.

Keep the Sigma replacement recognisably close to Qlik for efficient customer transition. Apply deliberate improvements to usability, accessibility, visual consistency, professionalism and premium-product quality, pushing Sigma's verified capabilities without silently changing agreed behaviour. Broader redesign requires business-owner approval.

Map every required Qlik business task and feature to a Sigma equivalent. Reproduce every required bookmark, alert, subscription, scheduled export or downstream dependency, or obtain explicit business-owner approval to retire it.

### 5. Implement and test security

Where Qlik security exists, map Section Access, row restrictions and other rules to the governed Snowflake/Sigma control. Validate representative allowed and denied access before promotion. Missing or unverified security blocks promotion.

### 6. Prove parity and task completion

Compare Qlik and Sigma at an aligned data cutoff, accounting for approved metric-definition changes. Retain evidence for:

- approved metrics and documented expected variances;
- grain, rows, keys and representative records;
- filters, selections, interactions and drill behaviour;
- security and access;
- refresh freshness and performance;
- exports, dependencies and every required business task;
- explicitly approved retired features.

An unexplained material difference fails the gate.

### 7. Complete sequential acceptance

An identified non-author BI Analyst validates first. Correct and retest evidenced defects. The Qlik app's business owner then reviews and accepts the corrected replacement. If no business owner is recorded, identify an appropriate customer business user and obtain recorded acceptance; do not silently substitute AI or unrecorded internal assumption.

Before Sigma becomes primary, provide affected users with transition guidance covering changed navigation, controls, workflows and replaced or retired features.

### 8. Cut over and hypercare

After acceptance, make Sigma the primary report and begin seven calendar days of hypercare. Keep the existing Qlik app available as the temporary fallback.

the Library owner owns technical monitoring and remediation. The BI Analyst and business representatives report behavioural defects. Monitor refreshes, dynamic-table state and lag, metrics, access, performance and required business tasks. Fix and retest each material defect; unresolved or unverified material defects block exit.

### 9. Archive Qlik

After clean hypercare and the shared decommission gate, disable the Qlik app's reload schedule and archive the app outside customer access. Do not delete it. Retain the archived app until the Qlik platform itself is formally decommissioned.

## Branches

| Condition | Required path |
|---|---|
| Only the source changes and Qlik remains the front end | Leave this playbook and use PLAY-0063 |
| Required Snowflake source, fact or dimension is missing | Build or onboard it under the governed Snowflake path, then resume |
| Required metric is absent from the Semantic View | Build and validate it there before Sigma construction |
| Qlik and Semantic View metric definitions conflict | Obtain a recorded decision through the business-owner or fallback customer-user path |
| Security exists in Qlik | Map it and prove allowed/denied access before promotion |
| Dependency cannot be reproduced | Obtain explicit business-owner retirement approval or block |
| Broader redesign is proposed | Obtain business-owner approval before implementation |
| BI Analyst or business reviewer finds a defect | Fix and retest before promotion |
| Material defect appears during hypercare | Use Qlik as the temporary fallback while fixing and retesting |
| Hypercare passes | Disable reloads and archive Qlik outside customer access |

## Acceptance benchmark

Given a Qlik app with calculations, interactions, security and user dependencies, an acceptable migration produces:

- a complete inventory and named owner or fallback customer reviewer;
- governed Snowflake facts and dimensions;
- approved metrics in the Snowflake Semantic View;
- one per-report golden dynamic table, or a recorded authorised exception;
- a familiar but measurably improved premium-quality Sigma workbook with no undeclared production modelling;
- mapped and validated security;
- aligned-cutoff parity and required-business-task evidence;
- explicit decisions for metric conflicts and retired dependencies;
- BI Analyst approval followed by business acceptance;
- user transition guidance;
- Sigma-primary cutover, seven-calendar-day hypercare and Qlik fallback evidence;
- disabled reloads and archival outside customer access after a clean exit.

A migration missing any mandatory item does not meet the 95-point operational-confidence gate.

## Stop

Stop successfully when Sigma is accepted, primary, has completed seven calendar days of clean hypercare, and Qlik is archived outside customer access with reloads disabled. Stop as blocked when required source, access, owner, security, decision, parity or acceptance evidence is missing; name the blocker and responsible owner.
