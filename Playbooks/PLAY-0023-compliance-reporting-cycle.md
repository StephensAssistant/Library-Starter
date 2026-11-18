---
id: PLAY-0023
type: playbook
title: Supplier Compliance Reporting Cycle — Periodic Gather, Validate, Submit
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0013, PLAY-0019, PLAY-0040]
tags: [playbook, compliance, supplier-compliance, reporting-cycle, reconciliation]
migrated_from: PLAY-0023-old-library
---
# Supplier Compliance Reporting Cycle — Periodic Gather, Validate, Submit

## Trigger

A named supplier-compliance period is requested.

## Method

The customer submits the complete export and reporting-period dates through the GoRamp Streamlit app. The app automatically normalises and validates headers, replaces RAW, processes STAGING and INGESTED, refreshes the reporting fact table and returns success or error. Routine live periods require no BI intervention or per-period sign-off; run detailed validation and acceptance only during development/UAT, after a material change, or when an error, anomaly or reported issue occurs.

## Stop

Period verified/released within authority or a precise missing source. Acceptance is a development/UAT release gate, not a recurring live-period gate. No guessed charge definitions; unrelated legal/EPR work does not route here.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

## Scope

owner-managed supplier-compliance period close and report only. Other regulatory, contractual or compliance processes—including EPR—must use their own defined workflow and must not be merged into this playbook.

## Trigger / entry condition

Use this playbook when any of the following is true: a owner-managed supplier-compliance reporting period is ready for upload/refresh/reporting use; the Library owner asks to run, close, or check a supplier-compliance period; a customer supplies a new extract for a named accounting period.

Do not enter claiming a completed cycle if the owning Project is blocked or waiting on the customer/colleague.

Wrong door: an ad hoc data question about compliance figures outside the reporting cycle is a normal data request, not this playbook.

## Period fact (do not substitute calendar months)

The customer determines each reporting period by submitting its start and end dates through the GoRamp Streamlit app. Those submitted dates are authoritative for that cycle and must not be replaced with assumed calendar-month boundaries. Evidenced example: Period 05 / June 2026 = 2026-05-30 to 2026-07-03.

## Stages

### Stage 1 — Confirm period and blockers

**Goal:** Know which accounting period this run is, and whether the cycle may proceed.

**Action:** Read the owning Project (work state, waiting-on, next action, evidence). Do not plan from the status board alone. Read the period start/end from the customer's GoRamp Streamlit submission, not from a month label or assumed calendar. If waiting on a customer/colleague for charge definitions or source mappings, record the blocker; do not proceed to a "released" claim. If the request is not supplier compliance, stop and route it to its own defined workflow.

**Exit:** Period dates stated, or EPR parked; blocker named or cleared. If blocked, overall exit is "cycle not run — waiting", not done.

### Stage 2 — Preconditions

**Goal:** Sources and governed config are ready for this period's universe.

