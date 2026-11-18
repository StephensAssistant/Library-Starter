---
id: SKILL-0323
type: skill
title: Application Telemetry Instrumentation Design
status: current
created: 2026-11-01
updated: 2026-11-01
links: []
tags: [skill, software-methods, observability]
trigger_phrases: ["design application telemetry", "plan application logs metrics and traces", "design instrumentation for this feature"]
---

# Application Telemetry Instrumentation Design

Design a bounded application telemetry contract that makes named operational questions answerable without collecting unnecessary data. This Skill produces a design and verification specification; it does not install instrumentation or operate production.

## When to use

Use when an application feature, service, endpoint, queue or integration needs a new or revised logging, metrics, tracing or alerting design. Use the existing implementation owner for changes after the design is accepted under the current task authority.

## Intent routing contract

Own the translation of application behaviour and operational questions into signal definitions, propagation boundaries, privacy controls and falsifiable telemetry checks. Natural paraphrases include “what should we instrument?” and “how will we tell this feature is working?” Similar words alone do not activate the Skill.

Capturing evidence for an actual ADF run belongs to SKILL-0244, not this general design method. An active failure belongs to the applicable incident/debugging owner; an agent-harness-only request belongs to its harness owner. Mutation audit design, performance diagnosis and launch decisions remain with their existing owners. This is not a new cross-Playbook workflow.

## Input and outcome contract

Required inputs, supplied or discovered from authorized current evidence:

- Identified application/feature and revision/environment; the authoritative behaviour or acceptance contract, critical outcomes, error/empty/partial cases and accountable operational owner.
- Entry points, downstream services, asynchronous boundaries, trust boundaries and current telemetry facilities/configuration, each with source path or record and revision/date. Name unavailable access rather than assuming a platform exists.
- Operational questions and consumers of the answers, including the intended response to a degraded result; existing SLOs/alert policies and their authority, or an explicit statement that no numeric threshold has been agreed.
- Data classification, permitted telemetry fields and destinations, access/retention constraints and applicable cost/cardinality limits. Missing approval for a new destination is not implied by a source example.

Output: one telemetry design in the task's existing authorized artifact target, or in the response if no persistent target is designated. Include question-to-signal matrix, field/label/span contract, propagation map, privacy/cost controls, alert/runbook drafts where justified, and a check table with expected observations and evidence oracle. Each check records `designed`, `not run`, `observed pass`, `observed fail` or `blocked`; only actual retained observations support observed pass/fail; blocked identifies a required missing or contradictory input and needs no runtime execution.

Acceptance predicate: every in-scope operational question has a justified signal and falsifiable check; every material propagation boundary and data/cost risk has a control or explicit blocking gap; no readiness or runtime claim exceeds evidence. A proposal with unresolved material inputs is a blocked design with named decisions, not an accepted instrumentation contract. No default numeric threshold, sampling rate, retention duration or provider is supplied by this Skill.

## Method

1. **Bound the design.** The designer reads the feature contract and current configuration, names the questions and owners, and distinguishes “operation succeeded,” “valid empty result,” and “missing/partial evidence.” If missing expectations could change that distinction, record the missing source/owner and stop the affected question; continue independent questions only. If an incident is active, preserve the known evidence and hand it to the existing response owner rather than designing during response.
2. **Select signals by question.** For a specific event, propose a structured event with stable name and allowlisted fields; for aggregate frequency/failure/latency, propose bounded-series counters/histograms; for time or causality across boundaries, propose traces. Apply RED to relevant request/dependency paths and USE to relevant constrained resources only when they answer an identified question. Record why an unused signal is unnecessary; do not create all three mechanically. For every definition specify producer, unit, success/failure classification, aggregation and intended query.
3. **Make attribution explicit.** For each entry point and HTTP/queue/job boundary, specify where correlation and entry-point identity originate, how untrusted incoming values are validated, how metadata propagates and what happens when it is missing. Trace sampling must not be mistaken for complete event counts. If a boundary cannot carry identity, mark the affected end-to-end attribution claim blocked and propose a scoped alternative rather than claiming continuity. Existing compliant propagation is reused.
4. **Bound data and cost before implementation.** Classify each proposed field/span attribute/label, destination and access/retention requirement. Replace whole payloads, secrets and unnecessary personal identifiers with approved metadata. Labels must have evidenced finite domains; unbounded request/user IDs remain outside metric labels. If required diagnosis conflicts with privacy or series/cost limits, show the trade-off to the accountable owner and block that portion until resolved; do not silently weaken either control. Verify platform-specific SDK/configuration choices against the detected version's primary documentation before specifying executable details.
5. **Design actionable response.** If a signal has an agreed operational response and an evidenced threshold/duration policy, draft an alert with owner, condition, runbook first check and escalation route. If no policy exists, record the exact decision needed and propose how baseline evidence could inform it; do not invent a number or silently omit the gap. A dashboard-only signal needs no fabricated page. Runbook and notification destinations are drafts; this method grants no send or schedule authority.
6. **Specify independent falsification.** For each contract element identify an isolated authorized verification environment, stimulus/fixture, expected output, negative case and oracle (actual sink query, trace continuity, series output, redaction inspection or authorized delivery receipt). Include failure, retry and valid-empty cases where material; test attribution across each named asynchronous boundary. For a privacy check the oracle is actual sanitized output, not merely a config assertion. No safe access/stimulus means `not run` or `blocked`, never a claimed pass. Test alerts, lowered thresholds and induced failures require their own existing operational authority; do not execute them from design authority.
7. **Return the bounded design.** Cross-check question coverage, field classifications, label domains, propagation boundaries and check statuses against inputs. On contradiction, preserve both sources and return the affected decision to its owner. Design revision has no operational effect, so re-entry is limited to affected definitions/checks after new evidence; do not repeat unchanged review or retry an operational action. If later implementation evidence is supplied, distinguish known changes from unknown sink/delivery effects and let the implementation/response owner decide any retry. Stop when the design is reviewable and all gaps are visible.

