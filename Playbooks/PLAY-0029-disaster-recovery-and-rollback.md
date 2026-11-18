---
id: PLAY-0029
type: playbook
title: Disaster Recovery & Rollback — Freeze, Assess, Recover
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0004, PLAY-0019, PLAY-0020, PLAY-0022, PLAY-0031, PLAY-0032, PLAY-0055, PLAY-0056, PLAY-0059]
tags: [playbook, disaster-recovery, rollback, deploy-failure, freeze]
migrated_from: PLAY-0029-old-library
---
# Disaster Recovery & Rollback — Freeze, Assess, Recover

## Trigger

the Library owner reports active or potentially worsening damage and requests investigation, recovery planning or rollback support.

## Method

Name the system and affected consumers. Search the relevant Library Ticket, Project, Knowledge, architecture, scripts and prior incidents before forming a conclusion. Return up to three possible causes ranked by evidence-based confidence percentage, state missing evidence, and produce the shortest diagnostic plan likely to isolate the cause. Recommend the safest containment, forward-fix or rollback action for the Library owner or the authorised operator to execute. Record execution only after confirmation, then verify results from supplied or accessible evidence. Preserve system-specific recovery constraints.

## Stop

Recovery verified or precise blocker. Never mix Library and pipeline rollback, rewind D365 checkpoints, overwrite newer state or bypass protected main.

AGENTS.md owns shared authority, evidence reuse and task boundaries. The AI has no implied operational access to Snowflake, ADF, OpenFlow, Qlik, Sigma or other the organisation’s systems: system actions are recommendations until the Library owner or an authorised operator confirms execution.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

## Two tracks, never mixed

- **Track F** — the organisation’s BI (Snowflake / ADF / OpenFlow / D365).
- **Track G** — GitHub Library automation, workflows, generated views, relationships, or governance.

These must never be run as one blob of steps. Stage 0 names the track before anything else happens.

Trading is out of scope. Stop if that is the domain. (See the `[NEEDS the Library owner]` section at the foot.)

## Nest under Mission Control

Layer, not a new front door.

- Mission Control still routes. This playbook never self-triggers around it.
- Enter when a change is already in the live system and continuing is unsafe.
- After restore, remaining RCA/consumer work returns to incident or observability playbooks. This playbook does not own long RCA.

Precedence: AGENTS.md and the current GitHub Library controls govern Track G. Source recovery happens on `staging`; `main` is protected and read-only to AI; generated views remain workflow-owned; PLAY-0059, PLAY-0056 and PLAY-0055 follow AGENTS.md's distinct current-conversation or explicitly approved enabled schedule authority; an unscheduled PLAY-0056 run requires its named single-use one-off exception, and source recovery grants none of those runs. D365 knowledge wins on rollback invariants (no checkpoint rewind). ADF knowledge wins on ADF (no Live-mode prod edit; Git/PR). This playbook wins only on freeze → assess → rollback-or-forward-fix → verify → document.

## Trigger / entry condition

A deploy, script change, or cutover has gone wrong in a way that's actively causing harm — corrupted data, a broken automation loop, a duplicated or lost record. Use this when something is already broken and getting worse, not for routine incident triage — that's Incident Response (PLAY-0020) for failures that aren't actively compounding.

Enter when a repository change is merged or partially applied and automation, generated views, relationships, policy enforcement, or release controls are unsafe.

Do not enter when: failure with no recent change (incident playbook); silent data issue with no deploy (observability playbook); a change exists only on `staging` and has not merged to `main` (do not freeze `main`; stop validation or merge and repair the candidate instead); trading system.

Wrong door: a pipeline that failed cleanly and can simply be rerun is Incident Response, not this playbook. This is for active, worsening damage.

## Stages

The spine is freeze → assess → rollback-or-forward-fix → verify → document, gated at the front by the track choice and closed at the back by an explicit unfreeze.

### Stage 0 — Track gate

**Goal:** Pick Track F or Track G. Never run both as one blob of steps.

**Action:** For Track G, freeze further affected mutation; capture branch, commit, workflow and check evidence; repair or revert through `staging` or a temporary reconciliation branch whose only destination is `staging`; rebuild derived outputs through their owning workflow; run authorised checks; verify the recovered branch and, only after an explicitly authorised merge, `main`. For Track F, inspect relevant Library evidence and prepare recommendations; the Library owner or an authorised operator performs system actions and returns the evidence. External the organisation’s systems use Track F; trading is out of scope.

**Exit:** Track named. Opposite track's prod is not touched.

### Stage 1 — Freeze

**Goal:** Stop further damage. No new deploys. No "just one more fix" paste. Do not attempt a fix while the process is still running and making things worse.

**Action Track G:** Stop further writes that overlap the affected Library surface and stop any pending validation or merge. Preserve the exact `staging` and `main` heads, failing workflow/check evidence, ID reservations and receipts. Do not write to `main`, hand-edit generated views, delete evidence or run PLAY-0059/PLAY-0056/PLAY-0055 without the required explicit authority.

