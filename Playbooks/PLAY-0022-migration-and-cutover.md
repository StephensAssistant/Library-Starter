---
id: PLAY-0022
type: playbook
title: Migration & Cutover — Old System to New
status: current
created: 2026-08-17
updated: 2026-11-01
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0003, PLAY-0014, PLAY-0019, PLAY-0025, PLAY-0029, PLAY-0063, PLAY-0064, PLAY-0065]
tags: [playbook, migration, cutover, parity, decommission]
migrated_from: PLAY-0022-old-library
---
# Migration & Cutover — Old System to New

## Trigger

A live system is being replaced.

## Method

Inventory old/new objects and consumers, keep the old baseline usable and define recovery. Build replacement, prove applicable data parity/security/usability and obtain actual cutover authority. Repoint consumers, verify and observe; retire old systems only with separate applicable authorization.

## Stop

Verified migration or explicit rollback/blocker. Preserve D365 checkpoint monotonicity/newer state; no universal parallel-run duration or premature legacy deletion.

AGENTS.md owns shared authority, evidence reuse and task boundaries. Its Production build baseline owns the architecture, access, grants, ownership, testing and seven-calendar-day hypercare controls shared with net-new work; this playbook adds legacy parity, cutover, rollback and decommissioning only when an old system exists.

## Reporting migration architecture baseline

All reporting routes and net-new reporting builds converge on Snowflake-owned modelling: facts and dimensions feed a Snowflake Semantic View; a per-report golden view or golden dynamic table is then built from that Semantic View before consumption by Qlik or Sigma. Sigma remains a replaceable front end: no production modelling belongs in Sigma, except temporary testing; Sigma-specific capabilities such as write-back may still be used.

Verify semantic-view compatibility and compare measured cost and performance before selecting materialisation.

**Default serving object:** use a per-report golden dynamic table. Use a golden view only when the Library owner explicitly directs it or a verified requirement or technical constraint prevents the dynamic-table path; record the exception and evidence.

**Delivery unit and reuse:** build, migrate and, where applicable, cut over each report or app independently after it completes the full path and passes its own parity gate. Each reporting purpose terminates in its own golden dynamic table. Reuse approved dimensions, relationships, facts, and metric definitions already present in the Snowflake Semantic View; extend them only for genuinely new requirements, so effort reduces as semantic coverage grows.

**Interim Qlik source-migration exception:** during the initial SQL Server-to-Snowflake migration, keep the Qlik front end and embedded load-script transformations unchanged except for the source-connection/query changes needed for Snowflake. Perform all changes in a duplicated development app and leave production untouched until promotion. After promotion, do not return the app to SQL Server; use fix-forward throughout the seven-calendar-day hypercare window. Do not introduce facts, dimensions, a Semantic View or a golden dynamic table in this route. Apply the full modelling path later when rebuilding that Qlik app in Sigma.

For this route, validate at an aligned reload cutoff: reconcile rows, keys and agreed metrics, prove a successful reload, and complete sheet-by-sheet front-end regression. A BI Analyst performs the final independent validation before production promotion; customer UAT is optional unless explicitly required.

After BI Analyst approval, publish the validated development app over the production app. Leave the preceding backstage app in the backstage space and add `(Archived)` to its name as historical evidence only; it is not a rollback source.

**Later Qlik-to-Sigma route:** keep the existing production Qlik app live throughout the Sigma build, required validation and seven-calendar-day hypercare. Keep the Sigma replacement recognisably close to Qlik for efficient customer transition, while applying deliberate usability, visual-consistency, professionalism and premium-product improvements that push Sigma's verified capabilities without changing agreed behaviour; broader redesign requires business-owner approval. Discover whether Section Access, row-level restrictions or any other Qlik security rule exists; where present, map it to the governed Snowflake/Sigma control and validate allowed and denied access before promotion. Inventory bookmarks, alerts, subscriptions, scheduled exports and other user-created or downstream dependencies; reproduce each required dependency or obtain explicit business-owner approval to retire it. Treat the Snowflake Semantic View as the canonical metric source: reuse an approved metric already defined there instead of recreating the Qlik expression in Sigma; when a required Qlik metric is absent, build and validate it in the Semantic View before constructing the Sigma output. If a Qlik metric conflicts with an existing Semantic View definition, present the definitions and evidenced result differences to the Qlik app's business owner for a recorded decision. If no business owner is recorded, discuss the conflict within the BI team and try to identify a customer business user who can review the difference; record the agreed forward definition and approver before continuing. Because this route replaces the front end, BI Analyst validation followed by business-owner acceptance is mandatory before production promotion. Before Sigma becomes primary, provide affected users with transition guidance covering changed navigation, controls, workflows and replaced or retired features. At cutover, Sigma becomes the primary report while the existing Qlik app remains available as the temporary fallback throughout seven-calendar-day hypercare. After successful hypercare, disable the Qlik app's reload schedule and archive the app outside customer access. Retain the archived app until the Qlik platform itself is formally decommissioned; do not delete it earlier. Retire Qlik only after the route-specific acceptance and shared decommission gates pass.

