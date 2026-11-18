---
id: SKILL-0191
type: skill
title: Active Plan Staleness Review
status: current
created: 2026-09-20
updated: 2026-10-13
owner: Library owner

trigger_phrases: ["stale live plan", "seven day plan review", "last meaningful update"]
links: []
tags: [skill, library-mechanics, planning, staleness]
---

# Active Plan Staleness Review

Determines whether an existing plan's stale claims affect the next authorised action.

## When to use

Use when a requested review or resumed Ticket/Project exposes potentially stale execution detail. A date alert does not create a compulsory portfolio or forecasting cycle.

## Method

1. Read the parent, its used plan and current acceptance/dependency evidence under PLAY-0050; the parent owns authoritative state.
2. Check whether a dated claim, open step or dependency still reflects current evidence and changes the next action.
3. Treat `Last meaningful update: YYYY-MM-DD`, when present, or a generated seven-day alert as discovery evidence only. Absence of that optional marker is not automatically a health defect, and elapsed days alone do not prove the plan's claims false.
4. Reject cosmetic edits, rolled dates, rewritten prose or unsupported ticks as evidence of progress.
5. Repair only evidenced contradictions affecting resumption within authority, preserving history; otherwise record the specific evidence gap or no-change result. Do not invent a review commitment or rewrite unaffected planning detail.

## Benchmark case

A plan's metadata changed yesterday but an old dependency claim conflicts with the verified current source: correct that blocking claim and next action. A seven-day alert with unchanged valid requirements does not by itself require a new plan or portfolio review.

## Anti-patterns

- Treating metadata churn as progress
- Treating a missing optional date marker or elapsed time as proof of stale claims
- Reviewing dormant transition backlog as active debt
- Repairing unaffected plan detail merely to clear an alert

## Stop

Stop when the next authorised action has a current evidenced plan, or name the precise stale claim or missing evidence that blocks it. Do not launch an automatic review cycle.
