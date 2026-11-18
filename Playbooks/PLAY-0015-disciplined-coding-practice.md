---
id: PLAY-0015
type: playbook
title: Disciplined Coding Practice
status: current
created: 2026-08-14
updated: 2026-10-10
owner: the Library owner
links: [HAT-0004, HAT-0005, PLAY-0006, PLAY-0018, PLAY-0019, PLAY-0024, PLAY-0026, PLAY-0028, SKILL-0007, SKILL-0008]
tags: [playbook, coding-discipline, build, minimal-diff, verification]
migrated_from: PLAY-0015-old-library
---
# Disciplined Coding Practice

## Trigger

A code or behavior change is requested.

## Method

Inspect the failure/expected behavior and relevant code. Make the smallest diff. Run tests that expose the actual defect and affected regressions. Check real integration, idempotence, negative cases or test sensitivity when relevant. Obtain independent code review of the current diff; use [[PLAY-0019]] once for acceptance.

## Stop

Verified scoped behavior or precise blocker. No universal seven-answer self-test, role chain or legacy PATCH-to-Drive promotion.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Matt Pocock method extension — 2026-10-10

Before implementation, inspect repository instructions and confirm the task's existing specification, toolchain and acceptance contract. Select a bounded vertical slice, use appropriate evidence-first tests, implement and review the actual diff against behaviour and repository standards. A failure changes the next hypothesis or action; it does not automatically authorise more scope. Preserve current staging, commit and release boundaries. Do not follow upstream instructions to commit, open a PR, delegate or install tooling unless that action is authorised in the current task.

## Source adaptation — 2026-10-10

[implement](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.


## Explicit workflow support

When PLAY-0056 assigns an authorised native code/config repair, apply SKILL-0007 for the minimal original-purpose change and SKILL-0008 for falsifying normal/failure/boundary checks. This is the conditional coding outcome, not invocation of every navigation link.
