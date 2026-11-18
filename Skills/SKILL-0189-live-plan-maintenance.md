---
id: SKILL-0189
type: skill
title: Live Plan Maintenance
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["update live plan", "maintain planning companion", "record plan checkpoint"]
links: [PLAY-0050]
tags: [skill, library-mechanics, planning, execution]
---

# Live Plan Maintenance

Keeps an existing live plan aligned with evidence as work progresses.

## When to use

Use at every meaningful execution checkpoint for an active Ticket or Project.

## Method

1. Mark complete only steps supported by evidence.
2. Add material dependencies, risks, assumptions, issues and decisions when discovered.
3. Resequence when evidence changes execution order.
4. Annotate deferred or cancelled steps without deleting history.
5. Align Current focus and Next executable steps; append an Update log entry.

## Decision and evidence details

Retain the checkpoint evidence and distinguish changes to execution detail from changes requiring reconciliation with the governing parent. The plan's focus and next executable work must agree with the supported state, not merely the most recent activity.

Boundary design case: a step appears complete but its acceptance evidence is missing. Leave completion unsupported, name the evidence gap and retain the history; a checkbox or recent update date cannot prove delivery.

## Benchmark case

A blocked task is annotated and resequenced; it is not checked complete or deleted.

## Anti-patterns

- Batching updates until session end
- Ticking unsupported boxes
- Deleting cancelled work

## Stop

Stop when the plan reflects current evidence, sequence, focus and next executable work.
