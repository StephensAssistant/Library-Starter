---
id: PLAY-0032
type: playbook
title: Pipeline Observability Response — Silent Failure
status: current
created: 2026-08-15
updated: 2026-10-13
owner: the Library owner
links: [HAT-0004, PLAY-0006, PLAY-0010, PLAY-0020, PLAY-0027, PLAY-0029]
tags: [playbook, pipeline-observability, silent-failure, blast-radius, triage, monitoring-gap]
migrated_from: PLAY-0032-old-library
---
# Pipeline Observability Response — Silent Failure

## Trigger

Within a Freshservice ticket, Library Ticket or Library Project, data looks wrong despite a possibly successful job. The signal may be a Snowflake data-quality flag or a direct business report of an unexpected value, volume, freshness or missing amount.

## Method

Use [[PLAY-0020]] and relevant Library evidence to compare source, pipeline layers and consumers; classify REAL/FALSE/INCONCLUSIVE; rank likely causes; identify blast radius; and provide the shortest diagnostic and recovery plan. the Library owner or an authorised operator executes system actions and returns evidence. Verify every affected consumer; alert clearance alone is not restoration.

## Stop

Consumers verified or named blocker. Never infer FALSE from missing evidence or presume a monitoring platform exists. Record a monitoring gap without automatically building one.

AGENTS.md owns shared authority, evidence reuse and task boundaries. The AI has no implied operational access to Snowflake, ADF, OpenFlow, Qlik, Sigma, Streamlit, source systems or Freshservice; system actions remain recommendations until confirmed.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

> Use manual evidence until the owner verifies that automated discovery is deployed and suitable for this pipeline.

## Scope and domain

the owner’s BI only (Snowflake FACT/DIM, D365 INGESTED, Qlik / Sigma / Streamlit / Public Reporting). Trading / personal trading is out of scope.

Use within a Freshservice ticket, Library Ticket or Library Project when the pipeline **did not throw**, or threw only a monitoring/DQ alert, and the question is "is this real, how far did it go, patch now or later, tell downstream". Keep diagnosis, decisions, evidence, customer updates and next actions in that same work record.

## Boundary vs other playbooks

**Incident Response (PLAY-0020)** owns the thrown-error / known-failure path: a hard failed run with an error object, a failed ADF/Snowflake job, a D365 entity ERROR, a Freshservice incident raised as a pipeline outage. Its current routing explicitly hands silent wrong/stale data to this entry. **This entry owns the silent-failure case** — data wrong with no thrown error; the earlier migration overlap is historical, not an unresolved current route. PLAY-0020 Stage 4 explicitly loops here when the failure is silent at FACT (job green, data wrong), and this entry loops back to PLAY-0020 Stage 4 if a hard error appears mid-flight.

**Pipeline Architect (PLAY-0010)** is pre-implementation design and does not overlap. Designing or building the observability framework itself is the observability project's own work, not this response playbook.

Unsafe live change already applied → Disaster Recovery & Rollback (PLAY-0029) first.

## Nest under Mission Control

Layer, not a new front door. Mission Control still routes. This playbook never self-triggers around it.

Precedence: the observability project wins on what the observability system will be (not yet implemented at time of migration). Snowflake layer/z-score knowledge wins on layer facts. D365 freshness/replay knowledge wins on that domain. Two worked silent-failure tickets win as precedent. This entry wins only on the response state-machine while the observability project is still pre-build.

## Trigger

Enter when all of these are true:

1. A Freshservice ticket, Library Ticket or Library Project is the work context. When a Snowflake data-quality flag or direct business report initiates work outside an existing record, create the Library Ticket only after the Library owner instructs it; otherwise stop and establish the correct work record before investigation.
2. Mission Control trail present; else return to Mission Control.
3. the owner’s data path (Snowflake FACT/DIM, D365 INGESTED, Qlik/Sigma/Streamlit/Public Reporting).
4. At least one of: dashboard/report gap or "numbers look wrong" with no failed ADF/Snowflake job; volume/row-count collapse or spike vs recent baseline; dynamic table SUSPENDED / lag breach / target-lag miss; an ownership-drift OPEN row from the daily drift-check task (detect-only); a DQ flag or future observability alert; source file present but INGESTED/FACT not moving.

