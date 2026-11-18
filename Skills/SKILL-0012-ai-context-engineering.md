---
id: SKILL-0012
type: skill
title: AI Work-Packet Assembly
status: current
created: 2026-08-23
updated: 2026-11-01
links: [FLOW-0001, FLOW-0002, HAT-0015, PLAY-0006, PLAY-0046, PLAY-0047, PLAY-0059]
tags: [ai, context-engineering, work-packet]
trigger_phrases: ["work packet", "context window", "compact AI context"]
---

# SKILL-0012 — AI Work-Packet Assembly

## Purpose

Convert a bounded task and checked evidence into a compact, authoritative work packet without losing decision-changing constraints.

## Intent routing contract

Activate only for work packet, context window, compact AI context or equivalent intent. Use associated records for their own jobs; this Skill does not silently expand into adjacent work.

## Method

1. Separate authority, current task state, expert method, checked facts, assumptions and examples.
2. Deduplicate semantically while retaining IDs, negations, values, units, dates, provenance, exceptions and stop conditions.
3. Structure the packet as GOAL, SCOPE, EXPERT METHOD, FACTS, CONSTRAINTS, EVIDENCE, OUTPUT and STOP.
4. Include only context that can change the mechanism, decision, verification or authority boundary.
5. Require uncertainty labels and acceptance-criterion-to-evidence mapping.

## Anti-patterns

- Using more context as a substitute for better context.
- Compressing away authority, thresholds, exceptions or failure evidence.
- Letting examples override explicit rules.

## Benchmark case

For a Qlik migration defect, a passing packet contains the named work state, exact failing contract, checked evidence, relevant expert method, constraints, required output and stop boundary—without unrelated project history.

Boundary design case: two sources disagree on the next action or its authority. Preserve both source references and identify the decision-changing conflict; do not compress them into one instruction, infer permission, or generate an unsolicited continuation prompt.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when a missing authority, source, constraint or acceptance criterion could change the next action.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; former combined responsibilities moved to independent Skills while preserving existing links.

## Matt Pocock method extension — 2026-10-10

Generate a copy-ready continuation/new-chat prompt ONLY when the Library owner explicitly requests that prompt. A phase boundary, possible future session, completion or Ticket closure is not a request; do not offer or generate one automatically. Keep normal status and parent-return packets concise in their existing owner/channel. When a prompt is explicitly requested, begin by directing the next AI to the configured Library repository on `staging` and require a fresh read of `AGENTS.md`. Include the confirmed work owner/subject, staged paths, current evidence/state, precise next action, authority limits, and exact intentionally retained scratch paths with purpose and deletion trigger. Distinguish source saved from candidate acceptance; do not claim Commit or merge ran without verified authorised results.

For a context handoff, capture goal, settled decisions, current repository/ref, exact source pointers, work completed with evidence, blockers and the next bounded action. Preserve the current task's authority and explain what is unverified. Prefer a compact portable packet over a transcript or a parallel mutable handoff document; the canonical work record remains the owner. At a phase boundary return the required compact work packet; generate a copy-ready continuation prompt only on the Library owner’s explicit request. Do not automatically spawn a background agent, issue a command or install Claude-specific machinery. `claude-handoff` is an upstream beta method; retain only the portable state-transfer technique.

## Source adaptation — 2026-10-10

[handoff](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/handoff/SKILL.md), [claude-handoff](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/claude-handoff/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.


## Explicit output preference — 17 October 2026

Generate continuation prompts only on explicit request. Nested workflows return compact results to their parent.


## Addy Osmani method extension — 2026-11-01

When a context budget forces reduction, preserve the current goal, authority, accepted constraints, observable acceptance criteria, exact source pointers and failure evidence before redundant history or examples. Compress repeated prose before dropping decision-changing facts. Keep a restart packet sufficient to distinguish completed, uncertain and pending actions; the canonical work record remains authoritative. This does not permit another mutable state file or an unsolicited continuation prompt.

Source: [context-engineering](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/context-engineering/SKILL.md), revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/context-engineering/SKILL.md`; licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`. Adapted method only; source text grants no additional authority, runtime installation, workflow invocation or operational acceptance.