**Open architecture decision — metrics model:** the Library owner needs the boss to define what “metrics model alongside the Semantic View” means. The current hypothesis is a separate metric-definition artefact intended partly for AI consumption, but its object type, ownership, canonical authority, and method of linking or synchronising with the Semantic View remain unverified. Until clarified, implement required metrics within the Snowflake Semantic View so delivery continues; do not invent a parallel metric store or relationship.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

> **RESOLVED — 2026-09-20:** phased migration is the default. Each report or app is an independent migration unit and may cut over only after passing its own parity gate; do not wait for an entire route or use an estate-wide single switch.
>
> **RESOLVED — 2026-09-20:** this playbook owns shared parity, cutover, rollback, hypercare and decommission controls. Specialised migration playbooks own only route-specific discovery and build steps and inherit these controls without duplicating them.

## Trigger / entry condition

An old system or pipeline is being replaced by a new one while both could theoretically run — e.g. SQL Server reporting migrating to Snowflake, or a legacy feed being replaced by a trickle feed. Use this playbook once the new system exists and needs to actually take over, not while it's still being designed or built.

Kind: operational state machine (old running → new built → parity → cutover → decommission). This playbook owns the cutover path. It does not design the new pipeline, write first-pass ingestion SQL, or translate Qlik concepts — those stay on the live design/build playbooks.

Wrong door: building the new system from scratch is Project Intake & Scoping and the relevant build playbook, not this one. Do not use when there is no old system of record. Do not use to architect a pipeline (Pipeline Architect) or write the first SQL (Snowflake ingestion knowledge). Do not use for Qlik expression/concept mapping (Sigma Migration playbook) — this playbook is the operational machine for its cutover stages.

## Stages

### Stage 0 — Classify

**Goal:** Name old, new, consumers, and cutover type.

**Action:** Classify as one of:

- **Type A — pipeline replacement.** Old Snowflake/ADF path still feeds consumers; new path is built. Precedent: the D365 trickle feed, where the legacy ingestion path stays live beside the new direct-ingestion path; decommission is a gradual re-point of consuming objects, a separate project from the new-pipeline work.
- **Type B — reporting replacement.** Old report still used; new Sigma workbook/data model is the target. Precedent: SSRS → Sigma first, with Qlik Sense continuing to run loyalty/operational apps until a later phase.
- **Type C — data missing from Snowflake.** SSRS/SQL Server still holds the grain the new report needs. Land FACT/DIM first via a data-source-onboarding path, then return here as Type B. Sigma consumes the per-report golden dynamic table derived from the Snowflake Semantic View under the reporting baseline; a golden-view exception requires its stated evidence/authority. It does not connect directly to RAW, STG, or INGESTED.

Inventory every consumer: stored procs, tasks, dynamic tables, Qlik load scripts, SSRS RDLs, Sigma workbooks, grants. For every layer and task, identify the required system, execution identity, role, developer and intended user access; verify it before the dependent work begins. Confirm old is still the live source of record.

**Exit:** One-paragraph statement: old object, new object, consumer list, type A/B/C, proposed strategy. the Library owner confirms before Stage 1.

### Stage 1 — Old running, freeze scope

**Goal:** Old stays live. No silent rewrite of business logic on the old path.

**Action:** Do not switch old off. Record freshness/SLA, owners, access, and the comparison baseline. Type A: old is the UAT/parity baseline. Type B: freeze old-side development; spend goes to the Sigma replacement.

**Exit:** Old confirmed running; old-path change-freeze except incident fixes; consumer inventory complete.

### Stage 2 — New built

**Goal:** Replacement exists and can be queried; it is not yet the source of record.

**Action:** If design is missing → Pipeline Architect, then return. If Snowflake objects are missing → use PLAY-0025 and its SKILL-0002 source-mechanism architecture: distinguish optional acquisition/orchestration, the governed Snowflake landing/ingestion route, and justified consumer modelling. Implement only layers with verified responsibilities; a controlled INGESTED endpoint can be sufficient for ingestion. Preserve source authority, grain, checkpoints, idempotency, deletes, late updates, lineage, recovery, reconciliation and governed consumer boundaries. Apply this playbook's reporting migration architecture baseline, including its source-only Qlik exception, when reporting is in scope. If Sigma content is missing → Dashboard Ideation then Sigma Computing build. If source data is missing → the data-source onboarding path, then return here. Apply the required schema-level privileges to both ALL existing and FUTURE objects for each applicable Snowflake object type, including tables, views and dynamic tables. Before creation or replacement, determine the required owner from verified current ownership rules and comparable existing objects in the same governed area; set and verify that ownership after the operation, stopping on conflicting or absent evidence. Verify effective grants after every object replacement. Use narrower object grants or row-level restrictions only for an explicit purpose and record the exception. Do not declare the build ready while any required system, service identity, developer or user access is missing or unverified.

