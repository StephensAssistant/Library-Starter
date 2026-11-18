---
id: PLAY-0072
type: playbook
title: Sigma Scheduling Manager — onboard one report
status: current
created: 2026-10-26
updated: 2026-10-26
links: [HAT-0016, HAT-0017, PLAY-0053, SKILL-0010, SKILL-0271, SKILL-0287]
tags: [playbook, sigma, scheduling-manager, snowflake]
---

# Sigma Scheduling Manager — onboard one report

## Trigger and intent routing contract

A named report must become eligible for scoped scheduling in a named environment. This Playbook owns preparation and onboarding to test-only eligibility. Distribution lifecycle belongs to PLAY-0073; deployment and promotion to PLAY-0074. It does not start business delivery.

## Inputs and supporting capabilities

Use the owner’s current scheduling-service handover for source limitations and PLAY-0053 for platform changes. SKILL-0287 owns standard scheduled exports, SKILL-0271 mechanism/tenant selection and SKILL-0010 row/measure reconciliation. HAT-0016 owns BI meaning and HAT-0017 security assessment. Require exact report/workbook/version/page/control IDs, source revision, current environment and actor permissions, report grain/filter semantics, approved test destinations and a scoped change request. Missing inputs stop their dependent step.

## Method

1. Resolve the current platform repository and deployed definitions. Confirm source freshness, owner/effective existing and future grants, Sigma access and responsible humans. Do not reuse truncated IDs from the handover.
2. Verify the serving object. Follow facts/dimensions → Semantic View → per-report golden dynamic table, or retain a documented authorised exception. Preserve report grain, measures and freshness. Do not rebuild a serving layer solely because the old document says Golden View.
3. Inspect the actual report YAML and SQL generator. Map each supported filter to verified columns/types. Define NULL/all, empty, invalid, overlap and leading-zero behaviour. Make proposed source changes through the platform's current branch/CI/human-review route.
4. Wire the exact Report_Scheduling control to scope-aware SQL and the published export source. Preserve interactive security separately. Scheduled absent/malformed scope must be refused; invalid nonempty scope must produce no restricted data.
5. Register through the current CI-owned REPORT_REGISTRY/REPORT_PARAMETERS procedure. Leave distribution unreleased and use NEVER or TEST_INBOX_ONLY; a UAT tag cannot release it.
6. Under separately authorised test execution, compare independently filtered source rows/keys and every relevant measure against at least two distinct scopes, shared/overlapping scopes, invalid/stale/inactive keys, all-value and empty selections. Check totals, formatting, attachments and data freshness. Confirm actual recipients/mailbox control. Written cases do not prove tests ran.
7. Only after isolation evidence, allowlist exact workbook/page/control/formats and TEST_INBOX_ONLY with evidence references. Use the currently verified schema and owner role, not illustrative INSERTs copied from the ZIP.
8. Handoff to PLAY-0073 with approved scope-to-target mappings, report revision, test results and remaining gaps. Production approval is separate.

## Verification and recovery

No source code or isolation tests were executed in the 26 October Library capture. Accept onboarding only with attributable evidence for the exact revision/environment. Missing source, failed reconciliation or unknown target proof leaves eligibility restricted. A mutation timeout requires read-only inspection for existing effects before a retry; do not duplicate report registrations or schedules.

## Benchmark case

A two-scope test report has independent expected rows/totals and an invalid-key no-data result, remains TEST_INBOX_ONLY and supplies a complete handoff. A missing scope, unreleased source or unexplained cross-scope row blocks eligibility. These are acceptance scenarios, not executed passes.

## Stop

Stop with one report demonstrably eligible for controlled tests and an evidenced lifecycle handoff, or the precise missing source/access/semantics/isolation evidence. No business send, activation or deployment.
