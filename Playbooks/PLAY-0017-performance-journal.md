---
id: PLAY-0017
type: playbook
title: Performance Journal
status: current
created: 2026-08-17
updated: 2026-09-06
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0012, PLAY-0006, PLAY-0013, PLAY-0016, PLAY-0019, PLAY-0026, SKILL-0001, SKILL-0059, SKILL-0060, SKILL-0061, SKILL-0062, SKILL-0063, SKILL-0064, SKILL-0272, SKILL-0273, SKILL-0274]
tags: [playbook, performance-journal, trading, live-review, sjf-alpha]
migrated_from: PLAY-0017-old-library
---
# Performance Journal

## Trigger

A trading performance review is requested or explicitly scheduled.

## Method

Read the named period/account/configuration and verified results. Compare appropriate baselines, regime evidence and applicable protection behavior. Separate facts from hypotheses; recommend one next action.

## Stop

Requested review delivered. No automatic parameter changes, new records or review schedule.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

## Trigger / entry condition

Use for a scheduled or ad-hoc review of personal trading live performance, or when current results need a regime-aware position before the Library owner chooses an action.

## Stages

### Stage 1 — Define period and scope

**Goal:** Ensure the review covers one identifiable operating state.

**Action:** Record dates, account/system version, active instruments, enabled protections, review purpose, and relevant Ticket or Project.

**Exit:** Scope and evidence sources are agreed.

### Stage 2 — Record facts before interpretation

**Goal:** Establish an auditable performance record.

**Action:** Capture opening, closing, and peak balance; P&L; drawdown; trade count; win rate; active pairs; and protection events. Cite sources and mark unavailable facts rather than estimating them.

**Exit:** The factual record is complete or every gap is explicit.

### Stage 3 — Apply regime context

**Goal:** Interpret results in the conditions that produced them.

**Action:** Using the approved market-regime reference, evidence whether conditions were ranging/low-volatility, directional, high-volatility/news-driven, risk-off/JPY-sensitive, or major-event affected. Record mixed or uncertain classifications honestly.

**Exit:** Regime classification and supporting evidence are recorded.

### Stage 4 — Compare calibrated baselines

**Goal:** Avoid emotional or cherry-picked comparison.

**Action:** Compare with prior periods and similar regimes where data exists. Treat the manual-trading baseline and recent high-water marks as context, not guaranteed targets.

**Exit:** Comparable evidence and its limitations are clear.

### Stage 5 — Audit protection behaviour

**Goal:** Determine whether protections behaved as configured.

**Action:** Inspect Weekly Loss Halt, B-RSI Momentum Guard, Dynamic Balance Offset, and 2-Week Loss Halt triggers and outcomes where present. Record a suspected incorrect trigger as an investigation candidate; do not disable it automatically.

**Exit:** Each applicable protection has an evidenced finding.

### Stage 6 — Decide and record next action

**Goal:** Turn the review into a truthful current position.

**Action:** Present result, regime, uncertainty, options, risks, and next-review choices. the Library owner chooses no change, investigate, backtest a proposal, pause, or another action. Record the decision in the relevant Ticket or Project.

**Exit:** the Library owner's decision and next review/action are recorded.

## Decision gates / branches

- Missing or inconsistent facts → return to Stage 2.
- Uncertain regime → gather evidence or record uncertainty; do not force a label.
- Suspected implementation defect → open/route an investigation.
- Proposed parameter or feature change → Backtest Analysis playbook before live consideration.
- Suspected sizing issue → consult the approved risk and sizing reference and ask the Library owner.
- Live operational incident → use the governed trading-operations playbook if admitted; otherwise stop with the Library owner.

## Loop-back rules

Corrections to facts return to Stage 2 and invalidate downstream interpretations. New regime evidence returns to Stage 3. A later review is a new journal period, not an overwrite of the prior record.

## Overall exit condition

A factual, regime-aware review and the Library owner-approved next action are recorded, or the review states exactly why it cannot yet conclude. No production action is autonomous.

## Hand-offs

- PLAY-0006 — routing and authority.
- Backtest Analysis playbook — evaluate any proposed system change.
- the approved system architecture — system and protection architecture.
- the approved market-regime reference / the approved risk and sizing reference — regime and risk/sizing reference.

## Nonbinding legacy heuristics

The source recorded drawdown bands of 0–5%, 5–10%, 10–15%, 15–20%, and above 20%, plus win-rate bands around 50%, 60%, and 75%. They are unverified calibration prompts, not standing authority to pause, resume, resize, disable protections, or change parameters. Present the observed value and context to the Library owner; he decides the applicable action.

## Anti-Patterns

- Judging performance before classifying regime.
- Treating one period as proof of edge or failure.
- Disabling a protection after one adverse result.
- Optimizing against recent live losses.
- Ignoring trigger logs or missing source evidence.
- Treating a legacy heuristic as an automatic production gate.

</details>
