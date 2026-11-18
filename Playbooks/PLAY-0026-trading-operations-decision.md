---
id: PLAY-0026
type: playbook
title: Trading Operations Decision — Acute Departures From Normal
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0012, PLAY-0013, PLAY-0015, PLAY-0016, PLAY-0017, PLAY-0020, SKILL-0005, SKILL-0070, SKILL-0071, SKILL-0072, SKILL-0073, SKILL-0074]
tags: [playbook, trading-operations, sjf-alpha, drawdown, decision-point]
migrated_from: PLAY-0026-old-library
---
# Trading Operations Decision — Acute Departures From Normal

## Trigger

A trading operational incident requires a decision.

## Method

Identify infrastructure, drawdown or performance evidence. Stabilize only within authority; check running configuration and existing protections. Diagnose infrastructure directly, analyze performance through [[PLAY-0016]]/[[PLAY-0017]] as needed, then present the live-action decision.

## Stop

Verified restoration or explicit human decision/blocker. No autonomous trading, resizing, protection disablement or parameter changes.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

> ⚠ **FLAGGED — unresolved conflicts in the old Library, carried over as-is, not resolved by this migration.** Three items were open questions, not settled rules, at time of migration — they must not be filled from memory:
>
> - **Knowledge ↔ Playbook mapping unverified.** Some referenced Knowledge entries have filed playbook counterparts (Strategy Evaluation → PLAY-0013, Backtest Analysis → PLAY-0016, Performance Journal → PLAY-0017, Disciplined Coding → PLAY-0015); others have no verified counterpart. Do not assume a Knowledge entry was superseded by a Playbook without checking.
>
> See also the `[NEEDS the Library owner]` block at the foot: five numeric/policy questions. Current account/configuration evidence and incident-specific values are required runtime inputs. Unaccepted policy choices remain the Library owner-owned and are not defaults; D1 and D2 require his explicit pause/continue/resume decision on current evidence. This documentary workflow does not require us to invent permanent thresholds before review, and no missing value permits an autonomous live action.

## Trigger / entry condition

Run this playbook when live trading system hits any of:

- **Strategy underperformance** — results look worse than expected for the current regime (the Library owner flags it, or a review period closes as "Review required" / "investigate").
- **Infrastructure hiccup** — cBot, cTrader, cTrader Copy, broker connectivity, order routing, or market-data feed is degraded, stalled, duplicated, or unknown.
- **Drawdown beyond threshold** — peak-to-trough (or from all-time high) exceeds the operational gate. Numeric gate: `[NEEDS the Library owner]`.

Also run when the Library owner names this playbook, or says pause / halt / "something is wrong with the live system" / trading ops / incident.

Do not enter for: a new strategy, signal, or variation (Strategy Evaluation, PLAY-0013); architecture, feature design, or "how the bot works" (trading-system architecture knowledge); a scheduled weekly/monthly review with no incident (Performance Journal, PLAY-0017); lot-size / Kelly / scale-up with no incident (risk/sizing knowledge); backtest-only interpretation with no live incident (Backtest Analysis, PLAY-0016).

If the ask is vague ("how are we doing?"), frame first (Session Intake / Grill Me). Enter here only once an operational incident is the actual ask.

Per the operating-model decision governing this system: this playbook structures the decision and the evidence behind it — it does not autonomously choose or execute a production trading action. the Library owner makes the call; this playbook makes sure he has what he needs to make it well.

## Stages

### Stage 0 — Stabilize

**Goal:** Stop adding unexplained risk before classifying the incident.

**Action:** Record clock (UTC), account, whether the cBot is running, whether cTrader Copy is on, open sequence count, current balance vs peak, which protection features are live (Weekly Loss Halt, B-RSI Momentum Guard, Dynamic Balance Offset, 2-Consecutive-Losing-Weeks Halt).

Do not: disable protection features; increase lot size to recover; retune parameters; override during a high-impact event; treat TradingView as ground truth.

