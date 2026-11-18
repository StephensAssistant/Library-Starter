---
id: SKILL-0030
type: skill
title: Learning Event Classification
status: current
created: 2026-09-05
updated: 2026-10-16
owner: Library owner

trigger_phrases: [classify learning event, learning signal, guidance outcome]
links: [FLOW-0001, FLOW-0002, PLAY-0041, PLAY-0046, PLAY-0056]
tags: [skill, library-mechanics, learning, classification]
---

# Learning Event Classification

Classifies one observed guidance outcome into one primary learning event.

## When to use

Activate at task routing, every correction or contradiction, and task completion. Select one event even when the result is `no-signal`.

## Method

1. Record observable outcome evidence; confidence, popularity and repetition are not fitness evidence.
2. Classify exactly one primary event: integrity-failure, guidance-conflict, routing-ambiguous, missing layer, guidance-failed, guidance-missed, hat-boundary-crossed, guidance-success, task-local, insufficient-evidence or no-signal.
3. Apply that precedence order when several descriptions appear applicable.
4. Map success to keep; missed/failed to bounded adjustment; conflict/integrity/ambiguity to stop-and-review; missing layer to its governed asset route; Hat boundary to switch; and local/insufficient/no-signal to no-change. Apply the Library owner's standing authority under AGENTS: a verified reusable missing Skill must be created on staging, and an existing Skill gap must be repaired there. Proposals remain necessary outside that bounded authority. Use PLAY-0041's event labels and repair receipt format unchanged.
5. Emit the minimal signal:
   `LEARNING-SIGNAL: <occurrence ID> | <asset ID or missing layer> | <event type>`
   `OUTCOME-EVIDENCE: <observable result or source>`
   `ACTION: <mapped action>`
6. Route proposals, validation, patterns, missing assets, Hat transitions and receipt formats to their focused Skills.

## Benchmark case

the Library owner restates an applicable stop rule that the AI missed: classify `guidance-missed`, cite the observed miss and retain PLAY-0041's `propose-adjustment` event label. Investigate and stage a verified bounded existing-Skill repair under the Library owner's standing authority when applicable; otherwise record the exact evidence, authority or decision blocker. Do not claim capture before the canonical source change is staged or independent acceptance before its separate review.

## Anti-patterns

- Treating repetition as proof
- Emitting several primary events
- Rewriting guidance after success
- Calling an unapproved proposal captured
- Manufacturing a signal where none exists

## Stop

Stop when one evidenced primary event and its mapped action are recorded.
