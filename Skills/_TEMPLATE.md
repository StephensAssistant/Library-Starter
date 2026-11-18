---
id: SKILL-<NNNN>
type: skill
title: <Reusable capability name>
status: current
created: YYYY-MM-DD
updated: YYYY-MM-DD
links: []
tags: [skill, <domain-tag-1>]
trigger_phrases: ["<specific user intent>"]
---

# <Reusable capability name>

<Class of work this Skill covers. Skills combine in a Playbook for one outcome; orchestration across Playbooks belongs in Workflows.>

## When to use

<Trigger or class of problem.>

## Intent routing contract

<User intent and natural paraphrases, owned technique, plausible near-miss exclusions and adjacent handoff owner. Align trigger_phrases with this scope. Similar wording alone does not establish applicability or execution authority.>

## Input and outcome contract

<Required inputs/types, authoritative source/revision/freshness, prerequisites, exact target/output, permitted effects and limits, acceptance predicate/tolerance and evidence oracle. Missing, contradictory or unevaluable required input is a gap; define its discovery/decision/failure route. A default requires an explicit condition and value.>

## Method

1. <Necessary action mapped to the intended outcome or named material-risk control; identify executor, allowed operation/effect, required evidence, observable success and immediate next/stop.>
2. <Account for every material decision in the owned technique: required evidence, exact branch condition, allowed action, resulting check/stop and owner. For failures state known/uncertain effects, retry safety, finite limits and affected re-entry. Omit an inapplicable mechanism only with its concrete reason.>

## Benchmark cases

- Normal: <representative inputs and independently expected result>.
- Failure/boundary: <material missing/contradictory input or unsafe effect and expected refusal/recovery>.
- Near-miss: <a realistic request sharing terms but requiring an adjacent capability; state the expected handoff or non-activation>.
- <Record actual verification separately; a written benchmark is not an executed PASS.>

## Sources and verification limits

<Source/date/revision, adapted technique, actual checks/results/evidence pointer and untested limits. Distinguish design, synthetic scenario, actual platform and independent review. Do not invent a runtime guarantee.>

## Anti-patterns

- <What not to do.>

## Stop

<Done condition or hand-off to a Playbook/work record.>