If platform state is unknown, or orders/data cannot be confirmed, preserve the current operating state and existing protections, gather the available evidence, notify the Library owner and wait for his instruction. Do not autonomously halt or resume new sequence openings, restart the bot, change parameters, alter sizing or disable protections.

If a protection feature has already halted the system, treat that as halt-already-in-force. This playbook then governs review-before-resume, not a second competing halt.

**Exit:** Incident log started; current operating state and protections recorded; the Library owner's instruction recorded when an operational change is required. Then Stage 1.

### Stage 1 — Classify

**Goal:** Name one primary track. Mixed incidents are allowed; precedence is fixed.

**Action:** Using only facts just recorded, classify:

| Primary track | Evidence |
|---|---|
| B — Infrastructure | Bot/Copy/broker/data/order state is wrong, stalled, duplicated, or unknown |
| C — Drawdown | Peak-to-trough (or vs all-time-high) has crossed, or is approaching, the operational gate |
| A — Underperformance | P&L / win-rate / behaviour is off versus same-regime expectation, and B/C are not the primary |

Precedence: B before C before A. Capital still being added by a malfunction outranks a P&L story.

**Exit:** Primary track named; secondary noted if present. Then the matching stage (2 / 3 / 4).

### Stage 2 — Track B: Infrastructure

**Goal:** Restore a known-safe platform state. Do not "fix" live-vs-TradingView divergence.

**Action:** Establish facts: is the cBot process running; is it attached to the live account; is Copy publishing; are orders filling; is price/data updating; are sequences firing on more pairs than expected (sequential pair processing is a known cAlgo quirk — not automatically a bug).

If any of running / filling / data is unknown → preserve the current state, surface the uncertainty to the Library owner and wait for instruction.

Restore in this order: connectivity → data → bot process → Copy. Do not restart the bot as a first reflex if open grid risk is already stacked; Only the Library owner may authorise restart.

After restore: confirm no duplicate instances, no orphan Copy subscribers receiving a dead/double signal, protection flags still ON.

If the hiccup looks like a code defect rather than platform/connectivity → hand off to trading-system architecture knowledge + Disciplined Coding Practice (PLAY-0015). Do not patch live parameters to paper over a bug.

**Exit:** Platform state is one of: Running-healthy / Halted-safe / Degraded-the Library owner-authorized. Then Gate D0. If P&L damage is the remaining question, continue to Stage 3 or 4.

### Stage 3 — Track C: Drawdown

**Goal:** Decide pause / partial pause / continue from severity + regime, not from the equity-curve high.

**Action:** Record the Performance Journal fact block for the incident window: period, open/close balance, net P&L, peak, max drawdown (£ and %), trades, win rate, active pairs, which protections triggered.

Classify regime via market-structure knowledge (Ideal / Challenging / Dangerous / Mixed). A loss in Challenging or Dangerous is not automatically a system failure.

Historical correlation illustration: 28 pairs were described as approximately 1.4 independent bets. Do not apply that number to the current portfolio without representative current evidence. Check actual exposure and clustering for the incident window; correlated losses must not be treated as independent merely because several pairs traded.

Apply SKILL-0005's evidence gate. Historical ladders, phase limits, margin percentages and portfolio statistics are not current policy and cannot be applied automatically. Verify the current account, broker constraints, cBot configuration, protection state and representative live evidence; then present the consequence and obtain the Library owner's explicit decision for any threshold or operational action. Margin stress is not sized here — hand off to risk/sizing margin management, do not invent a new free-margin %. If still adding grid levels into a one-way move: consider pausing new sequence opens (not a licence to disable the halts).

**Exit:** Severity decision recorded: Continue / Pause-new-opens / Full-pause. Then Stage 4 if cause is still unexplained, else Stage 5.

### Stage 4 — Track A: Underperformance (and unexplained P&L)

**Goal:** Separate expected-regime heat from edge decay, protection malfunction, or a bug. Do not retune on live pain.

