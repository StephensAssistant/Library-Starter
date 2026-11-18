---
id: SKILL-0093
type: skill
title: AI Workflow Evaluation Design
status: current
created: 2026-09-20
updated: 2026-10-17
links: [SKILL-0007]
tags: [testing, ai-evaluation]
trigger_phrases: ["design an AI evaluation", "test a skill or prompt", "measure agent repeatability"]
---

# SKILL-0093 — AI Workflow Evaluation Design

## Purpose

Design held-out capability and regression evaluations for Skills, prompts, retrieval, agents or automations.

## When to use

Use for: design an AI evaluation; test a skill or prompt; measure agent repeatability.

## Method

1. Define the intended environmental outcome and mandatory constraints before changing the workflow. Specify each case's inputs, independent expected result, actual outcome oracle, acceptance predicate/tolerance, evidence source and freshness.
2. Select mechanical graders for exact checks; use calibrated independent model grading for qualitative results and human review for decisions whose governing contract requires it. Do not use the implementation's own success flag as the sole oracle.
3. Separate held-out capability cases from regression cases and development examples. Cover the material decisions, denied scope/access, missing/stale/conflicting evidence, partial effects, recovery and cancellation for the actual mechanism. Record a concrete reason when a case is not applicable.
4. Distinguish pass@k (at least one accepted success within k attempts) from pass^k (all k attempts accepted). Record k, actual outcomes, sample size, model/tool/environment versions and the estimator used. Do not present recoverability as repeatability or apply a probability formula without its assumptions.
5. Record the baseline, exact candidate/input/grader revisions, named execution owner, command/procedure, actual results, failures and one evidence location. Reuse valid execution evidence across independent review under Workflows/README.md's minimum-execution contract; review independence alone does not require rerunning it.
6. Measure cost and elapsed time per accepted outcome when efficiency is in scope; define the population/window, include failures/retries and distinguish active time from waiting. Report unexecuted cases and incomparable configurations explicitly. A higher success rate does not excuse a forbidden effect.

## Benchmark case

Evaluate a routing Skill across held-out ambiguous and clear requests, measuring repeatability without letting its own heuristic grade itself.

## Anti-patterns

- Training on held-out cases.
- Using the same heuristic to create and grade labels.
- Reporting averages without failure cases.

## Stop

Stop with a reproducible evaluation packet and baseline comparison.

## Research extension and verification boundary — 17 October 2026

A transcript says an export succeeded while the target lacks the required records: FAIL the outcome even if every tool call returned success. A review packet with proposed tests but no executions remains untested. Assess actual case outputs against the oracle; do not infer live reliability from synthetic cases. Source: [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), inspected 17 October 2026. This extension defines evaluation technique, not a measured improvement.
