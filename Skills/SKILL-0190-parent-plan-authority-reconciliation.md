---
id: SKILL-0190
type: skill
title: Parent–Plan Authority Reconciliation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["reconcile parent and plan", "plan conflicts with ticket", "sync canonical next action"]
links: [PLAY-0050]
tags: [skill, library-mechanics, planning, authority]
---

# Parent–Plan Authority Reconciliation

Reconciles execution detail with the parent record’s authoritative state.

## When to use

Use when a Project/Ticket and its live plan disagree or plan evidence changes canonical state.

## Method

1. Treat the parent as owner of status, work_state, priority, due date, owner, blocker, evidence, decisions and canonical next_action.
2. Treat the plan as owner of steps, sequence, dependencies, RAID and working notes.
3. Repair the parent from evidence first when they disagree.
4. Reconcile the plan to the repaired parent.
5. Before validation, update the parent for material scope, blocker, decision, due, lifecycle or next-action changes.

## Decision and evidence details

Retain the conflicting parent/plan claims and the evidence used to repair authoritative fields. Parent ownership determines where state belongs; it does not turn an unsupported parent value into proof. If the governing evidence is absent or contradictory, hold the dependent state change and record the gap before synchronising.

Boundary design case: the plan says done while neither record has acceptance evidence. Do not promote done to the parent merely to make the records agree.

## Benchmark case

A checked plan step conflicts with an active parent; evidence updates the parent first, then the plan follows.

## Anti-patterns

- Choosing whichever record is convenient
- Letting a checkbox override evidence
- Storing canonical status only in the plan

## Stop

Stop when authority fields and execution detail agree with evidence.
