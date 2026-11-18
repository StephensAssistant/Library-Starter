---
id: SKILL-0324
type: skill
title: Application Rollout Readiness Assessment
status: current
created: 2026-11-01
updated: 2026-11-01
links: []
tags: [skill, software-methods, release-readiness]
trigger_phrases: ["assess application rollout readiness", "is this new application ready to launch", "review net-new app release readiness"]
---

# Application Rollout Readiness Assessment

Assess evidence for a proposed net-new application rollout and return a bounded advance, hold or stop recommendation to the existing decision owner. This Skill owns one readiness assessment; it neither deploys nor creates a new multi-Playbook release workflow.

## When to use

Use when a new application or independently released feature has an identified candidate and proposed audience/exposure stage, and the user needs a defensible readiness decision. Reassess after material candidate, audience, policy or outcome evidence changes.

## Intent routing contract

Own the mapping from the exact candidate and proposed exposure to acceptance, observability, recovery and operational evidence, resulting in a recommendation with limitations. Natural paraphrases include “can we advance this app to the next cohort?” and “what blocks this launch?” Similar launch terminology alone does not grant deployment authority.

If an old live system of record must be replaced or consumers re-pointed, use PLAY-0022 and its applicable route-specific controls; this general assessment cannot replace parity, sign-off, source-only fix-forward rules or seven-calendar-day hypercare. Active production harm belongs to the current incident/recovery owner. Building the application, designing tests or instrumentation, running infrastructure changes and granting release approval remain with their existing owners. A readiness recommendation is not that approval.

## Input and outcome contract

Required evidence, supplied or discovered from authorized current sources:

- Exact application/candidate revision or immutable build identity, target environment, intended users/critical journeys, proposed exposure/cohort and stage, requested decision and accountable release/operational owner.
- Authoritative acceptance criteria and applicable security/privacy/accessibility/performance obligations; exact evidence receipts identifying candidate, environment, observation time, expected result and observed result, including unresolved defects and exceptions.
- Current production baseline where one exists; applicable SLO/error-budget policy and freshness/observation-window requirements; proposed advance/hold/stop criteria and their approving authority. For a first launch without baseline, explicit first-launch acceptance limits or owner-approved observation criteria are required instead of a fabricated relative comparison.
- Monitoring/telemetry coverage and evidence of signal operation; an applicable recovery or fix-forward plan with authority, trigger, owner, known data effects and verified prerequisites; support capacity, the governing seven-calendar-day hypercare requirement for every production release, and applicable cleanup policy.

Output: one candidate-specific readiness assessment in the existing authorized work record/artifact target, or the response if no target is designated. State candidate, proposed exposure, applicable criteria, evidence per criterion (`observed pass`, `observed fail`, `blocked`, `not applicable` with reason), recommendation, material limitations, owner and exact re-entry conditions. A design document or planned test is not an observed pass. Record exception scope and authorizer; do not enlarge it.

Acceptance predicate: every applicable criterion has a current matching evidence receipt, an authorized exception or an explicit gap; the recommendation follows the branch rules below and preserves current release authority. Missing or contradictory material evidence yields hold, not implicit acceptance. No universal numerical threshold, cohort percentage, monitoring duration, flag expiry or error-budget policy is supplied by this Skill.

## Method

1. **Classify the decision.** The assessor binds the exact candidate, environment, audience/exposure and decision owner. If a live predecessor/consumer cutover is involved, hand off the migration decision to PLAY-0022; do not use a net-new label to bypass its controls. If observed harm requires immediate response, preserve known evidence and refer to the existing response owner, without attempting recovery. If candidate identity or authority is unknown, return hold with that input gap.
2. **Build the applicable criteria table.** Read the accepted specification and governing release/operational policies. Map each critical journey and material risk to its actual criterion, tolerance, receipt/oracle and required evidence freshness/window. Include correctness/compatibility, security/privacy/access, accessibility/performance where applicable, deployment/configuration prerequisites, telemetry, recovery and support. Mark a category not applicable only with its concrete scope reason. Do not require every possible checklist item or invent a missing target. If policy sources conflict, hold the affected decision pending the named policy owner's resolution.
3. **Check evidence identity and sufficiency.** For each receipt compare candidate/build, configuration, environment, population, observation window and expected versus observed result against the criterion. An old build's green suite, a screenshot without its state, a planned rollback exercise or an empty error dashboard with no evidence traffic/signal operation cannot pass the related criterion. If material receipts mismatch, are stale under the applicable policy, contradict each other or lack an oracle, mark blocked and specify exactly what must be re-observed. Reuse valid unchanged evidence; do not rerun checks for reassurance. Test execution, provider access and production probes remain separate authorized work.
4. **Assess exposure control and recovery.** Where an approved flag/cohort mechanism exists, verify evidence for both relevant states, cohort definition, access, operator, stop mechanism and cleanup owner under the project's policy. If absent, do not demand or install a flag automatically: determine whether the approved exposure/recovery approach satisfies the actual risk controls; unresolved capability is a gap. Review the recovery plan's exact target, prerequisites, authority and data consequences, distinguishing reversible exposure from irreversible writes. A previous-version deploy is not a complete database recovery plan. Preserve fix-forward restrictions and required retention; do not recommend a prohibited reversal.
5. **Apply operating-window constraints.** Compare telemetry and support evidence with the agreed observation/window criteria; absence of adequate traffic cannot prove a low error rate. Apply an existing error-budget restriction only if the authoritative policy and current budget evidence exist; otherwise do not invent a freeze threshold. Every production release enters seven calendar days of hypercare under the governing production baseline, including a net-new application release. For a migration route, retain its seven-calendar-day window from cutover with material defects resolved and retested, together with its route-specific controls. Exposure-stage observation criteria may require a different evidenced window, but cannot replace or shorten production hypercare; do not copy upstream 24/48-hour or one-week examples as alternative policy.
6. **Return the deterministic recommendation.** `Advance recommended` only if every applicable criterion passes for this exact exposure and candidate or has a valid authorized exception, and no applicable stop restriction is active. `Hold` if any required evidence, threshold, owner, observation window or prerequisite is unresolved, mismatched or incomplete; identify each blocker and its re-entry evidence. `Stop/do not advance` if matched evidence falsifies a mandatory acceptance criterion or a governing policy prohibits this exposure; cite the observed failure/policy and the existing remediation/response owner. Do not issue a rollback command or send notifications. If an exception conflicts with a non-overridable governing rule, it cannot convert stop to advance.
7. **Bound re-entry and effects.** Record that assessment itself changed no live state; separate reported known deployed/exposure/data effects from unknowns. Changed candidate/configuration invalidates evidence for affected criteria; changed cohort or window invalidates the corresponding exposure evidence. Re-enter only those rows and their dependencies once replacement evidence or a resolved decision exists. There is no autonomous poll/retry loop, scheduled monitoring or repeated unchanged review. If operational action had an uncertain outcome, refer to its existing owner to reconcile actual state before any retry.