Do not enter when: copy/task/ADF failed with an error (PLAY-0020); the Library owner asked to design the observability framework (the observability project's own build work, not this response playbook); trading performance / backtest / live cBot (stop).

**Constraint (manual evidence only).** The observability project's stored procs are not implemented, and auto-detect of new tables is not live at time of migration; the per-pipeline AI-agent idea is not decided. This playbook runs on manual evidence: task history, account usage views, dynamic-table metadata, row-count SQL, source-file checks, reload history. Do not pretend an alert platform exists.

## Stages

### Stage 0 — Domain and machine gate

**Goal:** Right playbook, the owner’s only.

**Action:** If trading, stop. If a hard error is already in hand and uncontained, PLAY-0020 Stage 1. If a bad deploy is live, DR Stage 1. Else continue.

**Exit:** Silent/alert-shaped the owner’s data issue confirmed within its Freshservice ticket or Library Project, or routed away.

### Stage 1 — Real vs false positive

**Goal:** Decide **REAL**, **FALSE**, or **INCONCLUSIVE** before touching data or paging anyone.

**Action:** Search the relevant Library Ticket, Project, Knowledge, architecture, stored scripts/procedures/tasks and prior comparable incidents. For a business-reported anomaly, record the reported actual value, expected value or missing amount, metric definition, store/entity, date/window, filters, comparison basis and where the figure was observed; keep the report as an evidenced symptom, not proof of a pipeline defect. Use accessible evidence for the following checks; where live access is unavailable, provide the exact query, file request or UI check for the Library owner or an authorised operator and wait for returned evidence. Do not skip the source-file check when the object is file-fed.

- **A. Job health:** ADF last success; Snowflake task state; dynamic table state (SUSPENDED/RUNNING); D365 entity registry (IDLE/ERROR/IN_PROGRESS).
- **B. Volume vs baseline:** compare INGESTED, FACT and the consumer metric at the same grain against the strongest available like-for-like history. Account for calendar, seasonality, promotions, known source behaviour and structural changes. Score whether the observed variance represents a real failure using the combined evidence; do not use a universal z-score threshold.
- **C. Freshness:** max load-date / last-refresh timestamp vs expected lag (D365 INGESTED default lag noted per entity in the freshness knowledge).
- **D. Source-of-truth:** open the source file or upstream API/export. Snowflake-side "healthy" is not proof — if the source collapsed by a large margin, it is REAL even if downstream tables refresh cleanly.
- **E. Known noisy checks:** an ownership-drift OPEN row that matches an already-accepted exception is likely FALSE. `[NEEDS OWNER: list of accepted drift exceptions / current OPEN noise.]`
- **F. Calendar/seasonality:** do not call a weekend/sale-day dip FALSE without a like-for-like prior period.

A Snowflake alert and a business report are both entry evidence; neither is automatically the root cause or final verdict. Verdicts require evidence-based confidence. **REAL** at ≥95% confidence: source, layer or consumer disagrees with expected grain, volume or freshness and the mechanism is evidenced. **FALSE** at ≥95% confidence: the apparent issue is explained by an expected empty source, governed exception, UI empty-state or display artefact. **INCONCLUSIVE**: neither verdict reaches 95%, or source/baseline access is missing; request the quickest discriminating evidence and never collapse missing evidence into FALSE.

PLAY-0020's current Method also admits REAL/FALSE/INCONCLUSIVE; both paths preserve uncertainty. A missing-evidence case is never to be collapsed into FALSE.

After the verdict, return the three most likely causes—or fewer when fewer are credible—in this format: Rank | possible cause | confidence % | supporting evidence | contradicting/missing evidence | quickest confirmation or rejection check | proposed fix. Confidence expresses investigative confidence, not statistical probability, and scores need not total 100%. Rank downward from the strongest evidence and never invent causes to fill three rows. Lead with a precise fix at 95% or above; below 95%, run or request the quickest discriminating check and rescore.

**False-alert communication:** When the verdict is FALSE, prepare a human follow-up for the Library owner to review and send under [[PLAY-0027]] to the original reporter and any audience previously notified. Explain the evidence, why the apparent variance or alert occurred, confirm that no data failure was found, and provide any useful interpretation guidance. Record sending only after the Library owner confirms it was sent.

**Awareness communication:** If the flag concerns data already available to business users, prepare an immediate human, STAR-based business-wide email under [[PLAY-0027]] stating that the issue is known and under investigation, the potentially affected data/reporting window and business impact if evidenced, any safe-use guidance, and the next update point. Freshservice or the Library Ticket remains the work record, not the default broadcast channel. This email does not require a ≥95% root-cause verdict, but must distinguish suspected impact from confirmed facts and must not claim a cause or fix. Record sending only after the Library owner confirms it was sent.

**Exit:** Verdict + the query/file that justifies it. No resume/merge yet.

### Stage 2 — Blast radius

**Goal:** Name every consumer of the bad slice before choosing speed.

**Action:** Walk downstream from the broken grain: the object itself; same-graph dependents; the reporting layer (governed reporting schemas vs BI-managed schemas); consuming apps (Qlik, Sigma — a migration may be in flight, `[NEEDS OWNER]` which apps are still Qlik vs Sigma — Streamlit, Public Reporting); the time window and keys affected; whether consumers already cached the bad window.

Write a radius card: objects, window, consumers, already-served-to-business yes/no.

**If already served, prepare the mandatory business notification promptly for the Library owner to review and send before RCA.** Do not wait for a perfect RCA. If sending is pending, record that communication dependency and owner; the AI never sends or treats a draft as notification.

**Exit:** Radius card. Notification sent or explicitly "not yet served".

### Stage 3 — Patch-now vs planned work

**Goal:** Choose speed without pretending capacity.

**Action:** Recommend patch-now versus planned work from verified impact, recorded priority and current change authority in the active Ticket, Project or conversation. Live wrong data, stuck processing, suspended tables, source collapse, historical-only slices, compensating controls and vendor/backfill windows are impact/dependency evidence, not automatic urgency or timing rules. Retain P1 or another priority only when recorded; if priority or consequential timing is missing or ambiguous, use SKILL-0318 to ask the Library owner the independent decision questions before dependent prioritisation. Verify the change window, authorised operator and required approver before recommending execution; never infer response clocks, working hours or standing approval. For planned work, record waiting-on and a review date only when explicitly known; creating a schedule requires separate authority. Do not leave the work unflagged.

**Exit:** Evidence-based recommendation and any agreed timing/priority recorded, or the exact unresolved decision and dependent action blocked. For planned work, containment recommendations under PLAY-0020 Stage 3 still require the applicable authority; planned status creates no schedule.

### Stage 4 — Execute the response at the broken layer

**Goal:** Restore truth at the correct layer; do not paint the dashboard.

**Action:** Recommend the exact operator action and verification evidence; never claim it occurred without confirmation. If a hard error appears during this stage → PLAY-0020 Stage 4 with the radius card. Source REAL (vendor/feed): do not "fix" FACT to invent rows — escalate the vendor, quantify undercount, keep replay ready for backfill. Layer REAL (dynamic table suspended, MERGE stale, worker stuck): smallest restore; D365 uses replay, not checkpoint rewind; resume suspended tables only after source volume is trusted. Consumer-only REAL (FACT correct, Qlik/Public Reporting stale): refresh the consumer, do not rebuild INGESTED. Ownership drift REAL: do not auto-fix — the daily drift check is detect-only, report current owner vs rule and let the Library owner decide the transfer; never issue an automatic ownership transfer as a response action. Rebuild: use the rolling rebuild mode for the affected days; a full rebuild only with the Library owner sign-off.

**Exit:** Action taken at the broken layer, or waiting-on vendor with containment held.

### Stage 5 — Close loop with each named consumer

**Goal:** Every named consumer in the radius card is either refreshed+checked or explicitly out of window.

**Action:** For each consumer on the card, identify the authorised owner and provide the refresh/validation step. After operator confirmation: compare the affected window to the restored FACT/source, not to the previous dashboard; tick the consumer off the card with evidence (row counts, screenshot, or query). A worked precedent found FACT validated at a specific row count while a downstream reporting surface still showed the old, much larger figure — the ticket must not close on FACT validation alone. If a consumer owner is unknown, identify one from current records or ask one targeted question; record the ownership gap rather than guessing.

After all affected consumers are verified, prepare a human, STAR-based resolution email under [[PLAY-0027]] for the same confirmed business audience. State that the issue is resolved, the affected metric/report and period, the verified restoration outcome, and any action users need to take. Do not announce resolution from a successful job alone; record sending only after the Library owner confirms it was sent.

**Exit:** Radius card all green and required resolution email confirmed sent, or remaining consumers and communication explicitly named on waiting-on.

### Stage 6 — Monitoring gap → the observability project

**Goal:** The next silent FACT failure is not discovered by a user.

**Action:** Write the gap as a concrete check, not a slogan. Candidate checks from the live Library: alert on a dynamic table SUSPENDED state; alert on an INGESTED volume or business-metric deviation whose evidenced, seasonality-adjusted rule reaches the agreed 95% confidence threshold; alert on a D365 entity ERROR/IN_PROGRESS beyond a time threshold; alert on last-refresh older than target lag + tolerance. Preserve the evidenced gap, proposed check, accountable owner and next action in the owning authorised work record. Update existing observability Project/backlog records only when authorised and needed; do not create a compulsory follow-up record. Do not implement the framework inside this incident. Do not invent that auto-register-new-tables already exists.

**Exit:** Evidenced gap and accountable next action preserved in the owning work, with any authorised existing-record update identified; or explicit "check already would have caught this and failed for reason X".

## Silent fact-table failure — mandatory path

This is the case the observability project exists to catch. Until that system is built, treat this path as **default** for any FACT/DIM that "succeeded": (1) the source-file/upstream-count check is mandatory, not optional; (2) compare INGESTED vs FACT vs consumer for the same grain and date; (3) if INGESTED collapsed and FACT did not, FACT is stale or isolated — radius includes both; (4) if FACT collapsed and INGESTED did not, stop at the FACT merge/dynamic-table step, do not rebuild RAW; (5) if all three collapsed, it is a source incident, Snowflake-side resume is containment at best; (6) close only after Stage 5 consumers match the restored grain.

Worked precedent (do not copy blindly): a loyalty dashboard went missing for several days; the mechanism was three suspended dynamic tables; the cause was a vendor export racing an upstream batch, a large order-volume drop confirmed on source files. Close required backfill + the downstream reporting surface + the dashboard, not table resume alone. Monitoring follow-up remains on the observability project.

## Decision gates

| Gate | After | If | Then |
|---|---|---|---|
| False positive | Stage 1 | FALSE | Document; prepare the required false-alert follow-up for the Library owner to send; keep communication pending until confirmed; no patch |
| Inconclusive | Stage 1 | Missing source access | Halt `[NEEDS OWNER]`; never FALSE |
| Already served | Stage 2 | Business already saw bad numbers | the Library owner reviews/sends the prepared notification; record confirmation before RCA |
| Speed | Stage 3 | Live consumer wrong or feed still collapsing | Assess impact against recorded priority/current change authority; recommend patch-now only when supported, otherwise obtain the Library owner’s unresolved urgency/timing decision |
| Speed | Stage 3 | Vendor backfill owns the rows | Record the dependency and recommend planned work/authorised containment from recorded priority and agreed timing; no automatic schedule and no fabricated FACT |
| Drift | Stage 4 | Ownership OPEN | Report only; no auto-transfer |
| Downstream unpaid | Stage 5 | FACT ok, cache stale | Do not close |
| Silent miss | Stage 6 | User found it, not a check | Preserve the evidenced monitoring gap, owner and next action in owning authorised work; update existing observability records only when authorised and needed |

## Loop-backs

| Signal | From → To | Rule |
|---|---|---|
| Source check overturns "healthy" dynamic table | Stage 4 → Stage 1 | Re-verdict REAL; expand radius |
| Hard error appears | Stage 4 → PLAY-0020 Stage 4 | Carry radius card |
| Resume table then volume still dead | Stage 5 → Stage 1 | Do not close |
| New consumer found | Stage 5 → Stage 2 | Extend radius; re-notify if served |
| Scheduled vendor fix lands | waiting → Stage 4 then 5 | Validate window, then downstream |
| Same gap loops twice | Any | Escalate to the Library owner; stop cycling |

## Overall exit

Done when all of: REAL/FALSE/INCONCLUSIVE-resolved is recorded with evidence; a FALSE verdict has been explained to the reporter and any notified audience; if REAL, broken layer restored or vendor waiting-on is explicit and radius consumers closed or named; if already served, business was told with the window of unreliability and received a verified resolution email after restoration; monitoring gap, evidence and accountable next action preserved in the owning authorised work, with existing observability records updated only when authorised and needed, or the check justified as already covered; the Ticket's evidence field holds the checks, not just the conclusion.

"Alert cleared" is not an exit. "DT resumed" is not an exit. "FACT looks fine" is not an exit while a downstream surface is stale.

## Hand-offs

| Direction | Target | What moves |
|---|---|---|
| From | Mission Control | Alert / "numbers wrong" ask + trail |
| Uses | Snowflake layer/anomaly knowledge | Layers, evidence-based confidence, ownership-drift detect-only |
| Uses | D365 freshness knowledge | Lag, ERROR terminal, replay |
| Uses | Qlik/Streamlit consumer knowledge | Consumer behaviour |
| Uses | Ticket-field/notify knowledge | Notify + field mechanics |
| Uses | Rebuild-mode knowledge | Rolling mode only; not a build-from-scratch |
| To | PLAY-0020 | Hard error found mid-flight |
| To | Disaster Recovery & Rollback (PLAY-0029) | Bad deploy caused the silent state |
| To | The observability project | The check that should exist |
| To | The two worked precedent tickets | Precedent only; reopen only if same incident |
| Never | Trading Knowledge | Trading is out of scope |

Does not mint IDs. Does not implement the observability project itself.

## [NEEDS OWNER]

Preserved verbatim from the old Library. Do not answer, fill, or delete these here.

1. Accepted ownership-drift exceptions must be verified from the governed exception source for the affected object; absent evidence means INCONCLUSIVE, never FALSE.
2. Missing source, baseline or consumer access is recorded per incident and produces INCONCLUSIVE until the authorised owner supplies evidence.
3. Current Qlik/Sigma/Streamlit/Public Reporting consumers and their owners are discovered from the affected record and dependency path; never rely on a static estate-wide list during migration.
4. Current change window and production approver are verified per incident; no fixed hours or standing approval are assumed.

</details>