**Action:** Complete the Performance Journal for this window (facts → regime → baselines → protection audit). That playbook interprets; this playbook decides.

Protection audit: did Weekly Loss Halt / B-RSI / Dynamic Balance Offset / 2-week halt trigger; was the trigger correct; what was the outcome. An "incorrect" trigger is a development candidate, not a reason to disable the feature.

Cause class — pick one: Expected-regime; Protection-as-designed; Suspected-edge-decay (hand off to Strategy Evaluation, PLAY-0013; do not start a new feature from this incident); Suspected-bug (hand off to trading-system architecture knowledge + Disciplined Coding Practice, PLAY-0015); Live-vs-backtest unexplained (hand off Backtest Analysis reconciliation, PLAY-0016 — never retune to force a match); Sizing/exposure (hand off risk/sizing knowledge — never increase size to "make it back"); Unknown (stay paused if Gate D1 requires it; do not fill the gap with a parameter change).

Underperformance magnitude/duration gate (when Track A is primary and C has not already paused): `[NEEDS the Library owner — do not invent]`.

**Exit:** Cause class named. Then Stage 5.

### Stage 5 — Decide and resume-or-hold

**Goal:** One operational state, with resume only through gates.

**Action:** Write the decision log (incident-scoped): incident window; primary/secondary track; regime; cause class; decision (no change / keep-halt / pause-new-opens / full-pause / infra-restore-only / hand-off); rationale; next review time.

Authority boundary (retained from the first filed version): material thresholds, timing, and escalation routes are requested from the Library owner when the case needs them — never invented as a global default. Log the outcome against the owning Project.

Forbidden decisions in this playbook: deploy a parameter change; disable a protection; scale lots up; add a new signal. Those are other playbooks, after this incident is stable.

**Exit:** System state is explicit: Normal / Paused-pending-review / Halted-protection-in-force / Handed-off. Then overall exit, or loop-back if a new signal appears.

## Decision gates / branches

**D0 — Still adding risk from a malfunction?** Yes (unknown platform, duplicate bot, orders not matching intent) → stay in Stage 2, preserve existing protections and obtain the Library owner's instruction before any halt, restart or resume action. No → proceed to C or A as classified.

**D1 — Pause vs continue.** This playbook does not apply a stored numeric ladder. Present verified current drawdown, account/configuration evidence, protection state, regime and stress consequences to the Library owner. Pause, continue or partially pause only on his explicit instruction; an existing protection halt remains in force unless separately authorised.

**D2 — Resume.** Resume new sequence openings only on the Library owner's explicit instruction after current platform state, protection state, drawdown evidence, cause class and any pending live change are presented. Never derive resume authority from an old threshold.

**D3 — Hand-off vs stay:**

| Cause class | Stay here? | Hand off |
|---|---|---|
| Expected-regime / Protection-as-designed | Yes — close incident | Performance Journal decision log only |
| Suspected-edge-decay | Close ops incident first | Strategy Evaluation (PLAY-0013); then Backtest Analysis (PLAY-0016) if a test is warranted |
| Live-vs-backtest unexplained | Keep halt if D1 | Backtest Analysis (PLAY-0016) → known-quirk knowledge |
| Suspected-bug | Preserve current state pending the Library owner's instruction | Trading-system architecture + Disciplined Coding Practice (PLAY-0015) |
| Sizing/exposure | Keep pause-new-opens until exposure is acceptable | Risk/sizing knowledge; regime check |
| Infrastructure code defect | After the state the Library owner authorises | Trading-system architecture + Disciplined Coding Practice (PLAY-0015) |

## Loop-back rules

