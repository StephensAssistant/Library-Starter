---
id: SKILL-0129
type: skill
title: Issue Management
status: current
created: 2026-09-20
updated: 2026-10-10
links: []
tags: [project-management, issues, resolution]
trigger_phrases: ["existing delivery issue", "defect management", "issue register"]
---

# SKILL-0129 — Issue Management

## Purpose

Manage an existing failed condition from evidence through resolution, acceptance or escalation.

## Intent routing contract

Activate only for existing delivery issue, defect management, issue register or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. State the failed condition, cause where known, affected outcome and dated evidence.
2. Distinguish source supplied no data from integration failed to ingest available data.
3. Record owner, response, next diagnostic or corrective action and closure evidence.
4. Keep technical completion separate from business acceptance or external waiting.
5. Close or reclassify accepted variance only with explicit decision evidence.
6. Synchronise material state to the governing parent and plan.

## Anti-patterns

- Calling an existing defect a future risk.
- Keeping accepted variance open indefinitely.
- Marking an issue resolved before corrective evidence exists.

## Benchmark case

For missing sales rows, a passing issue first determines whether the source delivered rows, assigns the correct owner, records the fix and closes only after reconciled output.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop closure when resolution evidence, owner or acceptance authority is missing.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.

## Matt Pocock method extension — 2026-10-10

Establish the actual issue and expected contract from source, reproduction and history before classifying it. Distinguish a defect, missing feature, already-fixed behaviour, duplicate and intentional/rejected behaviour; a prior rejection alone does not prove the present report is invalid. Draft a bounded implementation brief containing context, desired behaviour, acceptance evidence, affected area and explicit out-of-scope work. Treat researcher/clarifier/drafter as reasoning roles, not permission to spawn agents. Do not post, label, close or assign an external issue unless the task authorises that action.

## Source adaptation — 2026-10-10

[triage](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/triage/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.
