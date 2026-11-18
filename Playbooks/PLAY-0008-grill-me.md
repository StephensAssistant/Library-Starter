---
id: PLAY-0008
type: playbook
title: Grill Me — superseded Playbook classification
status: superseded
created: 2026-08-14
updated: 2026-10-15
owner: the Library owner
links: [PLAY-0006, PLAY-0007, PLAY-0009, PLAY-0010, PLAY-0021, PLAY-0030, PLAY-0035, SKILL-0318]
trigger_phrases: ["grill me","challenge my decision","decision interrogation","align on a consequential decision","decide the correct next steps","revisit a decision during implementation","use decision answers to select capabilities","grow me","grill me in rounds","resolve guardrail confidence gaps"]
tags: [playbook, grill-me, framing, mission-control, decision-interrogation]
migrated_from: PLAY-0008-old-library
---
# Grill Me — Full-strength Decision Interrogation

> **Superseded 2026-10-15:** the Library owner confirmed Grill Me is a Skill, not a Playbook. Use `SKILL-0318`, which governs the exact upstream `grill-me` and required `grilling` Skills. This record remains only as classification and migration history; do not invoke it for current work.
>
> Confirmed historical ledger relationships remain in `links` solely to preserve immutable reciprocal graph evidence; they do not restore invocation authority.

## Trigger

A consequential unresolved decision affects the next action, at any stage of work; or the Library owner explicitly requests a plan interview or stress test. the Library owner's 10 October 2026 instruction gives standing invocation authority and makes this the number-one decision workflow for both assistants. Resolve evidence-backed routine execution directly; preserve PLAY-0008's existing ID.

## Method

1. Read the current goal, relevant records, settled answers and discoverable facts. Map the affected choices and dependencies; research facts before asking the Library owner to supply them.
2. Map the design tree and current decision frontier: all unresolved material choices whose prerequisites are settled. Ask the whole independent frontier in one numbered round, giving a concise recommendation and its basis for each question. Word questions so a clear yes can accept the recommendation where appropriate. There is no fixed total or per-round question limit: five, ten, twenty or more may be necessary; a simple decision may need only one. Do not manufacture questions about settled facts or pad a round to meet a quota. Questions depending on unanswered choices belong in later rounds. Wait for the relevant answers before taking dependent steps.
3. Incorporate each answer into the existing canonical work record/brief: decision, answer, rationale or constraint, scope/acceptance effect, agreed next steps and remaining choices. Treat proposals as proposals until accepted; do not create a second decision store.
4. After each answered round, assess the complete Hat roster, Skill catalogue, applicable Playbooks and confirmed dependencies under SKILL-0113. Read the selected contracts and use the complete applicable set for the next action; document material changes to the selection. Answers are routing evidence, not authority to invent IDs, relationships or permissions.
5. Recompute the frontier after each round, resolve contradictions and partial answers, and continue questioning until all material branches for the authorised outcome are settled. Do not end the interview after the first answer or merely because the question count is high. Confirm the shared outcome and correct next steps briefly from the resolved answers; obtain the Library owner's confirmation of shared understanding when the interview establishes a new or materially changed plan. Continue authorised work once its relevant decisions and checks are settled. If evidence, constraints, requirements or a result changes a decision, return to the affected question at that point in the workflow.

## Stop

All material branches relevant to the agreed outcome are settled and the shared understanding/steps/capability selection are confirmed, or precise unanswered questions block dependent work. Leave unrelated work moving. Reuse accepted answers rather than restarting the whole interview; further consequential decisions trigger this workflow again. Evidence, tool access and authority checks remain mandatory.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Matt Pocock method extension — 2026-10-10

Read the proposal and available code/documents before asking questions; answer source-verifiable facts yourself. Identify dependent choices and focus interrogation on the current decision frontier. Use the upstream independent-frontier rounds: number every presently answerable material question, give a reasoned recommendation, wait for the answers, then incorporate them and prune obsolete branches. the Library owner's 13 October 2026 instruction replaces the former local one-question-at-a-time restriction. For software semantics, consult the canonical domain glossary and decision record rather than manufacturing parallel documentation. Stop once the relevant decisions are settled or a named external answer blocks progress.

## Source adaptation — 2026-10-10

[grill-me](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grill-me/SKILL.md), [grilling](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grilling/SKILL.md), [grill-with-docs](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/grill-with-docs/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Decision-priority benchmark cases

- Positive: a mid-implementation discovery changes the trade-off; invoke Grill Me before choosing, then use the answer to reselect the complete applicable capabilities and revise the steps.
- Reuse: a later review still fits accepted scope; reuse the decision rather than asking the same question again.
- Negative: a clear read-only fact lookup with no consequential unresolved choice proceeds directly.
- Authority: deciding an implementation approach does not authorise deployment, scheduling, sending or merge.

## Guardrail escalation and source verification — 13 October 2026

the Library owner requested a process guardrail Hat and restoration of the upstream multi-question method. “GrowMe” in this request is resolved to this existing Grill Me owner by the prior named workflow and verified upstream source; no duplicate Skill is created.

When a material action fails AGENTS.md's 95 gate, identify the missing evidence, authority, access, requirement, decision or verification. Investigate facts through authorised tools; ask the Library owner the remaining independent human-owned decisions in a numbered round. A user's answer is not proof of access, a test, or an execution result. Stop the affected action until the answers and applicable checks resolve its gaps. Continue independent authorised fact discovery where possible.

Verified mattpocock/skills main on 2026-10-13 at commit 49dd158d1076134a641b33efb035946536778336: grill-me is a wrapper calling grilling; grilling explicitly asks the full independent decision frontier in rounds. This is the same revision already retained in the Library; the repair restores omitted upstream behaviour, not a claim of a newer release. Preserve the MIT licence already retained under Reference. External methods do not grant tool, send, schedule, deploy or merge authority; repository-supported invocation replaces unavailable upstream Skill-tool mechanics.

## Round and guardrail benchmark cases

- Five independent choices: ask Q1–Q5 together with recommendations, wait, record answers, recompute.
- Twenty independent material choices: ask all twenty; do not silently drop branches or stop after Q1.
- Dependency: a storage choice depends on the unanswered retention decision; ask retention now and storage in a later round.
- Partial/contradictory reply: retain settled answers, ask remaining or affected questions, and hold dependent actions.
- Already settled: a verified routine action proceeds without an invented interview.
- Confidence boundary: a claimed 98 with missing authority/access or required verification cannot authorise action; investigate facts and escalate unresolved choices.
- Authority: interview agreement and a score above 95 never grant unstated execution or release permissions.

RELATIONSHIP-EVIDENCE: PLAY-0008--SKILL-0318 | related_to | undirected | user_confirmed | superseded_by
