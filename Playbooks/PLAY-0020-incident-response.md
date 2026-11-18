---
id: PLAY-0020
type: playbook
title: Incident Response — Customer Ticket and Project Failures
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0004, PLAY-0019, PLAY-0025, PLAY-0026, PLAY-0029, PLAY-0031, PLAY-0032]
tags: [playbook, incident-response, pipeline-observability, triage, root-cause]
migrated_from: PLAY-0020-old-library
---
# Incident Response — Customer Ticket and Project Failures

## Trigger

An existing customer Ticket or Project reports a business operational failure that needs response. Alerts and monitoring events do not activate this playbook until they have that work context.

## Method

Confirm actual impact and affected consumers; label REAL/FALSE/INCONCLUSIVE from evidence. Search relevant Library evidence, rank up to three possible causes by confidence, and propose the quickest discriminating checks. Recommend containment and the smallest precise fix for the Library owner or an authorised operator to execute; record execution only after confirmation. Verify consumers end-to-end. Use [[PLAY-0029]] for rollback and [[PLAY-0031]] for access.

## Stop

Affected service/consumers verified or named waiting/blocker state. Do not assume unbuilt monitoring exists or open unrelated platform work.

AGENTS.md owns shared authority, evidence reuse and task boundaries. The AI has no implied operational access to Snowflake, ADF, OpenFlow, Qlik, Sigma, SQL Server, Streamlit or Freshservice; system actions remain recommendations until the Library owner or an authorised operator confirms execution.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>


## Scope and domain

owner-managed BI only (Snowflake, ADF, OpenFlow, Qlik, SQL Server, Streamlit). Treat the context as business unless the Library owner explicitly states that it is personal. Trading / personal trading is out of scope.

## Position under Mission Control

Layer, not a new front door. Mission Control still classifies and routes every message. This playbook never self-triggers around it.

- Hard pipeline failure with an error/failed run → this playbook.
- Silent wrong/stale data with no thrown error → the pipeline observability response playbook.
- Bad production change already applied (need freeze/rollback) → the disaster recovery/rollback playbook.
- Trading/cBot/cTrader/personal trading → route to [[PLAY-0026]]; do not use this playbook.

**Precedence (fixed order):** the approved reproduce/bisect/fix procedure wins on reproduce/bisect/idempotent-fix. the approved feed-recovery invariants wins on D365 trickle-feed recovery invariants. the verified customer-ticket ownership rules wins on customer-ticket ownership/escalation where its system facts are verified. the current ticket-writing policy wins on Library ticket field updates and customer phrasing. This playbook wins only on the owner-managed incident state-machine: triage → contain → RCA → fix → verify → document.

## Trigger / entry condition

A customer reports a pipeline, job or dashboard failure through an existing Ticket or Project. An Azure/DataOps alert or observability finding must first be represented in that customer work context; never assume monitoring coverage exists or let an alert self-trigger this playbook.

Enter when all of these are true:

- Mission Control has already run (trail present). If missing, return to Mission Control.
- The live ask is a owner-managed pipeline/runtime failure, not a design/build request.
- An existing customer Ticket or Project is the work context.
- The Freshservice request has been routed through Service Desk into the BI resolver chain.
- At least one of: ADF pipeline/activity failed; OpenFlow processor/flow-file error; Snowflake task/proc/COPY/MERGE failed or stuck IN_PROGRESS; D365 entity ERROR; Streamlit app failing on warehouse/query; SQL Server source/CDC feed to ADF failed; Freshservice ticket assigned as a pipeline outage.

**Wrong door — do not enter when:**

- A request for a new feature or enhancement, not a failure — belongs in Project Intake & Scoping, not here.
- No error, but numbers look wrong / dashboard gap / volume collapse / suspended dynamic table with no failure event → observability playbook.
- A change just went live and the system is in an unsafe state (need freeze first) → disaster-recovery playbook, then return here only for remaining RCA/document.
- The work is to architect or rebuild a pipeline → Pipeline Architect / Snowflake ingestion knowledge.
- Ticket is a request/enhancement, not an incident → customer-ticket and ticket-field knowledge.