| Signal | From → To |
|---|---|
| Platform symptoms appear during A or C | Stage 3/4 → Stage 2 (Track B takes precedence) |
| Drawdown crosses D1 during A or B | Current stage → Stage 3 |
| After infra restore, P&L still unexplained | Stage 2 → Stage 4 |
| A proposed change is rejected by strategy/backtest review | Hand-off → Stage 5 as no change |
| Test failure / bug confirmed | Stage 5 → Stage 2; preserve the current state and protections, obtain the Library owner's instruction before any halt/restart, and do not resume without D2 |
| New distinct incident while paused | Stage 0 (do not skip stabilize) |
| Regime reclassified | Stage 4 → Stage 1 |
| the Library owner proposes a parameter tweak to "fix" the incident | Block here → strategy/backtest review; loop back to Stage 5 with no-change until those pass |

Loop-backs reopen only the gap. Do not restart a full weekly review unless the incident window needs facts that were never recorded.

## Overall exit condition

This run is done when all of: primary track and cause class are named (Unknown remains explicitly blocked pending the Library owner's instruction, with any existing halt/pause and protections preserved); system state is explicit; decision log is written; any hand-off has a named target and a next action; resume, if claimed, passed D2; the outcome is logged against the owning Project.

Not done: "we'll watch it" with no state, no gate, and no next review time.

## Hand-offs

| Target | When | What crosses |
|---|---|---|
| Performance Journal (PLAY-0017) | Every incident | Incident window numbers + status |
| Market-structure knowledge | Regime, session, correlation, event-risk | Regime class; whether a session overlap or a named event is in play |
| Trading-system architecture knowledge | Bug, protection behaviour, Copy/cBot identity, known quirks | What the live system is supposed to do; feature-flag / kill-switch |
| Backtest Analysis (PLAY-0016) | Live vs backtest outside expected divergence; any proposed change | Hypothesis, sample, walk-forward — this playbook does not interpret the test |
| Strategy Evaluation (PLAY-0013) | Suspected edge decay; any new/varied signal proposed as the fix | Falsifiable hypothesis; this playbook must already be stable |
| Risk/sizing knowledge | Margin, stacked exposure, scale-up, "should we cut size" | Correlation, ratchet, phase; no live size-up to recover |
| Disciplined Coding Practice (PLAY-0015) | Code change after a confirmed bug | Implementation only, after architecture context |
| Mission Control | Every run | This playbook is an operational resident, not a skip around earlier gates |
| Chat Continuity | Incident spans sessions | State, gates waiting on the Library owner, open halt |
| Trading-system architecture / Disciplined Coding Practice (PLAY-0015) | Root cause turns out to be trading infrastructure | Diagnose the trading technical fix within PLAY-0026; the Library owner or an authorised operator performs the agreed operational action, with position-risk implications surfaced to the Library owner. Business-only PLAY-0020 is not this route |
| the Library owner | All numeric gates; bot restart; resume override; any protection disable | `[NEEDS the Library owner]` items below |

## Anti-patterns

| Anti-pattern | Instead |
|---|---|
| Disable a protection to recover P&L | Audit the trigger; keep it on |
| Increase lots to make back a hole | Consult risk/sizing knowledge; wait for the ratchet |
| Retune live after a bad window | Strategy Evaluation → Backtest Analysis; feature-flag OFF |
| Treat TradingView as ground truth | cAlgo live is the reference |
| Judge a loss without regime class | Classify regime first |
| Treat pair losses as independent bets | Verify current clustering/exposure; the historical ~1.4 figure is not a current portfolio fact |
| Manually override during a major news event | Trust Weekly Loss Halt |
| Restart the bot as the first move | Stage 0 facts; the Library owner authorizes restart |

## [NEEDS the Library owner] — numeric / policy gates

Do not fill these from memory or apply historical Library numbers. SKILL-0005 requires current account/configuration evidence and the Library owner's explicit policy decision.

- Drawdown pause gate: % from peak? from ATH? both?
- Drawdown resume gate (may be tighter than pause).
- Which document binds live ops: which ladder, which phase limits, a new ops-only number, or a combination?
- Underperformance gate when drawdown has not hit (1): magnitude, duration, win-rate floor, consecutive losing weeks (noting the 2-week halt already exists).
- Copy-specific halt: pause publisher only, or also instruct subscribers?

</details>
