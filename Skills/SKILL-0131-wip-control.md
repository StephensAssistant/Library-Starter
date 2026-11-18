---
id: SKILL-0131
type: skill
title: WIP Control
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [project-management, wip, flow]
trigger_phrases: ["limit work in progress", "too many active items", "reduce context switching"]
---

# SKILL-0131 — WIP Control

## Purpose

Control attention-demanding work in progress to increase completion and reduce harmful context switching.

## Intent routing contract

Activate only for limit work in progress, too many active items, reduce context switching or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Separate active execution from waiting, review and queued work.
2. Count attention-demanding items rather than treating every open record equally.
3. Finish or unblock high-value near-complete work before starting more.
4. Use WIP limits as evidence-adjusted heuristics, not universal targets.
5. Choose which items to finish, pause, unblock or start and record the rationale.
6. Permit an urgent override only when an evidenced priority or commitment changes the order.

## Anti-patterns

- Starting every important item.
- Counting external waits as equal active load.
- Applying a fixed WIP limit without regard to work type.

## Decision and evidence details

Retain the current item/state inventory and the specific finish, pause, unblock or start decisions. Record the evidence behind any urgent override and re-evaluate the affected ordering when that commitment changes. Use observed attention demand, not an invented universal capacity threshold.

Boundary design case: several records are open but all await named external inputs. Do not count them as equal active execution load; identify any real chase/review work before imposing a new-start restriction.

## Benchmark case

When five Tickets are open but two await external owners, a passing decision focuses the actual three attention-demanding items and pauses a new start until one finishes.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when current work state or an overriding commitment is unknown.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