## Stages

### Stage 0 — Domain and machine gate

**Goal:** Prevent trading mix-in and prevent using the wrong playbook.

**Action:** Name the domain (owner-managed BI vs Library vs trading). If trading, stop. If silent-data, exit to observability. If freeze/rollback is the first need, exit to DR. Else continue.

**Exit:** owner-managed hard-failure confirmed, or routed away. No diagnosis before this exit.

### Stage 1 — Capture evidence

**Goal:** Freeze the facts before anyone re-runs anything.


**Exit:** Evidence pack exists. Pipeline state unchanged.

### Stage 2 — Severity and ownership

**Goal:** Decide who owns it and whether business notification is due now.

**Action:** Follow the confirmed resolver chain: Service Desk routes the request; the BI Analyst performs initial investigation; unresolved work escalates to a BI Developer; unresolved developer work escalates to a Senior BI Developer such as the Library owner. When the Library owner is working the Library mirror, treat him as the current owner unless he explicitly says he is supporting a colleague. Treat availability as current context; do not encode fixed working hours or after-hours assumptions.

Freshservice is the working intake, assignment, status, priority and requester-agent communication record. It does not diagnose or repair the BI system; this playbook governs that technical response.

Governing severity rule (ratified): when urgency is genuinely unclear, ask the Library owner rather than assuming — do not invent a severity level. Never default to "patch now" or "schedule" without a stated reason.

Priority is mandatory context. Retain the Freshservice priority, P1/P2/P3 or another label only when the current Ticket, Project or conversation supplies it. If priority is absent, ask the Library owner one targeted question before prioritising; never infer fixed thresholds, response clocks, working hours or due commitments. Reconfirm when the conversation indicates priorities have moved.

Recommend patch-now vs planned work from verified impact and the recorded priority; the Library owner decides any unresolved urgency/timing. A customer-facing symptom alone supplies no production authority or response clock. Record planned work in the existing Ticket; scheduling requires separate authority. File or reopen the Library TICK by Freshservice reference (one external reference = one Library TICK; reopen, never duplicate).

**Exit:** Owner named, severity named (or explicitly provisional and waiting on the Library owner), Library TICK exists or is the reopened canonical INC record.

### Stage 3 — Contain

**Goal:** Stop spreading bad data. Do not "fix" yet.

**Action:** Recommend the smallest containment matching the layer. Never claim it occurred until the Library owner or an authorised operator confirms it:

- ADF: do not start a full reload. Disable/pause the failed trigger only if it will keep writing bad files. Watermark is updated AFTER successful copy — never rewind a watermark without DR assessment.
- OpenFlow: do not drop flow files; error routing must stay explicit.
- Snowflake task graph: suspend the affected graph (D365: suspend → do not alter until Stage 6). Do not re-enable task dependents yet.
- D365 entity ERROR: leave ERROR. Do not recycle. Do not roll the last-processed checkpoint backward.
- Dynamic tables: if SUSPENDED, record it; do not RESUME until Stage 6.
- Downstream: if a report/dashboard is serving the bad slice, say so in the INC using the standard customer-comms structure. Do not silently refresh a dashboard over untrusted FACT.

**Exit:** Bleed stopped or explicitly judged unnecessary. Evidence pack updated with what was paused.

### Stage 4 — Bisect the layer

**Goal:** Name the failing layer and rank the credible causes before writing a fix.

**Action:** Reproduce with evidence (logs, row counts, sample keys). Bisect in this order and stop at the first broken hop: source system delivery → ADF/Azure Function/Blob → OpenFlow → Snowflake RAW → STAGING/HISTORY/STAGED → INGESTED → FACT/DIM → Consumer. D365-specific fast triage: source delivery → stage access → metadata → registry state → task history → processing errors → worker assignment → replay queue → STAGED-vs-INGESTED freshness. Do not reset checkpoints because a live comparison looks behind. SQL Server source: check CDC/Change Tracking LSN vs ADF last-success. Streamlit: separate query/data failure from widget/CSS empty-state.

