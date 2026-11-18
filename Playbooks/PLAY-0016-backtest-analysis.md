---
id: PLAY-0016
type: playbook
title: Backtest Analysis
status: current
created: 2026-08-14
updated: 2026-09-06
owner: the Library owner
links: [HAT-0012, PLAY-0006, PLAY-0013, PLAY-0017, PLAY-0019, PLAY-0026, PLAY-0039, SKILL-0001, SKILL-0004, SKILL-0059, SKILL-0060, SKILL-0061, SKILL-0062, SKILL-0063, SKILL-0064, SKILL-0065, SKILL-0066, SKILL-0067, SKILL-0068, SKILL-0069, SKILL-0272, SKILL-0273, SKILL-0274, SKILL-0275, SKILL-0276, SKILL-0286]
tags: [playbook, backtest-analysis, trading, verification, sjf-alpha]
migrated_from: PLAY-0016-old-library
---
# Backtest Analysis

## Trigger

Trading backtest evidence needs interpretation.

## Method

Record hypothesis, code/config version, source, period, instruments, sample, costs and parameter history. Check leakage, holdout/walk-forward validity, uncertainty, regime coverage and sensitivity. Reconcile platform differences when material; never tune solely to force agreement.

## Stop

Reproducible conclusion and limitations. Live changes remain a separate authorized decision; reuse this evidence in [[PLAY-0013]].

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

## Trigger / entry condition

Use when personal trading backtest results need interpretation, when a strategy hypothesis is being evaluated, or before the Library owner considers a parameter or feature change for live use. Backtests are evidence about a hypothesis, not authority to deploy.

## Stages

### Stage 1 — Pre-register the hypothesis

- **Goal:** Prevent results from defining their own success criteria.
- **Action:** State the proposed edge, what would falsify it, the decision the test may inform, and the case-specific effect required to matter. the Library owner resolves any material threshold or deployment intent in conversation.
- **Exit:** Hypothesis, falsifier, and decision criteria are recorded before interpreting results.

### Stage 2 — Establish the evidence set

- **Goal:** Make the result reproducible and correctly scoped.
- **Action:** Record platform, code/config version, instruments, date window, trade/event count, costs, data source, parameter history, and protection features. Distinguish TradingView exploration, cAlgo backtest signal-logic evidence, and cAlgo live execution evidence.
- **Exit:** Evidence provenance is complete or missing inputs are explicitly named.

### Stage 3 — Test robustness

- **Goal:** Detect leakage, overfitting, sample weakness, and regime dependence.
- **Action:** Check whether tuning and evaluation data overlap; examine held-out or walk-forward evidence; inspect parameter sensitivity; test multiple regimes; and use protection-event counts when evaluating protection features.
- **Exit:** Robustness strengths, limitations, and incomplete tests are recorded.

### Stage 4 — Reconcile platforms

- **Goal:** Explain differences before changing the system.
- **Action:** Account for documented sequential-pair processing, VWAP/bar-timing, and signal-count differences. Treat perfect agreement as something to investigate, not automatic proof. Never tune merely to force platform agreement.
- **Exit:** Divergence is explained within evidence, or an investigation gap is opened.

### Stage 5 — Prepare the decision brief

- **Goal:** Give the Library owner an evidence-backed choice without making it for him.
- **Action:** Summarise current position, uncertainty, options, risk, proposed monitoring, rollback questions, and required follow-up. Link the relevant Ticket or Project. the Library owner chooses whether to reject, extend testing, investigate, or consider a controlled live change.
- **Exit:** the Library owner's decision and next action are recorded, or the analysis is explicitly incomplete.

## Decision gates / branches

- No pre-registered hypothesis → return to Stage 1.
- Inadequate evidence, no held-out test, or missing adverse regime → extend the test; do not claim readiness.
- Unexplained live/backtest divergence → investigate before parameter changes.
- Proposed live change → consult the approved system architecture and the approved risk and sizing reference, then obtain the Library owner's live decision.
- New evidence changes the hypothesis → start a new analysis rather than rewriting the original criterion.

## Loop-back rules

New provenance or regime evidence returns to Stage 2 or 3. A failed robustness check may prompt a revised hypothesis, but the original result remains recorded as failed/incomplete.

## Overall exit condition

An evidence-backed decision is recorded by the Library owner, or the exact evidence required to continue is documented. The playbook never deploys, pauses, resizes, or changes parameters autonomously.

## Hand-offs

- PLAY-0006 — routing and authority.
- Strategy Evaluation playbook — whether an idea merits testing.
- the approved system architecture — trading-system architecture.
- Performance Journal playbook — comparison with live behaviour.
- the approved market-regime reference / the approved risk and sizing reference — market-structure and risk/sizing reference.

## Nonbinding legacy heuristics

The source recorded sample bands of under 30, 30–100, 100–300, and 300+ trades; a 70/30 split; a 60% out-of-sample comparison; six-month/two-month windows; and a 75% win-rate warning. These are unverified legacy heuristics, not automatic gates. Use them only as questions or comparison points unless the Library owner confirms the applicable criterion for the current decision.

## Anti-Patterns

- Calling a result strong without sample, period, costs, and provenance.
- Optimising and evaluating on the same evidence.
- Ignoring held-out data or adverse regimes.
- Tuning cAlgo to imitate TradingView.
- Converting an exploratory result directly into a production action.

</details>
