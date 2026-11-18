---
id: SKILL-0321
type: skill
title: Workflow State Soundness Assessment
status: current
created: 2026-10-17
updated: 2026-10-17
links: []
tags: [skill, workflow, state-machine, verification]
trigger_phrases: ["assess workflow soundness", "check semantic workflow transitions", "find deadlocked workflow states"]
---

# Workflow State Soundness Assessment

## When to use and intent routing contract

Use when designing/reviewing workflow states, guards, parallel joins, waits, loops or completion. Own semantic analysis of the declared state model. SKILL-0320 owns decision policy, SKILL-0093 outcome evaluation, and check_workflows.py structural admission. This Skill MUST NOT claim a formal proof from a diagram, approve its author's work, invoke an unapproved FLOW or install a model checker.

## Input and outcome contract

Require the exact workflow-json, current component/recovery contracts, acceptance predicates, guard/input domains, concurrency/effect rules and bounds. Output counterexamples or a scoped assessment in the existing owner: model/assumptions, examined reachable states, acceptance and invariants, methods/results, unresolved states and required corrections. Unknown guard semantics or external behaviour is an explicit limit that blocks affected approval, not an assumed transition.

## Method

1. Define a state as the control location plus decision-relevant data, active child/parallel work, recorded effects and remaining budgets. Separate terminal service outcome from stopped internal attempts. Preserve the existing completed/awaiting_steve and cancellation contract.
2. Identify invariants: required authority/preconditions before effects; counters never reset; completed child before a success return; no conflicting concurrent mutation; required evidence before completed; no outstanding required branch/effect at completion. Include actual mechanism-specific invariants and owners.
3. Check reachable configurations under feasible guards, not only graph edges. Detect an unavailable continuation/deadlock, an unreachable required activity, early completion with residual work, incompatible parallel joins, unsatisfiable resume condition and unsafe recovery re-entry. An impossible branch may indicate a modelling defect; it is not proof of tested execution.
4. Distinguish option-to-complete from guaranteed eventual termination. A possible route to completion from each reachable state does not prove every execution terminates. For loops/waits identify the decreasing budget, deadline or progress assumption, observable timeout route and evidence that the operator/runtime applies it. External fairness/availability assumptions MUST be named; do not promise a bounded external response without its contract.
5. Use a finite transition table and representative traces for a bounded model. Exhaustive enumeration MAY ONLY be called exhaustive when the full declared finite state/input domain was explored; record its bounds and assumptions. For larger/unbounded models use justified abstractions, targeted counterexamples and explicit unproved remainder. A model-checker PASS, if used, proves only the encoded properties/model.
6. Trace normal completion, each materially different branch/failure, partial and uncertain effects, child return, parallel cancellation, timeout, recovery exhaustion and terminal non-resumption as the actual mechanisms require. Derive expected transitions independently from component and governing contracts. Repair only the failed property and affected callers; then recheck the affected properties and mandatory gates.
7. Compare the canonical generated visual for structural parity and separately assess its meaning/readability. Record actual evidence class, revision, executor, findings and limits; return required changes to Head/Director. Independent acceptance remains with an actual non-author reviewer.

## Benchmark cases

- False reachability: the graph contains an edge to done but its guard is impossible for all admitted inputs -> report the unsatisfiable transition and incomplete service path.
- Parallel join: one branch may skip work but the join requires an unavailable completion signal -> identify the blocking trace and missing join policy.
- Residual work: done can be entered while a required child still runs -> fail proper completion, even when a graph walk reaches the terminal.
- Progress: a loop always has an exit option but may choose itself forever -> do not claim guaranteed termination without enforced finite bounds/progress conditions.
- Normal: a finite linear model completes only after all required evidence; failure enters bounded shared recovery and preserves effects/limits. Assessment is scoped to that model.

Written cases are not executed proof. Platform and enforcement claims require their own actual evidence.

## Anti-patterns

- Treating "has a path to done", Mermaid parity or a high score as semantic correctness.
- Assuming all possible graph paths are feasible, or hiding unknown guards behind otherwise.
- Claiming exactly-once effects from a sound control graph or durable replay.
- Equating synthetic state analysis with actual access, external success or business correctness.

## Stop

Return the assessed properties, counterexamples, exact model scope, actual results and remaining gaps. Withhold affected approval until required semantics and evidence are resolved; preserve source-only versus invocation authority.

## Sources and verification boundary

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.
