---
id: SKILL-0192
type: skill
title: Plan Closure Reconciliation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["close live plan", "open checklist on done ticket", "retain plan history"]
links: []
tags: [skill, library-mechanics, planning, closure]
---

# Plan Closure Reconciliation

Reconciles a live plan before its parent closes.

## When to use

Use during Ticket or Project closure or when a done parent still has open plan work.

## Method

1. Retain the plan as execution history.
2. Review every open checklist item against evidence.
3. Close, defer or cancel each item truthfully; unresolved executable work blocks closure.
4. Do not tick items merely to pass validation.
5. Reopen a done parent before adding genuine new live work.

## Decision and evidence details

For each open item, retain the actual disposition and its evidence or authorised deferral/cancellation decision. Reconcile the parent and remaining work before declaring closure; preserving history includes unexecuted work truthfully.

Boundary design case: a planned test is no longer required under an evidenced scope decision. Record cancellation with that reason rather than falsely marking the test executed. Genuine unresolved executable work still blocks closure or requires reopening.

## Benchmark case

A done Ticket has one unexecuted step; it is reopened or closure is blocked rather than falsely checked.

## Anti-patterns

- Deleting the plan at closure
- Falsifying checklist completion
- Adding live work to a done parent

## Stop

Stop when no unresolved executable work remains, or when the parent is reopened.
