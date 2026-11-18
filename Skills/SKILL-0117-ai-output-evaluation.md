---
id: SKILL-0117
type: skill
title: AI Output Evaluation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [PLAY-0019, PLAY-0024, PLAY-0041, PLAY-0042, PLAY-0056]
tags: [ai, evaluation, quality]
trigger_phrases: ["evaluate AI output", "prompt result review", "AI response quality"]
---

# SKILL-0117 — AI Output Evaluation

## Purpose

Evaluate an AI output against explicit instructions, expert method, evidence and safety constraints.

## Intent routing contract

Activate only for evaluate AI output, prompt result review, AI response quality or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Extract material requirements and acceptance criteria before judging the response.
2. Check instruction retention, expert-method retention, factual grounding, completeness, concision and format compliance.
3. Map each material criterion to direct output evidence.
4. Identify unverifiable claims, unsupported inference, omitted constraints and unsafe actions.
5. Return a verdict, residual risk and the smallest corrective action.

## Anti-patterns

- Scoring style while ignoring factual grounding.
- Treating eloquence as completeness.
- Approving an output whose material criteria lack evidence.

## Decision and evidence details

Retain the evaluated output/version and map each material requirement to its exact passage and supporting source. Distinguish an instruction included in a plan from evidence that the instruction was executed. Mark unavailable factual or execution evidence as unresolved rather than awarding approval.

Boundary design case: a polished migration plan says parity testing passed but supplies no result. The evaluation records an unsupported completion claim and requests its evidence; the sentence itself cannot satisfy the test criterion.

## Benchmark case

For a generated migration plan, a passing evaluation maps every required control to text evidence and rejects the plan if access verification or parity testing is absent.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop approval when any material requirement, evidence source or authority boundary is unresolved.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
