---
id: PLAY-0025
type: playbook
title: Data Source Onboarding — New Feed to Production
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0003, PLAY-0019, PLAY-0020, PLAY-0022, PLAY-0028, SKILL-0002, SKILL-0046, SKILL-0047, SKILL-0048, SKILL-0049, SKILL-0050, SKILL-0263, SKILL-0264, SKILL-0265]
tags: [playbook, data-onboarding, ingestion, schema-mapping, snowflake]
migrated_from: PLAY-0025-old-library
---
# Data Source Onboarding — New Feed to Production

## Trigger

An actual new source/feed is being onboarded.

## Method

Inspect live source shape/access and define grain/keys. Map fields and incremental, late-arrival, duplicate/delete behavior using approved architecture. Build ingestion and reconcile against source, permissions and consumers. Advance watermarks only after successful copy.

## Stop

Verified source delivery, seven calendar days of clean production hypercare and an operational next action. Small additions do not restart onboarding. Use the source-mechanism pattern selected under SKILL-0002 and retain environment-specific controls.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

> Use source-local checks until the owner verifies the shared observability service is deployed and suitable.

Kind: operational state machine (understand source → map schema → ingest → validate known-good → document → production).

## Trigger / entry condition

A new data source needs to be brought into the Snowflake environment — a new D365 entity, a new supplier feed, a new e-commerce platform. Use this once the source and its purpose are confirmed, following Project Intake & Scoping.

Use when the Library owner asks to onboard, land, ingest, or add a new source/feed/entity set that is not yet a owner-managed Snowflake system of record.

Wrong door: adding a field or table to an already-onboarded source is an ordinary Ticket, not a full onboarding cycle. Do not use to cut over consumers off an old running path (migration-cutover, PLAY-0022). Do not start at SQL (Pipeline Architect first if grain/keys/load strategy are unset). Do not use for Qlik/Sigma report rebuild.

## Stages

### Stage 1 — Understand the source

**Goal:** One paragraph that states system, grain, access path, frequency, and owner. Grain must be speakable.

**Action:** Capture source system; owner/contact; access path; volume; frequency; format; schema stability; PII; known pain; what one row means. Build an access matrix naming every required system, execution identity, role, developer and intended consumer, with required versus verified access. For an API-based source, run introspection to discover the actual schema rather than assuming it matches documentation.

File/SFTP precedent (a signed-off supplier-settlement feed): SFTP outbox triggers a move to sent; PGP decrypt; multiple record types in one file; natural keys per type; an empty file is a clean exit, not a fail.

Trickle/CDC-like precedent (D365): Azure Synapse Link → external stage → Snowpark processor → entity registry. PK detection order: RECID → MSERP_<ENTITY>ID → ID → explicit primary key column, with named exceptions. Deletes via an is-deleted flag. Frequency split (15-min vs daily) is a registry fact, not a guess.

ADF principle: metadata-driven, not one pipeline per table. Incremental over full load. Update watermark after successful copy, never before.

If the ask is vague → Session Intake / Grill Me, then return.

**Exit:** Source statement + access matrix confirmed (or each missing permission and owner named as a blocker). Grain is one sentence. The source's shape and access method are confirmed against the live system, not just its docs.

### Stage 2 — Map the schema

**Goal:** Field map, source-mechanism classification and load strategy before any DDL. Decide which physical layers have a necessary responsibility.

**Action:** Inspect real samples (DESCRIBE / information schema / file header / Synapse model JSON). Map source field → destination column → type → key role. Decide load strategy: watermark, CDC/change feed, file last-modified, or trickle/folder fingerprint. Flag any field with unclear meaning or an ambiguous target rather than guessing its mapping.

Architecture gate: use SKILL-0002 to separate three parts. First, document any optional acquisition/orchestration required to move data from the source—such as SFTP → ADF → Azure Blob → OpenFlow. Second, document the governed Snowflake route: a file-based path normally lands in a Snowflake stage, then RAW → STAGING or STAGED → INGESTED; a verified direct connector, API or application may use a different Snowflake landing boundary. Third, add FACT and/or DIM only when reporting grain, reusable business logic, history or consumer requirements justify them; the pipeline may stop at INGESTED. Do not create ceremonial layers; preserve source authority, grain, checkpoints, idempotency, deletes, late updates, lineage, recovery, reconciliation and governed consumer boundaries for every pattern.

Cross-family schema type changes require controlled migration, not automatic DDL (D365 rule — apply to any registered-entity source).

Late-arriving rows, duplicates, and deletes must have an explicit rule. Do not assume MERGE semantics.

**Exit:** Mapping table + classified source mechanism + justified physical layers + load strategy. Open questions are listed, none hidden, and every required field has a confirmed mapping.

