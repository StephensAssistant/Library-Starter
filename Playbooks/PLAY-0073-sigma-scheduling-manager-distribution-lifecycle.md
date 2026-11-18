---
id: PLAY-0073
type: playbook
title: Sigma Scheduling Manager — schedule and subscriber lifecycle
status: current
created: 2026-10-26
updated: 2026-10-28
links: [HAT-0017, HAT-0018, SKILL-0010, SKILL-0271, SKILL-0287]
tags: [playbook, sigma, scheduling-manager, snowflake]
---

# Sigma Scheduling Manager — schedule and subscriber lifecycle


## Current edit qualification hold — 28 October 2026

Before applying this procedure to the current Scheduling Manager pilot, read the18:39 checkpoint and ordered plan in TICK0203/KNOW0341. Native creation/pause is historicallyqualified foronejob; a laterattachment-onlyPATCHfailedother-settingsverification andA4restorationwasnotconfirmed. Existingjob286f69dc-1b96-4461-9502-ecf53c807594 mustremainpaused; do not replaytest/repair/CALL or treat it as a healthy source fornewsettings. Nextaction isread-onlyinspectionandactualpath-leveldiff, thenanexplicitreviewedrecovery. A sparse nested PATCH's unrelated-settingpreservation isnotqualified. Storebaselineanddiffs beforefurtherwrites; unknownGETtargetlistsremainunknown, notempty. CurrentPLAY0073 PathBexamples mustnotbeusedtooverrideTICK'sverifiednativeburstmechanismor silentlychangeitsdestination. No send/activation/repairauthorityiscreatedbythisdocument.

## Trigger and intent routing contract

Create, change, pause, retire or troubleshoot one report's app-managed distributions, including subscriber additions/removals/scope changes. Native email bursting is a separate SKILL-0289 mechanism; do not follow its automatic-recipient assumptions for Path B.

## Inputs and support

the owner’s current scheduling-service handover supplies the dated handover; SKILL-0287 owns scheduled export configuration and lifecycle proof, SKILL-0010 reconciles data, SKILL-0271 verifies supported mechanisms. HAT-0018 owns operations, HAT-0017 recipient/security controls. Require environment, exact report/workbook/schedule IDs, actor and approver, authorised old/new recipient scopes, report policy/version, time zone/cron and evidence destination. Communications remain the Library owner-executed under AGENTS; this procedure supplies no send/activation authority.

## Method

1. Read subscriptions, current scopes, app register and paginated Sigma schedule state. Distinguish app-managed from unmanaged schedules. Confirm actual approver, approved inbox control and report release policy; do not infer ownership or approval from access.
2. For an existing subscriber/scope change, identify every affected old/new scope and schedule. Pause and verify affected active schedules **before** changing subscriptions. If pause cannot be proved, stop the change and escalate; do not leave a removed recipient receiving while continuing.
3. Apply only the approved subscription change through the verified owner procedure. Recompute scope keys and recipients. The old key can remain valid for other subscribers. Preserve their distribution; never retire an entire shared scope merely because one person moved.
4. For an unchanged key, modify only while paused, re-sending the complete approved target list. For a new key, use a verified supported scope-change path or create a new paused schedule; retire obsolete schedules only after reconciliation and approval. Do not assume Modify can rebind scope merely because it can re-sync recipients.
5. For creation, save DRAFT, inspect the implementation's safe-creation/compensation design, then use Create in Sigma (paused) under its authority. Confirm the exact created ID and disabled state through the supported list endpoint before applying real timing. A placeholder December date is not a formal no-send guarantee.
6. Read back controls, pages, formats, cron/timezone and disabled state. Source says targets are absent from list responses: name a supported target-verification oracle, or mark target verification incomplete and hold activation. A 200 response or app register alone cannot prove Sigma recipients. Unknown PATCH fields may be ignored.
7. Prepare a scoped test to an owner-confirmed approved inbox for the Library owner to execute. Reconcile actual attachment rows/metrics and confirm receipt; no live test is run by this Playbook text. Validate positive/negative scope cases and source freshness.
8. Resume/activate only after authorised approval, recipient/scope proof and report policy pass. Record approving identity/time and final state. Check the next genuinely due execution with Europe/London/DST and evidence-lag allowance, then separately obtain receipt/attachment evidence.
9. For retirement, verify pause first, confirm the intended target, delete only the authorised managed schedule and retain audit/history; confirm absence from Sigma. Unmanaged schedules require their own owner-authorised route.
10. For a missing email, inspect expected due time, state, scope validity, source freshness, query/export evidence and lag, then mailbox/address/junk and attachment evidence. Zero rows are not automatically a scope failure. Manual exports may share scope tags. Do not treat query success as email delivery.

## Failure and recovery

On any failed/uncertain API action, preserve request ID/status, target IDs, known/uncertain effects and current register/audit; inspect current state before retrying. Never repeat unchanged payloads or create a duplicate after timeout. Failed pause/delete, missing recipient oracle, stale keys or cross-scope content blocks activation and routes to the owner. Preserve paused state where verified and repair only within authority. Do not manually alter DISTRIBUTION_AUDIT or the app register to manufacture consistency.

## Benchmark cases

- Shared scope removal: pause; remove one subscriber; retain the other subscriber's scope; apply complete remaining targets; prove target/content and approval before resuming.
- Changed scope with others remaining: preserve the old schedule for remaining subscribers and create/rebind the moved recipient's distribution without duplication.
- API returns 200 but readback differs, target verification is unavailable, or pause is uncertain: refuse activation, preserve evidence and investigate.
- Weekly schedule not due within 26 hours: no missing-run alert solely from that interval.

These are procedure checks. Verify runtime behaviour in the owner’s environment before accepting the change.

## Stop

Stop with the exact authorised schedule/subscriber change verified and evidence recorded, or a precise unresolved access/authority/state/target/delivery gap. No unstated send, schedule or repair effect.
