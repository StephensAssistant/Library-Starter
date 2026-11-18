---
id: SKILL-0014
type: skill
title: Outcome-Based Work Breakdown
status: current
created: 2026-08-29
updated: 2026-10-31
links: []
tags: [project-management, work-breakdown, planning]
trigger_phrases: ["break this down", "work breakdown", "delivery steps"]
---

# SKILL-0014 — Outcome-Based Work Breakdown

## Purpose

Decompose one accepted outcome into evidence-verifiable milestones, deliverables and executable steps.

## Intent routing contract

Activate only for break this down, work breakdown, delivery steps or equivalent intent. Use associated records for their own jobs; this Skill does not silently expand into adjacent work.

## Method

1. Start from the accepted outcome and inspect current governed work before creating gaps.
2. Decompose outcome to observable milestones, deliverables and atomic verb-led steps.
3. Give each step one outcome, one owner or authority boundary and one completion evidence item.
4. Separate build, validate, external/waiting, decision/sign-off and release/closure work.
5. Represent temporary parity and the final end state as separate milestones.
6. Stop decomposition when more detail would not change the next actor, evidence or dependency.

## Anti-patterns

- Creating tasks before checking existing governed work.
- Breaking down technical activity without acceptance evidence.
- Treating a workaround or implementation finish as final acceptance.

## Benchmark case

For a report migration, a passing breakdown separates source preparation, build, parity validation, independent approval, release and hypercare, each with a provable acceptance result.

Missing-input design case: a migration outcome is named but final acceptance is undefined. Inspect the parent and existing plan, then identify the missing acceptance decision; do not convert a list of technical activities into apparently verified delivery milestones.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the parent outcome or acceptance boundary is missing, or the work contains independent outcomes that require separate governed records.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; former combined responsibilities moved to independent Skills while preserving existing links.

## Matt Pocock method extension — 2026-10-10

Decompose an agreed specification into end-to-end vertical slices. Start with a small tracer slice that traverses the real integration path and proves a useful behaviour; each subsequent unit has observable acceptance, prerequisites and a bounded change. Prefer slices that can be reviewed independently over layers that leave every unit unusable. For a broad refactor, use expand–migrate–contract so compatibility holds while callers move. Draft task content in the existing planning owner; decomposition does not authorise creating external issues or adding scope.

## Source adaptation — 2026-10-10

[to-tickets](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.