### Stage 3 — Build ingestion

**Goal:** Objects exist in non-prod (or isolated prod schema) and one load has landed. Get data flowing reliably, including edge cases from day one.

**Action:** If design is missing → Pipeline Architect, then resume. Then build the SKILL-0002 pattern selected at Stage 2. Build optional acquisition/orchestration first when required. For staged files, use setup → Snowflake stage → RAW source-fidelity landing → STAGING/history with ingestion metadata → governed INGESTED/current state → optional justified FACT/DIM/reporting objects. For managed connectors, APIs/GraphQL, CDC, application writes or derived transformations, implement only layers with explicit responsibilities while preserving the universal control objectives. Apply schema-level privileges to both ALL existing and FUTURE applicable objects, including tables, views and dynamic tables, unless an explicit narrower object or row-level restriction is required. Before each create or replace, determine the required owner from verified current ownership rules and comparable governed objects; set and verify ownership and effective grants after the operation. Apply reconciliation and recovery controls to every pattern.

Naming convention: SP_ / TSK_ / STG_ / FF_ prefixes; databases `INGESTION_[SOURCE]_[ENV]`; never report from RAW.

Historical ownership examples: D365 used SYSADMIN; OpenFlow-managed objects used the OpenFlow admin role; BI-managed reporting used its BI system/writer roles. These examples do not establish current ownership. Use the verified current ownership rules and comparable governed objects required above; conflicting or absent evidence blocks creation/replacement.

Path choice must follow verified source capabilities and current owner-managed architecture: ADF/Function may orchestrate files, OpenFlow may own managed extraction/landing, APIs/GraphQL require explicit pagination or bulk-operation state, and D365 uses its registered trickle pattern. Do not duplicate connector state management or mix unrelated sources' blockers.

Adding an entity to D365: registry + worker assignment + schema cache; do not clone a one-off 5-layer sidecar for a D365 entity.

**Exit:** One successful load in the target env; the selected pattern's source-fidelity landing boundary reconciles to the source (RAW counts for a staged-file route, or the evidenced equivalent for a direct route, with any discrepancy named); objects named to standard. Ingestion runs successfully against real data, not just a sample.

### Stage 4 — Validate against known-good

**Goal:** Idempotent, complete, and comparable to a named baseline before anyone reports from it. Prove the ingested data is correct, not just present.

**Action:**

- Re-run the load; INGESTED/FACT must not double-count (MERGE / source-hash or D365 replay/fingerprint rules).
- Test every recovery mode required by the selected source pattern; staged-file INGESTED tables use delta/full/rolling only where that contract applies.
- Key uniqueness, nulls on keys, freshness (max load timestamp advancing), delete handling.
- Compare to a named known-good: source extract, legacy schema, or prior pipeline. Record known non-blocking anomalies; do not bury them. Run the comparison through Testing & Validation (PLAY-0019).
- Write and retain the checks this source needs. Register them only in a verified live monitoring service.
- Working Playbooks gate: testing → sign-off before live. the Library owner signs.

**Exit:** Known-good pack with evidence (counts, keys, freshness, re-run). the Library owner sign-off recorded on the Project entry.

### Stage 5 — Document

**Goal:** A future operator can rebuild and recover without the original chat.

**Action:** Data Documentation: pipeline technical spec + data dictionary (from real DESCRIBE, never guessed fields) + runbook. Infer-and-confirm audience first. Hand off to Documentation Lifecycle (PLAY-0028) for the technical spec and companion records. D365 additional: short AI maintenance block on each proc (purpose, invariants, dependencies, required validation, smallest-change, return-complete-object); task guidance in the task comment after suspend → alter → re-enable. File into the Library Project (and architecture Knowledge if the pattern is stable). Do not leave the only copy in a notebook.

**Exit:** Spec, dictionary, and runbook exist and name keys, schedule, failure modes, and owner.

### Stage 6 — Hand to production

**Goal:** Scheduled, granted, and the system of record for this source — not yet a cutover of other consumers.

**Action:** Promote using the same object names. Verify the complete access matrix, current-object grants, future grants, effective access and ownership after promotion or replacement. Do not promote while any required system, execution identity, developer or consumer access remains missing or unverified. Separate warehouses for ETL vs BI. Create/resume tasks; observe the first success, then run seven calendar days of production hypercare. Hypercare is an observation and fix-forward window: do not suspend or stop an otherwise running pipeline merely because a defect is found during hypercare; correct and retest it forward through the governed change path. A separate critical incident still routes to PLAY-0020 under its own evidence and authority. Empty-source pre-check where the source can legitimately send nothing. Confirm it's included in the status board's active view if ongoing. Go-live / production changes require the Library owner sign-off. Outstanding engineering (D365 precedent): a repo-first change-control gate is required for final project sign-off even after technical PASS — a technical PASS is not change-control complete.