**Exit:** New objects exist; schedule may be on; consumers still point at old.

### Stage 3 — Parity (parallel run)

**Goal:** Prove new matches old on named checks before any consumer moves.

**Action:** Run old and new together. Route this comparison through Testing & Validation (PLAY-0019) — parity is exactly the kind of evidence that playbook exists to gate. Discrepancies are investigated to root cause, not waved through as "close enough." Compare at grain: row counts, key uniqueness, agreed business metrics, freshness timestamps advancing, task/graph health. Name known non-blocking exceptions; do not fail the pack on them and do not "fix" them into a false pass. For every reporting route, prove equivalent agreed metrics, filter and selection behaviour, access controls, refresh freshness, and acceptable performance using representative scenarios. Front-end layout and interaction may be intentionally redesigned rather than copied, provided users can still complete every required business task. Dual-run cost is real (measured D365 example: new path materially cheaper per day than legacy, but combined spend while both run is a separate concern) — do not let parallel run become permanent by neglect. Generic pipeline observability is not implemented in the old Library — use explicit comparison queries; do not pretend a generic DQ framework is live.

**Exit:** Written parity pack (pass/fail per check + named exceptions). the Library owner signs that new may receive consumers.

### Stage 4 — Cutover (re-point)

**Goal:** Consumers read new. Old remains available for rollback.

**Action:** Use phased cutover: each report or app moves independently after its own parity approval, never as an estate-wide big-bang switch. Within that migration unit, choose a hard switch or a justified parallel period based on risk and recovery needs; do not impose an unverified universal duration. The source-only Qlik route is explicitly fix-forward after promotion and must not return to SQL Server. Do not drop old objects in this stage. Verify each moved consumer against new. Document the applicable recovery: source-only Qlik remains fix-forward with no return to SQL Server; other routes may re-point to old only under their approved recovery authority.

**Exit:** Moved-consumer list verified on new; remaining-on-old list explicit; applicable recovery path written, including the source-only Qlik fix-forward restriction.

### Stage 5 — Hypercare

**Goal:** Catch silent wrong or stale data after re-point.

**Action:** Run hypercare for seven calendar days from cutover. Watch task success, dynamic-table lag/timestamps advancing, row-count deltas, user-reported metric breaks, and required business-task completion. Resolve and retest every material defect found during the window; unresolved material defects block exit. D365 invariants: ERROR is terminal (no silent recycle); replay never moves checkpoints backward; do not overwrite newer STAGED state. If a silent fact-table failure is suspected, hand off to incident/observability-response — do not debug inside this playbook.

**Exit:** Seven calendar days elapsed and no material defect remains unresolved or unverified on moved consumers.

### Stage 6 — Decommission old

**Goal:** Old no longer runs. Dual-run cost and dual-truth stop.

**Action:** Search again for remaining consumers (procs, tasks, Qlik scripts, SSRS, Sigma connections, grants). Zero remaining → suspend old tasks/graphs before drop. Technical validation PASS is not permission to drop legacy if a separate change-control gate is still pending. Archive the old runbook via Data Documentation. Update the Project entry.

**Exit:** Old tasks suspended; objects dropped or explicitly retained read-only; Project entry records cutover + decommission dates; dual-run credits gone.

## Branches

| Condition | Path |
|---|---|
| No old system of record | Leave this playbook → data-source onboarding |
| Design/SQL/Sigma content missing at Stage 2 | Loop to the matching build playbook, then resume Stage 2 |
| Unexplained parity fail | Loop to Stage 2 (fix new) or Stage 0 (wrong grain/consumer). Never cut over anyway |
| Type C (data not in Snowflake) | Onboard to FACT/DIM, then resume as Type B |
| Qlik concept/expression work | Sigma Migration playbook; return here for Stage 3–6 |
| SSRS→Sigma vs later Qlik→Sigma | Same machine; different inventory and Phase 1 constraint (SSRS first) |
| Qlik metric conflicts with the Semantic View | Escalate evidenced differences to the business owner; if none is recorded, agree internally and seek an identifiable customer business user before recording the selected definition |
| Consumer cannot move (access, contract, dependency) | Leave it on old; do not decommission; record residual list |
| Incident during hypercare | Incident/observability-response; source-only Qlik fixes forward; other routes use their approved recovery path |

## Loop-backs