After the first broken hop is identified, return the three most likely causes—or fewer when fewer are credible—in this format: Rank | possible cause | confidence % | supporting evidence | contradicting/missing evidence | quickest confirmation or rejection check | proposed fix. Confidence percentages express investigative confidence, not statistical certainty, and do not need to total 100%. Base them only on current evidence and comparable Library history; never invent causes to fill three rows.

At **95% or above**, lead with the precise evidence-backed solution and its verification check. Still show other credible options when useful, but label them as alternatives with their evidence, trade-offs and confidence; do not present them as equivalent conclusions or let exploration displace the recommended solution. Below **95%**, do not present any cause as established: request or run the quickest discriminating checks, then rescore.

**Exit:** Single failing layer named, with the query/log that proves it, plus ranked hypotheses or a ≥95%-confidence cause. If the failure is silent at FACT (job green, data wrong), loop to observability playbook Stage 1 with this evidence — do not invent a code fix.

### Stage 5 — RCA

**Goal:** Cause, not symptom.

**Action:** Write four lines: symptom (what the consumer saw); immediate mechanism (what object failed); root cause (why that object failed, supported at ≥95% confidence by a source-of-truth check—or explicitly marked provisional below that threshold); blast radius (objects, dates, reports, whether data already landed downstream). If root cause is a vendor/source feed, the INC stays open until backfill + consumer validation. If root cause is a bad deploy, hand to DR for rollback-vs-forward-fix; keep this playbook for verify/document.

**Exit:** RCA four-liner recorded on the TICK. No production write before this exit unless Stage 3 contain already required one.

### Stage 6 — Fix

**Goal:** Smallest idempotent reversible change that restores the pipeline.

**Action:** Provide the exact operator runbook, expected result and verification checks. the Library owner or an authorised operator performs system changes and confirms each completed action. Prefer replay / delta or rolling rebuild over full rebuild. D365: use the entity-folder replay queue and the metadata-recovery scan, never checkpoint rewind. Do not run the bulk load procedure concurrently with the live trickle feed unless the Library owner explicitly plans it. ADF: Git branch → PR; never a live-mode prod edit. Snowflake: verify DDL before prod; preserve future grants/ownership — the ownership-drift detector only detects, never auto-transfers ownership as an incident fix. Fix must be reversible; if not, it is a DR forward-fix: freeze first, then return. Route the fix itself through Testing & Validation (PLAY-0019) before calling it resolved. Snowflake remains deployed truth for existing legacy objects. Before changing a legacy script, procedure or task, export its current deployed definition into the Library; store every new or changed definition there. If the stored definition is more than 90 days past its last explicit verification, ask the Library owner whether it changed or request the current Snowflake definition before relying on it.

**Exit:** Operator-confirmed change applied in the failing layer only with returned evidence, or blocked pending the Library owner/vendor.

### Stage 7 — Verify

**Goal:** Prove the consumer is correct, not that the job is green.

**Action:** Failed object now succeeds on a controlled run; row counts/keys for the affected window checked vs source; downstream refresh actually happened (report, dashboard); no new ERROR/stuck IN_PROGRESS/suspended DT in the same graph; D365 registry not left IN_PROGRESS, replay queue drained or explicitly remaining. Record checks in the TICK's evidence field. Do not mark done without them.

**Exit:** Verification evidence on the TICK, or failed → loop to Stage 4. "Job succeeded" is not an exit. "DT resumed" is not an exit. Named-consumer refresh is required.

### Stage 8 — Document and close

**Goal:** Next incident does not start from zero.

**Action:** Update the owning Project and any Knowledge constraint the RCA changed. If the miss was "job green, data wrong" or "monitoring should have caught this", record the exact evidenced monitoring gap in the owning work. Append an existing observability owner only within authorised scope; a separate Ticket/Project or platform investigation requires authority and need. Close the Freshservice ticket + Library via the standard ticket-field/ownership rules. Draft the recovery notification through the appropriate comms playbook for the Library owner to review and send; record actual notification only on confirmation. Update a runbook/spec if it's now wrong. Update the Ticket to done only after PLAY-0019 confirms it.