**Exit:** Task has run successfully on schedule throughout seven calendar days of hypercare; no material defect remains unresolved or unverified; Project entry is live; source-specific observability checks are listed; consumers are named.

## Decision gates / branches

- Grain/keys unset → Pipeline Architect (Specify/Validate), then Stage 2.
- Staged file/SFTP → document and verify the complete acquisition path, including any ADF/Blob/OpenFlow transport, then Snowflake stage → RAW → STAGING/STAGED → INGESTED; add FACT/DIM only when needed.
- Managed connector/OpenFlow → let the connector own evidenced extraction state; add downstream layers only for explicit history, contract, transformation or reconciliation needs.
- API/GraphQL/custom extraction → prove scopes, pagination/bulk completion, stable IDs, checkpoint and replay behaviour.
- Synapse Link/D365 entity → use the D365 registry/trickle pattern; do not create a sidecar merely to mimic staged files.
- Application-maintained or derived data → use controlled write/transaction or transformation controls from SKILL-0002.
- Source mechanism or required control objective unresolved → stop; do not invent architecture.
- Old consumers already exist → after Stage 6 → migration-cutover (PLAY-0022).
- Known-good fail → loop Stage 3; do not schedule prod.
- Access/credentials missing → Stage 1 blocker; `[NEEDS the Library owner]` rather than invent.
- Source's live schema doesn't match its documentation → trust the introspected reality, flag the documentation as stale.
- A field's meaning or mapping is ambiguous → stop and ask the Library owner, do not guess a mapping.

## Loop-backs

- Sample disagrees with assumed schema → Stage 2 (never patch RAW to make it fit).
- Rebuild-from-scratch fails → Stage 3 INGESTED/FACT.
- Production task fails empty vs malformed → Runbook; empty may be success, malformed is not.
- New entity on an existing D365 registry → Stages 2–4 inside that pattern, not a new database.
- If Stage 4's validation reveals a mapping error, return to Stage 2 to correct it before re-running Stage 3's ingestion.

## Overall exit condition

Source understood; schema mapped; ingest idempotent; known-good signed; spec/runbook filed; production task has completed seven calendar days of clean hypercare; any old consumers are handed to migration-cutover rather than silently switched.

Closing boundary: if existing consumers still read an old path, stop here and enter migration-cutover (PLAY-0022) — do not silently re-point them.

## Anti-patterns

- Skip to MERGE SQL → grain, keys, load strategy first (Pipeline Architect).
- Treat Source → FACT/DIM as one rigid chain → separate optional acquisition/orchestration, governed Snowflake landing/ingestion and optional consumer modelling; stopping at INGESTED can be correct.
- Full load every run as default → incremental; watermark after success.
- One ADF pipeline per table → metadata/registry-driven.
- Report directly from ingestion layers → use the governed reporting contract: facts/dimensions → Snowflake Semantic View → per-report golden dynamic table, with only the explicit AGENTS.md exceptions.
- Embed long-lived cloud keys on the stage → storage integration.
- Silent ERROR recycle / move checkpoints back → terminal ERROR; replay idempotent forward-only (D365).
- Invent field meanings → DESCRIBE / sample; flag gaps.
- Treat technical PASS as change-control complete → repo-first gate if the Project states it.
- Onboard by cutting over old consumers in the same breath → this playbook then migration-cutover.

## Hand-offs

- SKILL-0002 — canonical Snowflake ingestion judgement for staged files, connectors, APIs/GraphQL, CDC, application writes and derived transformations.
- PLAY-0019 — Testing & Validation, for the known-good comparison.
- PLAY-0020 — Incident Response, for issues found post-go-live.
- PLAY-0022 — migration-cutover, when an old path still serves consumers.
- PLAY-0028 — Documentation Lifecycle, for the technical spec.
- Hand ongoing monitoring to the owner’s verified observability procedure.
- Pipeline Architect — design before SQL.
- Data Documentation — spec, dictionary, runbook.
- Dashboard Ideation / Sigma Computing — if a report is in scope, after its required facts/dimensions, Snowflake Semantic View and per-report golden dynamic table are verified under AGENTS.md; a golden view requires the Library owner's direction or an evidenced constraint.
- People: the Library owner signs known-good and go-live. Do not invent named colleagues or credentials.

## [NEEDS the Library owner]

The source draft contains no filled-in `[NEEDS the Library owner]` items. It states the convention only, verbatim: "Access/credentials missing → Stage 1 blocker; `[NEEDS the Library owner]` rather than invent." Nothing has been answered, filled, or deleted here.

</details>