- Parity fail → Stage 2 or Stage 0.
- New consumer discovered mid-cutover → Stage 0 inventory, then Stage 4 for that consumer only.
- Approved rollback on a route permitting it → Stage 1 (old is source of record again); do not delete new. Source-only Qlik failures retain Snowflake and follow fix-forward.
- Unresolved source mechanism, layer responsibility or universal control objective → stop the affected build and resolve it under PLAY-0025/SKILL-0002; do not invent architecture. For reporting, also satisfy the reporting migration architecture baseline and its route-specific exceptions.
- If the cutover breaks something the earlier stages didn't anticipate, this playbook hands off immediately to Disaster Recovery & Rollback (PLAY-0029) rather than continuing forward.

## Overall Exit

All inventoried consumers on new (or an explicit residual-on-old list with an owner); parity pack retained; old decommissioned or justified; Project entry has cutover date; dual-run stopped except residuals.

## Anti-Patterns

| Anti-pattern | Instead |
|---|---|
| Switch old off before the last consumer moves | Phased re-point; old stays until residual list is empty |
| Treat "technical validation PASS" as decommission | Separate decommission stage |
| Lift-and-shift old layout into the new tool | Reporting cutover may redesign (Dashboard Ideation); this playbook still owns parity + re-point |
| Point Sigma at RAW/STG/INGESTED or SQL Server | Semantic View-derived per-report golden dynamic table; evidenced golden-view exception only |
| Invent an ingestion route or ceremonial layers | Verify the source mechanism and necessary layer responsibilities under PLAY-0025/SKILL-0002; preserve universal controls, then apply the reporting baseline where applicable |
| Fail parity on named known anomalies | Record them; don't pretend they are new defects |
| Assume generic DQ/observability is live | It is not; write explicit checks |
| Big-bang drop of the legacy path | One consumer at a time |

## Hand-offs

- PLAY-0063 — source-only Qlik SQL Server-to-Snowflake discovery, query conversion, validation, promotion and fix-forward hypercare.
- PLAY-0064 — SSRS-to-Sigma discovery, Snowflake modelling, Sigma build, sequential acceptance and retirement.
- PLAY-0065 — Qlik-to-Sigma discovery, semantic migration, premium Sigma build, acceptance, hypercare and archival.
- the owner-approved conversion standard — SQL Server to Snowflake conversion pattern, for this specific migration type.
- PLAY-0019 — Testing & Validation, for the parity-check evidence bar.
- PLAY-0029 — Disaster Recovery & Rollback, if cutover breaks something unanticipated.
- Pipeline Architect — design before Stage 2 SQL.
- Snowflake ingestion build knowledge — 5-layer build; rebuild pattern; grants.
- Sigma Migration (PLAY-0014) — Qlik→Sigma concept/expression mapping and app inventory; this playbook owns the shared operational migration controls after the route-specific build work.
- Sigma Computing + Dashboard Ideation — build/rebuild of workbooks/data models.
- Data Documentation — parity pack, cutover runbook, decommission notes.
- Data-source onboarding path — Type C data-layer first.
- Incident/observability-response — hypercare failures.
- People: the Library owner signs Stages 0, 3, and 6.

</details>

## Guardrail correction — 2026-10-13

Architect, Data & BI Lead and Reliability: generic serving and recovery branches now preserve the canonical golden-object path and the source-only Qlik fix-forward exception.



## Addy Osmani reference-method extension — 2026-11-01

Within the existing migration unit, distinguish advisory deprecation from an authorised mandatory removal date; record the replacement, reason, affected consumers and transition support without treating a notice as consumer migration. Consumer-exit evidence combines the dependency inventory, verified migrated behaviour and current usage evidence; retain explicit residual consumers and approved retention obligations. No observed traffic alone proves that every scheduled or infrequent consumer has exited.

For an applicable schema transition, reason in separate expand, migrate and contract phases: additive compatible shape; controlled backfill and, where needed, consistent dual writes; verified read cutover; then later cleanup only after compatibility and consumer-exit evidence support it. Assess locking, reconciliation and recoverability for the actual platform rather than assuming additive changes are harmless or destructive changes reversible. Existing route-specific fix-forward, fallback, hypercare and archival requirements remain controlling. Contract/cleanup is not implied by successful migration and retains its separate applicable authority.

Source adaptation: Reference/addyosmani-agent-skills-8bfcc1f/skills/deprecation-and-migration/SKILL.md. Pinned revision: `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Paraphrased reference techniques within this existing owner; the Library contract and current task authority govern use. No upstream workflow, trigger, link relationship, installer, agent configuration or operational authority is imported.

## Contextual links

- `SKILL-0324` — `shared_method` — Compare net-new application rollout readiness when no live predecessor or consumer cutover exists; migration controls stay with this Playbook.
