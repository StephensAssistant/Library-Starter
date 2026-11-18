---
id: SKILL-0160
type: skill
title: Change Authority and Sign-off Routing
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, change-control, authority, signoff]
trigger_phrases: [identify change approver, route sign off, who can approve change]
---

# Change Authority and Sign-off Routing

Identify and route a change or acceptance decision to the evidenced authority.

## When to use

Use when scope, spend, production release, business acceptance or final sign-off requires a named decision-maker.

## Method

1. Separate requester, implementer, reviewer and decision authority.
2. Verify the authority from current evidence; do not infer it from seniority or involvement.
3. Route the decision with the change, impact and required acceptance evidence.
4. Keep build, UAT, production approval and final acceptance as separate states.
5. Record deferred sign-off as waiting on the named authority.

## Decision and evidence details

Retain the decision being requested, current authority source, named decision owner, evidence packet and actual sign-off state. If sources identify conflicting approvers, resolve that conflict before treating either as authorised; do not convert technical review into business or release acceptance.

Boundary design case: the requester says testing is complete but production approval ownership is unknown. Record test evidence separately and return the precise authority gap without claiming release approval.

## Benchmark case

A stakeholder requests and tests a change but cannot approve production. A passing application records their roles separately and routes release approval to the evidenced authority.

## Anti-patterns

- Assuming the requester can approve.
- Treating technical completion as acceptance.
- Calling deferred sign-off a technical blocker.

## Stop

Stop when the decision owner, required decision and current sign-off state are explicit.