## Benchmark cases

- **Normal — design benchmark, not an executed PASS:** A net-new app has a pinned build, identified internal cohort, agreed critical-journey criteria, current matching acceptance receipts, sanitized telemetry-operation receipts, an approved recovery plan and an owner-agreed exposure observation window satisfied by representative evidence, and an assigned plan for the mandatory seven-calendar-day production hypercare. No mandatory criterion or policy restriction fails. Independently expected result: advance recommendation for that candidate and cohort only, with evidence table and existing decision owner; no deployment or announcement.
- **Failure/boundary — design benchmark:** Build B is proposed but the green test receipts are for Build A; no first-launch baseline exists and the draft says “advance below twice baseline error rate.” Independently expected result: hold for candidate-matched evidence and owner-agreed first-launch criteria; do not invent a baseline, copy upstream percentages, declare tests failed, run production tests or claim readiness.
- **Failure — design benchmark:** Candidate-matched evidence exceeds a mandatory accepted latency limit, or current authoritative budget policy prohibits this exposure. Independently expected result: stop/do not advance with exact criterion/receipt and remediation owner, even if unrelated checks pass. No automatic rollback or code change.
- **Near-miss — design benchmark:** “Re-point this Sigma app from the old reporting system and close hypercare after two days.” Independently expected result: migration decision routes to PLAY-0022; preserve the applicable seven-calendar-day hypercare, parity/sign-off and route-specific recovery restrictions. This Skill does not create a competing rollout path.

## Sources and verification limits

Adapted from Addy Osmani [shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/shipping-and-launch/SKILL.md), pinned revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`; retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/shipping-and-launch/SKILL.md`, with referenced shared definition-of-done/security/performance/accessibility checklists under that snapshot's `references/`. Retained licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`.

Static source review on 2026-11-01 covered readiness dimensions, cohort/flag lifecycle, observable advance/hold/stop decisions, recovery preparation and error-budget considerations. The governing AGENTS production baseline requires seven calendar days of hypercare for every production release. The retrieved PLAY-0022 contract additionally preserves migration-specific cutover timing, material-defect exit checks and route-specific fix-forward restrictions. Persistent admission evidence: `Reference/addyosmani-agent-skills-20261101-review.md` (with retained individual source-review and coverage reports). These benchmarks are written design cases, not runtime tests or independently executed acceptance. No application, deployment, rollback, canary, monitoring window or alert was exercised. Source example thresholds, timings, automatic git operations and universal release gates are not imported.

## Contextual links

- `PLAY-0022` — `shared_method` — Migration-specific specialization for live predecessor replacement, parity, consumer cutover, recovery, seven-calendar-day hypercare and decommission; discovery pointer only, not a confirmed relationship. Reciprocal endpoint pointer is included in the source proposal.

- `SKILL-0113` — `shared_method` — Find the reviewed Addy Osmani collection and its qualified local-owner routing.

## Anti-patterns

- Equating green tests, a successful deploy tool or a quiet dashboard with rollout readiness.
- Using relative error thresholds without a valid baseline or copying upstream numerical defaults.
- Treating advance recommendation as approval, deployment, notification, rollback or monitoring-schedule authority.
- Omitting the seven-calendar-day hypercare required for every production release, closing it early, ignoring irreversible data effects, weakening acceptance to manufacture a pass, or routing migration through a generic net-new assessment.

## Stop

Stop with the bounded advance/hold/stop recommendation, candidate-specific evidence table, unresolved gaps and re-entry conditions. Deliver to the existing authorized decision/work record. Do not send externally, deploy, change exposure, run recovery or launch another Playbook automatically.

## Link review — 1 November 2026

- Confirmed result: `no_supported_links`; no user statement or existing endpoint frontmatter establishes a confirmed relationship to this new ID. Frontmatter `links: []` remains accurate.
- Contextual result: `contextual_links_created`; the two advisory pointers above have reciprocal endpoint edits in this same proposal. They are retrieval aids, not authority or confirmed dependencies.
- Discovery: searched the complete current Skills and Playbooks filename catalogues, the Hat action roster and 41 relevant current owner contracts; compared all 25 upstream method contracts. The exact inspected paths, coverage distinctions and source revisions are retained in `Reference/addyosmani-agent-skills-20261101-review.md`.
- Rejected claims: generic method overlap does not confirm ownership, execution authority, a causal relationship or complete platform support. Existing narrower owners remain applicable in their domains.
