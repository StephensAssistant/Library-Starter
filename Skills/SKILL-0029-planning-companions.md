---
id: SKILL-0029
type: skill
title: Planning Companion Creation
status: current
created: 2026-09-05
updated: 2026-10-13
owner: Library owner

trigger_phrases: [create planning companion, add live plan, initialise ticket plan]
links: [PLAY-0049]
tags: [skill, library-mechanics, planning, creation]
---

# Planning Companion Creation

Creates the proportionate work plan selected under PLAY-0049 and maintained under PLAY-0050.

## When to use

Use when authorised work needs a usable plan. Small work uses an inline Work plan in the parent; create one linked companion when substantial sequencing or dependencies need it. Preserve an existing used plan and its history. Link-only bookkeeping does not trigger creation.

## Method

1. Keep outcome, acceptance and authoritative state in the parent. For small work, use an inline Work plan checkbox list and name the next executable step; do not force a separate companion.
2. When substantial work needs a companion, use one file named `Planning/<PARENT-ID>.md`, with no slug, and `Parent: [[<PARENT-ID>]]`.
3. For that companion, add `Live plan: Planning/<PARENT-ID>.md` to the parent and verify the exact reciprocal pointer.
4. Include Objective, Work plan and Next executable steps; retain existing useful sections/history and add further detail only when it changes execution or acceptance.
5. Preserve unknowns and material dependencies honestly; do not require empty ten-section boilerplate for small work.
6. Keep authoritative status, work_state, priority, due date, owner, blocker, evidence, decisions and next_action on the parent.
7. Split independently managed outcomes into separate governed parents, never a second plan.
8. Route maintenance, parent reconciliation, staleness and closure to their focused Skills.

## Benchmark case

A one-step legacy Ticket receiving a bounded correction uses an inline Work plan and clear next action. A substantial migration uses one linked companion with Objective, Work plan, Next executable steps and exact parent/backlink integrity.

## Anti-patterns

- Adding a slug
- Copying another parent’s pointer
- Creating a second live plan
- Forcing a separate ten-section companion onto small work
- Treating a plan checkbox as parent completion evidence

## Stop

Stop when the next executable action is clear in the proportionate plan. When a companion is used, verify its exact parent/backlink integrity. A plan is not completion evidence or authority to create extra work.