**Action Track F:** Recommend the smallest containment needed: suspend the affected Snowflake task graph (D365: suspend before any ALTER); disable the ADF trigger publishing the bad pipeline without editing Live mode; stop the affected OpenFlow processor group without dropping flow files; or pause downstream reloads consuming wrong objects. Never claim any action occurred until the Library owner or an authorised operator confirms it. Never recommend rewinding watermarks or D365 checkpoints.

**Exit:** No further live changes. Freeze inventory listed (what was paused) — this list is what Stage 5 lifts, item by item.

### Stage 2 — Assess rollback vs forward-fix

**Goal:** One decision, evidenced. Not both. Understand the actual scope and cause before touching anything further.

**Action:** First search the relevant Library Ticket, Project, Knowledge, architecture, scripts, procedures, tasks and comparable prior incidents. Write an assessment card containing: change identity; blast radius; known-good restore point; data already written; evidence found; the three most likely hypotheses (or fewer when fewer are credible), each with an evidence-based confidence percentage, supporting evidence, contradicting evidence, fastest confirmation or rejection check, and proposed fix; plus missing evidence. If the bad change mutated rows, state that code rollback is not data rollback. Prefer a precise likely solution when evidence supports it; otherwise give a brief ordered diagnostic plan designed to eliminate the most likely causes quickly.

**Hypothesis confidence rule:** Percentages express investigative confidence, not statistical certainty, and do not need to total 100%. Base them only on current evidence and comparable Library history. At **95% or above**, lead with the precise evidence-backed solution and its verification check. Still show other credible recovery options when useful, but label them as alternatives with their evidence, trade-offs and confidence; do not present them as equivalent conclusions or let exploration displace the recommended solution. Below **95%**, do not present a cause as established: provide the ranked top three and run or request the quickest discriminating checks. If evidence cannot support three credible causes, return fewer rather than inventing possibilities.

**Required hypothesis format:** Rank | possible cause | confidence % | supporting evidence | contradicting/missing evidence | quickest check | proposed fix.

System-specific recovery limits take precedence: the initial Qlik SQL Server-to-Snowflake source migration is fix-forward after promotion, never a return to SQL Server, and its archived backstage app is historical evidence rather than a rollback source. Preserve required BI Analyst validation and seven-calendar-day hypercare.

Decision rule: ROLLBACK only when the route permits it, known-good exists and forward-fix would be larger or unreviewed. FORWARD-FIX if no restore point, or the bad change is a one-line revert that is itself the fix, or data mutation requires a compensating MERGE rather than code restore. STOP-FOR-the Library owner if a required restore point is unknown and no safe authorised forward-fix is evidenced, or if data compensation is destructive.

**Exit:** ROLLBACK | FORWARD-FIX | STOP-FOR-the Library owner. No execute before this exit.

### Stage 3 — Execute

**Goal:** Apply the Stage 2 decision only.

**Track G — ROLLBACK:** restore the affected source on `staging` from a verified Git commit or Library version, preserving unrelated concurrent work. Use a temporary reconciliation branch only when needed, and target it solely back to `staging`. Do not direct-push, edit or revert `main`. Rebuild generated outputs through their owning workflow; never hand-edit them.

**Track G — FORWARD-FIX:** apply the smallest evidenced correction to `staging`, preserving unrelated work and expected-version guards. Reconstruct state from verified repository facts, never memory. If ID allocation may have fired, stop new-ID work until receipts are reconciled; reserved IDs are never reused. Source repair does not authorise PLAY-0059, PLAY-0056 or PLAY-0055.

**Track F — ROLLBACK recommendation:** Provide the exact operator runbook and validation evidence required. ADF: revert via Git/PR to last good; publish from collaboration, not Live. Snowflake: restore prior proc/task text; sequence remains suspended → alter → re-enable → verify next run. Data: if bad rows landed, use a separate, idempotent compensating MERGE/replay; never DROP+reload by default. D365: never move a checkpoint backward—use replay plus the metadata-recovery scan. the Library owner or an authorised operator executes and confirms each system action.

**Track F — FORWARD-FIX recommendation:** Specify the smallest evidenced change, exact execution order, expected result and verification query/check. ADF remains Git-based; D365 graphs remain suspend → alter → enable. the Library owner or an authorised operator executes it. If the change is not reversible, STOP-FOR-the Library owner instead of improvising.

**Exit:** Track G decision applied on `staging`, or Track F recommendation issued and operator confirmation/evidence received; otherwise blocked on evidence or authority. Any confirmed freeze remains until Stage 4 passes; `main` remains unchanged unless the Library owner separately authorises merge.

### Stage 4 — Verify

**Goal:** Prove the live system matches the restore intent. Tool-call success is not enough. Verified, not assumed complete.

**Action — Track G checks (read back, do not hand-edit):** repaired source content and reciprocal relationships; reserved-ID continuity; required schema/integrity checks for the affected surface; generated outputs rebuilt only by their owning workflow; failing evidence retained and triaged. Run PLAY-0059 only when the Library owner requests commit-ready, PLAY-0056 only when he authorises the commit playbook, and PLAY-0055 only when he explicitly authorises merge. Route the recovered state through Testing & Validation (PLAY-0019).