## Benchmark cases

- **Normal — design benchmark, not an executed PASS:** A checkout retry feature has an authoritative success/retry/final-failure contract, identified API and worker entry points, an existing approved sink and agreed service alert policy. Expected design maps first-attempt versus eventual success to bounded outcome metrics, final failure to a sanitized structured event, and provider latency to a histogram/trace; propagates correlation and entry-point metadata through the queue. Checks require fixtures with independently specified outcomes and retained sink/trace observations. Unrun checks remain `not run`.
- **Failure/boundary — design benchmark:** A proposed metric labels every request ID and logs payment payloads; the privacy contract prohibits sensitive data and no series budget supports unbounded labels. Expected result rejects that shape, proposes bounded outcome/provider labels and approved sanitized diagnostic metadata, and blocks any unresolved data decision. It does not install a logger, send an alert or claim redaction passed.
- **Near-miss — design benchmark:** “The ADF run is green but produced zero rows; capture the run evidence.” Expected result routes to SKILL-0244 for correlated expected-versus-observed evidence, without expanding into an application telemetry redesign or assuming zero is legitimate/data loss.

## Sources and verification limits

Adapted from Addy Osmani [observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/observability-and-instrumentation/SKILL.md), pinned revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`; retained source and shared checklist: `Reference/addyosmani-agent-skills-8bfcc1f/skills/observability-and-instrumentation/SKILL.md` and `Reference/addyosmani-agent-skills-8bfcc1f/references/observability-checklist.md`. Retained licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`.

Static source review on 2026-11-01 covered question-driven signal selection, correlation/entry-point propagation, RED/USE, bounded cardinality, redaction, runbooks and telemetry self-verification. Persistent admission evidence: `Reference/addyosmani-agent-skills-20261101-review.md` (with retained individual source-review and coverage reports). Written benchmarks are design cases only. No SDK, sink, trace, dashboard, alert delivery, failure injection or application runtime was tested. No upstream executable, fixed threshold, mandatory provider, universal alert severity scheme or operational approval rule is imported.

## Contextual links

- `SKILL-0244` — `shared_method` — ADF-specific specialization for capturing correlated run receipts and missing expected-volume evidence; discovery pointer only, not a confirmed relationship. Reciprocal endpoint pointer is included in the source proposal.

- `SKILL-0113` — `shared_method` — Find the reviewed Addy Osmani collection and its qualified local-owner routing.

## Anti-patterns

- Logging everything, collecting whole payloads, or treating a request ID as a safe metric label.
- Inferring an entry point from circumstantial logs or claiming a sampled trace is a complete population.
- Copying upstream SDK snippets, destinations, numeric policies or alert tests into production without current platform evidence and task authority.
- Treating a designed check, tool success or missing telemetry as proof the feature is healthy.

## Stop

Stop with a reviewable telemetry contract and explicit evidence/gap table, or a blocked portion naming the exact missing source/decision and owner. Hand accepted design to the existing authorized implementation work record. No external sends, schedules, installation or deployment are authorized here.

## Link review — 1 November 2026

- Confirmed result: `no_supported_links`; no user statement or existing endpoint frontmatter establishes a confirmed relationship to this new ID. Frontmatter `links: []` remains accurate.
- Contextual result: `contextual_links_created`; the two advisory pointers above have reciprocal endpoint edits in this same proposal. They are retrieval aids, not authority or confirmed dependencies.
- Discovery: searched the complete current Skills and Playbooks filename catalogues, the Hat action roster and 41 relevant current owner contracts; compared all 25 upstream method contracts. The exact inspected paths, coverage distinctions and source revisions are retained in `Reference/addyosmani-agent-skills-20261101-review.md`.
- Rejected claims: generic method overlap does not confirm ownership, execution authority, a causal relationship or complete platform support. Existing narrower owners remain applicable in their domains.