**Exit:** TICK done only with evidence; monitoring gap and accountable next action recorded if a gap remains; a separate follow-up is not compulsory.

## Decision gates

| Gate | After | If | Then |
|---|---|---|---|
| Wrong domain | Stage 0 | Trading / personal trading | Stop. Do not continue. |
| Wrong machine | Stage 0 | Silent data / no error | Observability playbook |
| Wrong machine | Stage 0 | Need freeze/rollback first | DR playbook |
| False positive | Stage 1 | Alert fired on healthy data | Stop; flag the alert threshold/rule for review; do not proceed |
| Severity unclear | Stage 2 | Urgency is a judgement call | Stop, ask the Library owner; do not invent a severity level |
| D365 invariants | Stage 4/6 | Checkpoint rewind proposed | Refuse; use replay |
| Symptom vs cause | Stage 5 | Snowflake object healthy, source collapsed | Keep INC open; vendor path; observability blast-radius |
| Unreversible fix | Stage 6 | Change cannot be undone | DR freeze → rollback-or-forward-fix |
| Green job, bad consumer | Stage 7 | FACT ok, dashboard stale | Do not close; downstream refresh required |
| Monitoring gap | Stage 8 | Catch should have existed | Record evidenced gap in owning work; separate follow-up only when authorised and needed |

## Loop-backs

| Signal | From → To | Rule |
|---|---|---|
| New error after contain | Stage 3 → Stage 1 | Recapture; do not skip evidence |
| Scope wider than captured | Stage 4/6 → Stage 1 | New downstream consumer found mid-fix; re-scope blast radius before continuing |
| Bisect was wrong layer | Stage 6/7 → Stage 4 | Keep contain; re-bisect |
| Verify fails | Stage 7 → Stage 4 | Do not widen the fix until layer is re-proved |
| RCA shows bad deploy | Stage 5 → DR Stage 1 | Freeze; this playbook resumes at Stage 7 after restore |
| RCA shows silent FACT failure | Stage 4/5 → Observability Stage 1 | Carry evidence pack |
| Same gap loops twice | Any | Escalate to the Library owner; stop cycling |

## Overall exit

Done when all of these are true: failing object healthy on a controlled run; affected date/key window matches source, not only downstream cache; named consumers refreshed and checked; RCA four-liner on the canonical TICK; fix has passed Testing & Validation; containment lifted or explicitly left in place with owner + review date; affected customer/stakeholder notification confirmed by the Library owner or retained as a named pending send; monitoring gap recorded in owning work or explicitly "no gap"; ticket status reflects only what has actually been verified. "Job succeeded" is not an exit. "DT resumed" is not an exit.

## Hand-offs

| Direction | Target | What moves |
|---|---|---|
| From | Mission Control | Sized incident ask + trail |
| Uses | the approved reproduce/bisect/fix procedure | Reproduce, bisect, idempotent fix |
| Uses | the approved feed-recovery invariants | D365 recovery invariants |
| Uses | current platform documentation | ADF / OpenFlow / Snowflake facts |
| Uses | the verified customer-ticket ownership rules / the current ticket-writing policy | Verified customer-ticket ownership + TICK/customer text |
| Uses | the owner-approved ingestion architecture | Rebuild-mode only; not a build-from-scratch |
| Uses | the current Ticket schema | Ticket fields (priority, evidence) this playbook's stages populate |
| Uses | PLAY-0019 | Testing & Validation, for confirming the fix before closing |
| Uses | Customer/Stakeholder Communication playbooks | Notifying affected parties |
| To | Pipeline observability response playbook | Silent FACT / false-positive / blast radius |
| To | Disaster recovery/rollback playbook | Freeze, rollback vs forward-fix |
| To | Data documentation | Runbook/spec update |
| Never | Trading-specific Knowledge | Trading is out of scope |

Does not mint IDs. Does not edit Project Intake artefacts / Chats / markers.

</details>

## Guardrail correction — 2026-10-13

Requirement Gatherer, Reliability and Documentarian: urgency is evidence/decision-led; monitoring gaps remain in existing authorised work; communications remain drafts until the Library owner confirms a send.
