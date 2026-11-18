---
id: SKILL-0271
type: skill
title: Sigma Automation Capability and Mechanism Selection
status: current
created: 2026-09-20
updated: 2026-10-26
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050]
tags: [skill, sigma, automation, capability-selection]
trigger_phrases: [choose sigma api cli or assistant, verify sigma automation capability, select sigma automation mechanism]
---

# Sigma Automation Capability and Mechanism Selection

Select the verified Sigma API, CLI, Assistant or manual mechanism that can perform one named lifecycle action.

## Intent-routing contract

Activate only to verify capability and choose the execution mechanism. Object discovery, mutation and export are separate Skills.

## When to use

Use before committing to an automated Sigma operation or when available mechanisms are uncertain.

## Method

1. Define the exact object type, action, evidence requirement and authority boundary.
2. Verify current official support, authentication, limitations and tenant availability for each plausible mechanism.
3. Exclude mechanisms that cannot satisfy the required object, action, concurrency or verification contract.
4. Compare operational complexity, repeatability, cost and security only among supported candidates.
5. Select one mechanism and record the evidence, constraints and handoff to the action-specific Skill.
6. Stop rather than inventing an API, CLI command, Assistant ability or successful access.

## Benchmark case

A workbook lifecycle task considers API, CLI and Assistant routes. A passing application verifies which routes support the exact action and selects the smallest supported mechanism with a read-back path.

## Anti-patterns

- Choosing from remembered rather than current capability.
- Treating similar object support as proof.
- Selecting a mechanism before defining the action.
- Executing the operation during selection.

## Stop

Stop with one evidenced mechanism and constraints, or the precise capability, authentication or tenant-availability gap.

## Scheduling Manager route selection — 26 October 2026

Verify current tenant capability and distinguish metadata discovery from executable export filters. Use the scheduling and burst skills for mechanism-specific checks.

Required inputs: exact tenant/object/action/environment, proposed mechanism, current source or official/tenant evidence, actor/access, permitted effects and observable state/target/delivery oracle. Output: one justified mechanism and its gaps. An API that cannot read recipient targets cannot satisfy a target-readback requirement merely by returning 200 on writes. Stop the dependent activation or obtain a verified supported oracle; do not broaden permissions or invent capability.

Failure boundary: investigate a changing input/capability before retry, preserve uncertain effects and avoid duplicate jobs. Benchmark: API 501 + older UI receipt leads to endpoint-specific evidence gathering and a bounded Path B alternative, with static-target reconciliation declared. This is source-grounded routing guidance, not runtime execution proof.

## Link review — 26 October 2026

- Confirmed result: `links_created`. Reciprocal navigation records the explicitly authored procedure/support/source dependencies in this source candidate. Existing links are retained; no typed or causal ledger claim is added.
- Contextual result: `no_contextual_links`. Useful source and procedure/support retrieval paths in the reviewed scope are already confirmed; no additional advisory pointer adds distinct value.
- Review scope: source-attributed documentation and direct navigation only. No runtime, non-author acceptance, approved FLOW or generated ledger/view changes are claimed. Endpoint existence and new reciprocal/contextual pairs are checked before source save.

## Metadata catalogue and filter-role routing — 26 October 2026


Require exact workbook/element/column IDs, source/export version, authorized visibility scope, complete pagination, sync status and approved semantic role/filter binding before offering a dimensional filter. A numeric datatype is neither a dimension nor a measure verdict. Column enumeration alone does not supply distinct values or wire a control into an export. If role/version/filter mechanism is unresolved, keep the field unavailable for the dependent scheduling action and record the exact gap.

A Snowflake copy has bounded freshness, not guaranteed live identity. Preserve the last coherent snapshot on partial/error reads, show staleness and revalidate affected configuration before create/modify/activate. Never infer deletion from a denied or incomplete listing. Benchmark: workbook rename preserves ID; numeric store dimension is eligible only with a verified binding; net-sales measure is excluded; removed/changed/unmapped column produces a blocked configuration rather than an unrestricted export.