**Action — Track F checks:** task state + next scheduled run; object definitions match intended restore; row counts for the change window, no duplicate grain from a panicked full rebuild; consumers named in the freeze inventory; D365 registry health (no unexpected ERROR/stuck IN_PROGRESS).

**Exit:** Evidence on the TICK/CHAT. Freeze lifted only after this exit. Fail → Stage 2 (re-assess; do not double-forward-fix).

### Stage 5 — Document and unfreeze

**Goal:** The next deploy cannot claim it was the first time. Leave a clear incident record so the same failure is recognisable next time.

**Action:** Track G: record the repaired `staging` state, restore point, validation status, generated-output status and whether merge remains unauthorised, authorised or verified. A successful staging repair is not a `main` recovery claim. Track F: update the relevant architecture Knowledge/Project only if a constraint changed. File monitoring gap to the observability project if the bad deploy was undetected. Lift freeze as an explicit step, not a side effect — walk the Stage 1 freeze inventory item by item. If a marker was BLOCKED, follow the recovery rules: preserve receipts, completed/pending writes, exact next action; never claim completion. If the root cause isn't fully resolved, say so explicitly rather than closing the ticket prematurely.

**Exit:** Freeze lifted; proof recorded; the Library owner PASS/FAIL recorded for Track G; any unresolved root cause stated.

## Decision gates

| Gate | After | If | Then |
|---|---|---|---|
| Staging only | Trigger | Candidate changed but has not merged to `main` | Do not freeze `main`; stop validation/merge and repair `staging` |
| Track mix | Stage 0 | Trading | Stop |
| Restore unknown | Stage 2 | No known-good | Block rollback; never guess a version. Use only an evidenced authorised forward-fix, or STOP-FOR-the Library owner if no safe permitted path exists |
| Data mutated | Stage 2 | Rows already written | Code rollback ≠ data rollback; plan compensating MERGE/replay |
| Generated files look wrong | Stage 1/3 Track G | Urge to edit them by hand | Refuse; repair source and run the owning generator under authority |
| D365 rewind offered | Stage 3 Track F | Checkpoint backward | Refuse; replay |
| Verify fail | Stage 4 | Still unsafe | Re-assess Stage 2; keep freeze |
| Merge not authorised | Stage 3/4 Track G | `staging` repair passes | Stop at the staged result; do not change `main` |
| Root cause not understood | Stage 5 | Cause still open | Still freeze and recover, but keep the Ticket active/blocked rather than done |
| Rollback and forward-fix both viable | Stage 2 | Either would work | Prefer whichever loses less verified work, and state the reasoning |

## Loop-backs

| Signal | From → To | Rule |
|---|---|---|
| Verify fail | Stage 4 → Stage 2 | New assessment card; do not stack fixes |
| Forward-fix creates a worse live state | Stage 3 → Stage 1 | Re-freeze; prefer ROLLBACK if restore point now clearer |
| After restore, data still wrong | Stage 5 → Observability Stage 1 | DR done; silent-data path owns the rest |
| After restore, jobs still failing | Stage 5 → Incident Stage 4 | DR done; incident owns remaining failure |
| Marker BLOCKED remains | Stage 5 → recovery rules | Do not delete the marker to close DR |
| Same gap loops twice | Any | Escalate to the Library owner; stop cycling |

## Overall exit

Done when all of: freeze inventory is cleared or each remaining pause has owner + review date; live code/config matches the Stage 2 decision (read back); Track G: `staging` repair and applicable checks are evidenced; `main` is either unchanged and explicitly pending, or an authorised merge has been verified; Track F: task/pipeline next-run verified, compensating data action evidenced or explicitly N/A; consumers named in freeze are safe or still paused on purpose; record updated; no generated Library file was hand-edited as a fix.

"Pasted something" is not an exit. "Trigger is running" is not an exit.

## Hand-offs

| Target | What moves |
|---|---|
| AGENTS.md / PLAY-0059 / PLAY-0056 / PLAY-0055 | protected `main`, staging repair, generated-file ownership, validation, commit and explicit merge authority |
| Library-mutation recovery rules | Markers, receipts, no ID reuse |
| D365 / ADF / OpenFlow knowledge | the organisation’s restore invariants |
| PLAY-0019 — Testing & Validation | Confirming the recovery |
| PLAY-0022 — Migration & Cutover | If the disaster occurred mid-cutover |
| PLAY-0031 — Security & Access | If the root cause was an auth/credential failure |
| Incident playbook (PLAY-0020) | Remaining hard failures after restore |
| Observability playbook (PLAY-0032) | Remaining silent-data after restore |
| Observability project | "We did not detect the bad deploy" |
| Never | Trading Knowledge — trading is out of scope |

Does not mint or reuse IDs. Does not write to `main` or infer commit/merge authority.

## [NEEDS the Library owner]

These block the critical path. A Track G rollback cannot complete as written until the restore point itself is defined.

- Trading DR playbook not yet drafted.
- Whether any ID was allocated by the bad run.

</details>
