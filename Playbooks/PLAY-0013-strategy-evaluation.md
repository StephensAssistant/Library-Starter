---
id: PLAY-0013
type: playbook
title: Strategy Evaluation — Trading Edge Validation
status: current
created: 2026-08-17
updated: 2026-09-06
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0003, PLAY-0006, PLAY-0016, PLAY-0017, PLAY-0026, SKILL-0001, SKILL-0059, SKILL-0060, SKILL-0061, SKILL-0062, SKILL-0063, SKILL-0064, SKILL-0272, SKILL-0273, SKILL-0274]
tags: [playbook, strategy-evaluation, sjf-alpha, trading, design, mission-control]
migrated_from: PLAY-0013-old-library
---
# Strategy Evaluation — Trading Edge Validation

## Trigger

A trading strategy hypothesis needs evaluation.

## Method

State a falsifiable mechanism and decision criteria before results. Reuse one evidence set with [[PLAY-0016]]: baseline, costs, untouched evaluation, regimes and robustness. Present reject, extend evidence or controlled build options.

## Stop

Evidence-backed decision point. Never tune until a pass, infer a universal sample threshold or enable a strategy without authority.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

Evaluate whether a proposed trading idea or signal has defensible edge rather than an attractive historical artefact. the Library owner makes every material trading and production decision in the live conversation; this playbook structures evidence and never deploys or enables a strategy.

## Trigger / entry condition

Mission Control routes a new strategy idea, signal, trading system variation, claimed edge, or suspected edge decay here for evaluation.

## Stages

### Stage 1 — Triage the idea

**Goal:** Determine whether the idea is specific, falsifiable, non-duplicative, and compatible enough to test.

**Action:** Record the proposed mechanism, why it could persist in a competitive market, expected regime dependence, architecture fit, data availability, implementation feasibility, complexity added, and whether this is disguised parameter tuning. Consult retained architecture, FX-market, and risk Knowledge.

**Exit:** A testable idea proceeds, or a rejection/reframing decision and reason are recorded.

### Stage 2 — Precommit the edge hypothesis

**Goal:** Define success and failure before examining favourable results.

**Action:** Write the mechanism, why counterparties may be wrong, expected operating and failure regimes, falsification criteria, comparison baseline, required evidence sufficiency, and minimum worthwhile effect. Any material numeric gate not already governed is asked of the Library owner and recorded.

**Exit:** The hypothesis and decision rules are confirmed before testing.

### Stage 3 — Run the minimum viable test

**Goal:** Produce reproducible evidence that can distinguish signal from noise.

**Action:** Select data periods, regimes, sample/trade coverage, untouched out-of-sample evidence, costs and constraints appropriate to the hypothesis. Compare with the current system and a naive baseline. Execute and document analysis through the Backtest Analysis playbook.

**Exit:** A reproducible results package exists, or insufficient evidence and its next collection action are recorded.

### Stage 4 — Red-team the result

**Goal:** Actively test whether the apparent edge is fragile, biased, or accidental.

**Action:** Check parameter tuning, sub-period dependence, sensitivity, uncertainty, multiple testing, market/regime persistence, operational costs, architecture fit, and failure modes. Separate observed evidence from interpretation.

**Exit:** The result has an evidence-backed finding, caveats, and known invalidation conditions.

### Stage 5 — Record the decision

**Goal:** Convert the evidence into an explicit human decision and controlled next action.

**Action:** the Library owner and the AI choose reject, gather more evidence, run a bounded experiment, or propose build work. Create/update the relevant Ticket or Project; define monitoring and a disable/rollback path before any proposal to enable. Update the strategy-idea log.

**Exit:** The decision, rationale, evidence, owner, and next action are recorded. No production action is implied.

## Decision gates / branches

- Weak or unfalsifiable mechanism: return to Stage 1 or reject.
- Insufficient evidence: collect data and repeat Stage 3.
- Fragile result: revise the precommit/test or reject; do not tune until success.
- Architecture conflict: consult the approved strategy architecture and return to Stage 1.
- Live performance decay: receive evidence from Performance Journal, then return to Stage 2 or 3.
- Missing risk, evidence, approval, or deployment threshold: ask the Library owner and pause the affected branch.

## Loop-back rules

- New regime information returns to Stage 1 or 2.
- Red-team failure returns to Stage 2 or 3.
- Implementation evidence that challenges the mechanism returns to Stage 1.
- Repeated testing preserves every prior hypothesis and result in the idea log.

## Overall exit condition

The strategy idea has a documented evidence-based decision and controlled next Ticket/Project action, or a documented rejection. Nothing is autonomously deployed or enabled.

## Hand-offs

- **From Session Intake:** receive the framed trading question, constraints, and resolved decisions.
- **To Backtest Analysis:** send the precommitted hypothesis, data definition, baselines, evidence gates, and falsification rules.
- **From Performance Journal:** receive live results, regime context, suspected decay, and operational changes.
- **To approved architecture, market-structure and risk references:** consult retained architecture, market-structure, and risk references; these remain Knowledge.
- **To Ticket/Project work:** send the decision, evidence, caveats, monitoring needs, rollback/disable requirement, and next chosen action.

## Nonbinding historical heuristics

Examples of unverified historical heuristics include twelve months or three years of history, 100/300-trade bands, a 30% out-of-sample split, p < 0.05, and a two-standard-error comparison. These are unverified historical heuristics, not canonical gates. Use only when the Library owner confirms them for the live case or a governed current source establishes them. Select evidence sufficiency and statistical methods appropriate to the hypothesis, dependence structure, costs, regimes, and multiplicity.

## Anti-Patterns

- Treating a chart story as a mechanism.
- Testing repeatedly until something works.
- Evaluating only in sample.
- Adding complexity because it "cannot hurt."
- Declaring success before red-team review.
- Ignoring regime dependence, costs, or operational constraints.

</details>
