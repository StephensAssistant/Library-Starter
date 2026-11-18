---
id: SKILL-0015
type: skill
title: Dependency Analysis
status: current
created: 2026-08-29
updated: 2026-10-31
links: []
tags: [project-management, dependencies, blocking]
trigger_phrases: ["what blocks what", "dependency analysis", "analyse dependency blocker"]
---

# SKILL-0015 — Dependency Analysis

## Purpose

Identify and evidence the states that constrain progress or final acceptance.

## Intent routing contract

Activate only for what blocks what, dependency analysis, waiting or blocked or equivalent intent. Use associated records for their own jobs; this Skill does not silently expand into adjacent work.

## Method

1. Read the current parent, plan and confirmed links before asserting a dependency.
2. Classify each dependency as hard, soft/preference, external/source, decision/sign-off or temporary/interim.
3. State the contract: A cannot achieve a named acceptance condition until B provides a specific state or evidence.
4. Distinguish execution from completion dependencies and waiting from blocked.
5. Record upstream state, downstream acceptance effect, evidence, owner, current state and workaround semantics.
6. Close or supersede an edge when direct evidence changes it.

## Anti-patterns

- Inferring dependency from shared technology or tags.
- Calling every external wait blocked.
- Removing a final dependency because an interim bridge permits progress.

## Benchmark case

If a report can be built against a bridge but cannot complete until a native source arrives, a passing analysis records progress as available while retaining the native-source completion dependency.

Near-miss design case: two Tickets share a platform but neither supplies a state required by the other. Record no dependency from that overlap; require the specific upstream state and downstream acceptance effect before adding an edge or calling work blocked.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when a material dependency lacks direct evidence; surface it as unknown rather than drawing the edge.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; former combined responsibilities moved to independent Skills while preserving existing links.

## Matt Pocock method extension — 2026-10-10

Translate the confirmed specification into a dependency graph, separating prerequisites, independent work and the critical path. Select the smallest actionable frontier, keep acceptance evidence attached to each node, and reassess after actual results. Parallel execution is appropriate only when the session explicitly permits delegation and work/state ownership will not collide. A graph is not permission to spawn agents, share a dirty worktree, publish or implement unsettled requirements. Keep one canonical plan and mark blocked nodes with the actual missing decision.

## Source adaptation — 2026-10-10

[implement-spec](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement-spec/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.
