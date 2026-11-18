---
id: SKILL-0289
type: skill
title: Sigma Email Burst Configuration
status: current
created: 2026-09-21
updated: 2026-10-31
owner: Library owner

links: [SKILL-0270, SKILL-0271]
tags: [skill, sigma, export, email-burst]
trigger_phrases: [sigma email burst, burst sigma report, split sigma export by recipient]
---

# Sigma Email Burst Configuration


## Intent-routing contract

Activate only when one export must be partitioned by data value and delivered to recipient mappings. Standard recurring exports use SKILL-0287.

## When to use

Use for ad hoc or scheduled recipient-specific report delivery driven by a column-sourced control.

## Method

1. Verify the **Export as email burst** permission, document access, recipient-domain policy and Cc/Bcc allowlists.
2. Build a column-sourced list control whose split field is text or number.
3. Keep the dynamic-recipient column in the same source as the split control; parse comma-separated addresses deliberately.
4. Select the split control, dynamic recipients, standard recipients and attachments from a published or tagged document.
5. Keep split values at or below 500, dynamic recipients at or below 500 and dynamic-plus-standard recipients at or below 1,000.
6. Count one render/query per split value and design the batch to finish within 30 minutes.
7. Prepare a reviewable burst configuration and representative split-value/recipient run for the Library owner to execute under the current communications contract. Validate restricted data, static-recipient behaviour and attachment size from actual run evidence; configuration alone does not prove delivery.
8. Assess observed duration, query volume and failures before proposing scaling. This Skill does not authorise sending or schedule activation; preserve current explicit user instruction precedence.

## Verified behaviour boundary

Saved-view-only elements are unsupported. Dynamic recipients have no unsubscribe option. Static recipients receive every generated attachment; Cc/Bcc recipients can receive one copy for each dynamic and standard delivery.

## Benchmark case

A department report splits on Department, resolves each department's authorised address from the same source and supplies a one-department security and attachment test for the Library owner; record a pass only after actual authorised run evidence exists, before proposing full delivery.

## Anti-patterns

- Using a manual list instead of a column-sourced split control.
- Mapping recipients from a different data source.
- Assuming one query serves all split values.
- Sending a full-scale burst before testing one mapping.
- Treating Cc/Bcc as a single audit copy.
- Promising unsubscribe to dynamic recipients.

## Stop

Stop with one reviewable burst configuration and verified recipient mapping. Claim tested or delivered only for actual evidenced authorised runs; otherwise name the exact authority, permission, mapping, limit, timeout or security gap.


## Destination verification

Check the live tenant, current API schema, intended recipient and permissions before preparing a schedule. Keep design and mutation approvals separate. Verify exact settings and status with readback, and use delivery evidence before claiming delivery. Confirm paused schedules retain their intended settings. If a mechanism is unsupported or readback differs, stop and investigate before switching delivery routes.
