---
id: SKILL-0320
type: skill
title: Workflow Decision Policy Design
status: current
created: 2026-10-17
updated: 2026-11-09
links: [PLAY-0069, SKILL-0313]
tags: [skill, workflow, decision-policy]
trigger_phrases: ["design workflow decision rules", "remove ambiguous workflow branches", "specify a decision table"]
---

# Workflow Decision Policy Design

## When to use and intent routing contract

Use to turn an agreed workflow/business policy into evaluable branch rules or assess ambiguous conditions. Own decision inputs, predicates, match semantics and rule tests. SKILL-0312 owns sequencing unresolved human decisions; SKILL-0318 owns the Library owner clarification; SKILL-0321 owns state/transition soundness. This Skill MUST NOT choose unagreed business policy, grant authority, install a rules engine or invoke a workflow.

## Input and outcome contract

Require the policy owner and authoritative current policy, intended decision/output, accepted scope, typed input domains, provenance/freshness and the calling state's contract. Output a rule table or equivalent predicate specification in the existing workflow/owner, mapped to existing branch destinations and verification cases. Approval requires an evaluable result for every valid in-scope input class and an explicit error route for invalid/unavailable evidence. Missing policy remains a gap, not a rule invented by the author.

## Method

1. Name the decision, owner and exact output domain. Inventory inputs with types, units, timezones, allowed values, boundary inclusivity, null/absent distinctions and evidence freshness. Define only semantics that apply to those inputs.
2. Express each condition as a testable predicate over those inputs. For qualitative judgement specify the rubric, evidence and deciding owner; do not claim deterministic equivalence.
3. Declare one match-selection policy: unique matching rule; ordered first match with explicit priority; or a defined aggregation of multiple matches. State ties/conflicts and the exact result. If the caller permits only one next state, multiple results require an explicit resolution rule compatible with that caller; do not silently select one.
4. Define valid no-match behaviour separately from invalid input/evaluation failure. In FLOW, retain exactly one otherwise branch for valid no-match; missing, stale, malformed, contradictory or unevaluable required evidence follows failure/shared recovery. A permitted default MUST name its triggering predicate and exact value. Do not use a catch-all as evidence of business-policy completeness.
5. Map rule outcomes to actual existing transitions and allowed effects. Verify that no predicate, priority or default bypasses prerequisite/authority gates or expands scope. Keep the rules beside the canonical decision contract; do not create a competing graph.
6. Design representative boundary/equivalence, overlap, no-match, missing/null/stale/conflict and evaluation-error cases. For a finite small domain, enumerate it; otherwise state the sampled/partitioned domain and unproved remainder. Derive expected results from the accepted policy independently of the implementation.
7. Record exact source/rule/input revisions, actual observed outputs, execution owner and one evidence pointer when tested. Reuse accepted evidence under Workflows/README.md; this Skill does not require duplicate execution for independent review. Hand a true policy gap to its owner; follow current SKILL-0318’s Method for the necessary material question when the Library owner owns the decision.

## Benchmark cases

- Normal: accepted policy says amount strictly greater than 100 requires review. Cases 99.99, 100 and 100.01 must produce the independently specified boundary results, using the policy's currency/precision.
- Conflict: two unique-policy rules match the same valid input -> reject the policy table until the owner resolves the overlap; do not choose the first row.
- Missing evidence: required permission evidence unavailable -> failure/recovery; it must not enter an otherwise "proceed" branch.
- Ordered policy: two matches under an explicitly accepted first-match priority -> the named priority selects one result; overlap is intentional rather than universally prohibited.

These are design scenarios. Actual verification and limits belong in the qualification evidence; the examples alone do not establish runtime correctness.

## Anti-patterns

- "Proceed if appropriate" without a predicate or rubric.
- Choosing a policy to fill a template, treating unknown as false, or silently prioritising overlapping rules.
- Forbidding all overlaps when an accepted aggregation/ordering policy intentionally permits them.
- Treating a diagram/default as proof of complete or safe decisions.

## Stop

Return explicit rules, destinations, tested/untested coverage and residual policy gaps. Withhold dependent approval/execution while a required input, rule or authority remains unresolved.

## Sources and verification boundary

[OMG DMN](https://www.omg.org/dmn/), inspected 17 October 2026, supports precise decision modelling alongside process models. This is an original Library design technique; no DMN engine or complete standards-conformance claim is introduced. Source-only creation under the Library owner's instruction; allocator issue455 returned this ID. See the workflow qualification record and Reference/workflow-quality-research-20261017-v1.md for actual qualification.
