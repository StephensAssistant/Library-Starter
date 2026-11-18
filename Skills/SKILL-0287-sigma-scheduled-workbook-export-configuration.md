---
id: SKILL-0287
type: skill
title: Sigma Scheduled Workbook Export Configuration
status: current
created: 2026-09-21
updated: 2026-10-28
owner: Library owner

links: [PLAY-0072, PLAY-0073, PLAY-0074, SKILL-0270, SKILL-0271]
tags: [skill, sigma, export, scheduling]
trigger_phrases: [configure sigma export schedule, recurring sigma workbook export, manage sigma export schedule]
---

# Sigma Scheduled Workbook Export Configuration

Configure and operate one recurring Sigma workbook export schedule. Artifact presentation and audience-split bursting use separate Skills.

## Intent-routing contract

Activate for recurrence, timing, execution identity, scheduled control values, conditional sending or schedule operations. Use SKILL-0270 for a one-off export.

## When to use

Use when a workbook, page or element must be exported repeatedly to an authorised destination.

## Method

1. Verify document access, destination permission, **Schedule export** permission, schedule ownership and execution identity.
2. Select the published workbook version, compatible tagged version or saved view; do not schedule an editing draft.
3. Resolve export scope, destination and a compatible format.
4. Configure frequency, timezone, control-value overrides and any conditional-send rule.
5. Decide whether queries run with creator access or recipient access. For **Run queries as recipient**, require Sigma users, cap recipients at 300 and account for one query per recipient.
6. Prepare one representative run for the Library owner to review and execute under the current communications contract; validate the resulting content, security scope, filters, destination and warehouse impact only from actual run evidence. A send or schedule activation is not authorised by this Skill.
7. Stagger high-cost schedules, monitor last-run state and correct failures before resuming.
8. Treat more than 10 consecutive failures as a suspension requiring the owner or an admin to modify the schedule.

## Benchmark case

A monthly workbook PDF runs on the first business reporting date with named control values and recipient-level security, then passes one representative send and warehouse-load check.

## Anti-patterns

- Scheduling an unpublished draft.
- Assuming scheduled exports reuse materialized results.
- Using creator-access data when recipient-level restrictions are required.
- Concentrating many expensive schedules at the same time.
- Treating schedule creation as proof of successful delivery.
- Mixing email-burst audience splitting into this Skill.

## Stop

Stop with a reviewable schedule configuration and named owner; claim a configured, test-run and monitored schedule only when those actions and their results are evidenced under current authority. Otherwise name the exact authority, permission, identity, destination, capacity or output gap.


## Destination verification

Check the live tenant, current API schema, intended recipient and permissions before preparing a schedule. Keep design and mutation approvals separate. Verify exact settings and status with readback, and use delivery evidence before claiming delivery. Confirm paused schedules retain their intended settings. If a mechanism is unsupported or readback differs, stop and investigate before switching delivery routes.