**Action:** Source extract for the period exists (customer's export is the snapshot/row universe). Exemption/exclusion configuration is current for this run: blanket/PO exemptions, charge exclusions, buyer list, charge rates (effective-from entered; effective-to is calculated, never stored). Scope in force per the department-type filter agreed with the customer. Do not add new charge types until definitions, source fields, rates, and effective dates are confirmed. Known unsourced/open items stay visible rather than silently closed.

**Exit:** Preconditions listed as ready, missing, or blocked. Missing items are `[NEEDS the Library owner]` or waiting-on — never filled by guess.

### Stage 3 — Upload source snapshot

**Goal:** Land the period file by column name into the raw layer with the correct period window.

**Action:** Use the GoRamp Streamlit uploader with the customer-supplied period-start/period-end dates set before upload. Require the complete GoRamp export: the upload truncates and replaces RAW, normalises known headers, rejects unknown or missing required headers, then merges STAGING by GoRamp ID and loads the persistent INGESTED history. A resubmission updates included IDs and inserts new IDs; omission alone does not delete an existing persistent record and must not be treated as deletion evidence. Prefer upload close to period end, since a late upload pulls more late-raised cases into the window.

**Exit:** Upload succeeded; period start/end/load date, source filename, RAW rows loaded, STAGING rows inserted/updated and row errors recorded. Unknown or missing headers are resolved or the run stops.

### Stage 4 — Automatic processing and exception validation

**Goal:** The automated pipeline produces the reporting fact table; detailed BI validation is invoked only for development/UAT, material change or exception.

**Action:** The Streamlit app automatically runs RAW → STAGING → INGESTED → fact refresh. Do not require routine BI action for a successful live upload. During development/UAT, after a material change, or when the app reports an error or output appears anomalous, run mechanical checks (precedent, not invented thresholds): row count equals unique `GORAMP_ID + PO_NUMBER` keys at the fact grain; exemption and Additional Charge detail/aggregate joins do not fan out; flag-count equals amount-count per wired charge type; missing-rate counts are zero; department-type filtering excludes Concessions while that rule remains approved; PO identifiers are normalised for comparison; unknown status/reason mappings remain visible rather than defaulted. Record what was queried and the numbers — intention is not evidence.

**Exit:** For a routine successful live period, the app's returned completion evidence identifies the submitted period and completed processing. For development/UAT, material change or exception, all required mechanical checks pass with recorded figures, or the run stops with the failing check named.

### Stage 5 — Conditional business validation

**Goal:** When development/UAT, a material change or an exception requires review, labels, rates and inclusions match the customer's confirmed mapping; otherwise skip this stage for routine live periods.

**Action:** Use confirmed terminology from the customer, not an earlier assumption. Recheck seeded rates and labels after any mapping change. Apply agreed inclusion rules (e.g. a damage category the customer wants included in full) even where a finer split remains unresolved upstream. Do not assume downstream population (e.g. a buyer list) is complete without checking. Do not claim a downstream release (e.g. a reporting-tool script) if that work is still open. During development or UAT, missing required customer/external sign-off means blocked, never done. Once the process is live, per-period sign-off is not required unless a material change or exception reopens acceptance.

**Exit:** During development/UAT, customer/business sign-off is recorded as evidence or waiting-on is named. In live operation, validation evidence is sufficient unless a material change or exception requires renewed acceptance. Open mapping/source gaps remain listed.

### Stage 6 — Record exceptions or material movement

**Goal:** Preserve evidence for development/UAT, material changes and exceptions without creating administrative work for every successful live period.

**Action:** For development/UAT, a material change or an exception, update the owning Project's evidence/next-action/waiting-on in place. A routine successful live upload requires no Library update. Do not create a second project. If a pipeline/reporting/runbook doc is requested, inspect tables, never invent columns, and flag gaps. Library write-back is not complete until read back; simulation is never a production mutation.

**Exit:** For development/UAT, material change or exception, the canonical Project entry (and any requested doc) is read back and its evidence field contains checks run. A routine successful live period requires no Library update.

## Known gaps carried forward

Outstanding source-mapping and consignment-level gaps from the owning Project are carried forward explicitly, not silently omitted. A fee-amount discrepancy class discovered during a prior customer review round is a known discrepancy class for this cycle — route genuinely uncertain figures through Testing & Validation (PLAY-0019) rather than assuming they are correct because they came from the source system.

## Decision gates

- Owning Project blocked/waiting → stop at Stage 1. Chase; do not fabricate completeness.
- Request is not supplier compliance → stop and route it to the applicable separate workflow.
- Unknown source header → update the column map or abort upload.
- Row fan-out, flag/amount mismatch, or an obvious mapping failure → do not publish; loop to Stage 3/4.
- New charge type proposed without definitions/sources/rates/effective dates → do not seed.
- Development/UAT release sign-off required and absent → blocked, not done. Once live, do not create a per-period approval gate unless a material change or exception requires it.

## Loop-backs

- Failed mechanical validation → identify the failed layer and retained RAW/STAGING/INGESTED state before proposing a bounded authorised repair or resubmission, then recheck Stage 4. Preserve the complete source file and submitted period; omission is not deletion evidence. Do not repeat an unchanged upload or claim that partial processing completed.
- Rate edit not visible in the fact table → force a refresh; re-run Stage 4 amount checks.
- Customer mapping correction → correct the rate configuration (distinguishing a seeding error from a genuine effective-date change), refresh the fact table, recheck labels, return to Stage 5.
- New header variant in a later period → Stage 3 column-map update, then Stage 4.

## Overall exit

The period cycle is done only when all are true: named accounting period-start/end loaded via the uploader; routine live success evidenced by the app's completion result for the named period; detailed mechanical checks (counts, grain, scope filter, flag/amount tie-out, no mapping collapse) recorded when development/UAT, material change or exception requires them; development/UAT release sign-off is recorded when applicable; live periods require no recurring sign-off unless a material change or exception reopens acceptance; open gaps remain visible, not silently closed; the owning Project (and any doc) updated/read back when development/UAT, material change or exception requires it, with no terminal claim without inspected evidence.

A blocked wait on a customer/colleague/leave is a valid overall exit. It is not done.

## Hand-offs

- PLAY-0019 — Testing & Validation, for uncertain figures needing verification.
- Data documentation knowledge — spec/dictionary/runbook after a real run.
- Pipeline architecture knowledge — schema, procs, rates, header map.
- Ingestion build knowledge — if layer SQL/rebuild mode is in play; do not diverge from the governed architecture.
- The owning compliance Project — canonical work record.
- Security/access playbook — a platform/privilege failure during upload.

## Anti-patterns

- Treating "June" as the 1st to the 30th.
- Loading the source extract by column position.
- Reporting out-of-scope rows in the fact table while the agreed department-type filter stands.
- Seeding a new charge type "because it looks related" to an existing one.
- Claiming a downstream release while the underlying build is unfinished.
- Marking the cycle done because the upload button succeeded.
- Closing an open source-mapping gap by assumption.

## [NEEDS the Library owner]

Preserved verbatim from the old Library. Not answered, not filled, not deleted here.


</details>

## Guardrail correction — 2026-10-13

Data & BI Lead, Tester and Documentarian: reconciled conditional validation/recording exits with routine automated operation and specified partial-processing evidence before bounded retry.
