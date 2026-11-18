---
id: PLAY-0074
type: playbook
title: Sigma Scheduling Manager — administration and release readiness
status: current
created: 2026-10-26
updated: 2026-10-26
links: [HAT-0016, HAT-0017, HAT-0018, PLAY-0053, SKILL-0271, SKILL-0287]
tags: [playbook, sigma, scheduling-manager, snowflake]
---

# Sigma Scheduling Manager — administration and release readiness

## Trigger and intent routing contract

Maintain the Scheduling Manager service, diagnose credentials/runtime failures, or assess a requested environment promotion. PLAY-0072 owns report onboarding; PLAY-0073 owns schedule/subscriber operations. This procedure does not create a recurring monitor or approve release.

## Inputs and support

the owner’s current scheduling-service handover preserves the source inventory and limitations. PLAY-0053 governs platform code/config/documentation changes; SKILL-0271 verifies actual mechanisms and SKILL-0287 supplies recurring-delivery proof. HAT-0018 owns service operations, HAT-0017 privileges/secrets, and HAT-0016 report assurance. Require exact source/deployed revision, environment, system/actor access, current owner/grants, authorised effect, test/evidence paths, service owner and recovery route.

## Method

1. Obtain the repository URL and immutable commit, source/config/dependencies, current DDL/grants/ownership and deployment evidence. Verify the supplied feature branch matches the deployed app; a branch label alone is not a version.
2. Inspect distribution_schema.sql, deploy_streamlit_dev.sql and create_dist_sigma_secrets.py before use. Source reports CREATE OR REPLACE with viewer regrants and a CLI ownership pitfall. Verify actual role selection, source PUT inventory and grant preservation; do not execute illustrative commands or substitute environment strings blindly.
3. Verify owner-rights viewer identity/approval checks, admin-only approver writes, least privilege, secret mapping/egress, controlled PyPI dependency installation and separate app warehouse. Store no credentials in Library. Replace personal Sigma credentials with an approved service identity before UAT through the authorised secure route.
4. Before an authorised deployment, run the actual unit suite and read-only DEV smoke tests against pinned inputs; browser-test the Snowsight app and identity. Mutation/UI tests and send-now tests require their distinct authority and controlled workbook/inboxes. Retain commands/results/coverage; a source assertion of 20 passing tests is not new execution evidence.
5. After any replacement, verify app owner, viewer access, effective existing/future grants, package/network access, identity, approvals and no unintended schedule effects. Use the platform's required human review, CI and explicit environment release gates.
6. For routine diagnosis, distinguish authentication failure, warehouse queue/runtime, stale report data, schedule drift, query/export failure and mailbox delivery. Use exact logs without secrets. Schedule monitoring must calculate expected runs by cron/timezone/DST and account for query-history lag; fixed 26-hour checks apply only to a suitable daily schedule.
7. Require each release prerequisite: owner-confirmed DEV inbox/attachments; service credentials; one release report passing isolation; verified UAT deployment path; named service/support/approvers; financial certification where relevant; source/target evidence; explicit production authority and operational recovery.
8. Progress DEV → UAT → production only through current authorised platform gates. Existing DEV scripts are not proof of a tested promotion mechanism. Apply seven-calendar-day production hypercare and do not close with material unresolved/unverified defects.
9. Native-burst reconsideration requires current tenant-specific official/actual evidence and a separately tested migration/target-isolation plan. Do not replace Path B because a generic product page says bursting exists.

## Failure and recovery

Stop the affected effect when source, identity, ownership, target proof or environment mapping is missing/conflicting. Preserve known deployment/schedule state and request evidence; diagnose before retrying. Redeploy is described as a container restart, not proof that a broken credential or deployment is repaired. No unapproved production modification, credential disclosure, guessed IDs or emergency grant expansion.

## Benchmark cases and verification limits

An authorised DEV redeploy preserves owner/access and passes pinned unit/smoke/browser evidence; a UAT request with only uninspected DEV scripts stops for mapping/source proof. A scheduled query run without inbox confirmation remains delivery-unverified. No deployment, live test, credential rotation or promotion was performed during 26 October documentation capture.

## Stop

Stop with the exact authorised maintenance result proved, or a release-readiness packet naming remaining evidence, owners and next action. No automatic promotion, send, schedule, validation pipeline or merge.
