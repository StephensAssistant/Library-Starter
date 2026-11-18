---
id: PLAY-0031
type: playbook
title: Security & Access — Live Auth, Rotation and Permission Review
status: current
created: 2026-08-17
updated: 2026-09-20
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0004, PLAY-0019, PLAY-0020, PLAY-0029, PLAY-0038]
tags: [playbook, security, access, oauth, credential-rotation]
migrated_from: PLAY-0031-old-library
---
# Security & Access — Live Auth, Rotation and Permission Review

## Trigger

A live authentication failure, credential rotation, suspected credential exposure or permission/access review is in scope.

## Method

Identify the exact credential, identity, grant or ownership failure using current evidence. Recommend the smallest least-privilege operational correction, preserving environment separation and recovery; the Library owner or an authorised operator executes system changes. Record execution only after confirmation, verify with a real access or ingestion call, and store evidence—never secret values. Route new or materially changed security architecture to [[PLAY-0038]].

## Stop

Required access/control works or precise blocker. Historical OAuth/service incidents are diagnostic references, not assumptions. No whole-estate audit.

AGENTS.md owns shared authority, evidence reuse and task boundaries. This playbook does not imply AI access to operational systems or permission to change credentials, grants, ownership, OAuth configuration or runtime services.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

> ⚠ **FLAGGED — invented cadence in the old Library, corrected there, not resolved further here**
>
> The first filed version invented a rotation schedule. the Library owner has now confirmed that permission reviews are event-driven only, not calendar-driven. Trigger them for joiners/leavers, role or responsibility changes, new or materially changed integrations, suspected exposure, security incidents, ownership/grant drift, or the Library owner's request. Credential rotation follows an evidenced expiry, compromise, platform requirement or explicit instruction; do not invent a general cadence.

## Trigger / entry condition

An integration or connector's authentication breaks (an invalid_grant error, an expired token, a blocked sign-in), or an authorised credential rotation or permission review is requested or triggered. Grounded directly in a real incident: a static plaintext refresh token combined with an OAuth consent screen stuck in "Testing" status caused silent 7-day token expiry.

Enter this playbook when any of the following is true: auth-break (invalid_grant, connector/tool auth failure, 401/403 on a connected service, reconnect did nothing); credential rotation (planned, post-incident, new OAuth client, or suspected leaked/expired token); permission review (the Library owner asks; joiner/leaver/role or responsibility change; new or materially changed schema/service/integration; suspected exposure or security incident; ownership/grant-drift alert—event-driven only); promoting a dev integration to prod (secrets are not cloneable).

Wrong door: a one-off permission request for a new person is an ordinary access request, not this playbook. Also wrong door: a pre-Build security design question (new attack surface, new integration, access-control design) — that's the Security Design Review playbook (PLAY-0038). This playbook is for something already live: an auth break, a rotation, or a permission review.

## Incident this playbook is built from

Do not generalise beyond what the source Knowledge entry records.

**Symptom:** connector MCP tools failed with invalid_grant on every call. Reconnecting the chat client's own session did not fix it — that only re-authenticates the client's session with the connector endpoint, a different credential from the backend service's refresh token.

**Root cause:** (1) the OAuth consent screen for the GCP project was in Testing; Google auto-expires Testing refresh tokens after 7 days. (2) the connector service stores the Google credential as a static plaintext refresh-token environment variable (with client ID, client secret, API key), set at deploy, never rotated. HTTP between the client and the connector stayed 200/202; the error was inside the response body — `invalid_grant` does not appear in the service's request logs.

**Fix (verified):** publish the OAuth app to production; mint a new refresh token via the OAuth flow using the service's own client credentials; replace only the refresh-token variable on a new service revision; confirm the revision is serving 100 percent traffic; re-test with a direct tool call. Publishing status "In production" as of the fix date — this 7-day expiry should not recur for this app.

**Prevention recorded:** publish any new OAuth client/service to production before first real use.

## Classify the credential before acting

Evidenced classes: (A) the chat client's own connector session; (B) the backend service's refresh token and sibling env vars (client ID/secret, API key); (C) the GCP OAuth client publishing status (Testing vs In production); (D) Snowflake secrets/external access for a dev-store integration, not for the production store; (E) Snowflake role grants; (F) other the organisation’s/personal credentials — `[NEEDS the Library owner]` inventory, do not invent a list.

## Stages

### Stage 1 — Diagnose: classify the break or the review

**Goal:** Find the real cause, not just the symptom of "it stopped working." Touch the failing layer only. Do not rotate everything.

**Action:** If tools fail, capture the exact error string and which tool/service. Search the relevant Library Ticket, Project, Knowledge, configuration history and comparable incidents before diagnosing. Do not spend time searching backend logs for `invalid_grant` — request logs carry HTTP metadata only. Check the specific error against known patterns first — an `invalid_grant` on a Google OAuth integration matches the Testing-mode 7-day expiry pattern before assuming a different cause. Decide class A–F. Reconnecting the client (A) does not fix B, and fixing B does not refresh A. If OAuth-related, check publishing status before assuming the last token mint failed. If this is an event-triggered permission review with no incident, skip to Stage 5 using the inventory the Library owner provides. If an evidenced credential expiry or explicit rotation instruction triggered the work, use Stages 3–4.

When the cause is not already proven, return the three most likely causes—or fewer when fewer are credible—in this format: Rank | possible cause | confidence % | supporting evidence | contradicting/missing evidence | quickest confirmation or rejection check | proposed fix. Confidence expresses investigative confidence, not statistical probability, and scores need not total 100%. Rank downward from the strongest available evidence; never invent causes to fill three rows. Test or request the quickest discriminating check first, then rescore. At 95% or above, lead with the precise evidence-backed fix and verification check while retaining credible alternatives as labelled options.

**Exit:** The cause is confirmed by evidence or the ranked hypotheses and next discriminating check are recorded; it is never assumed from the symptom alone. Class named; incident vs rotation vs review named. Unknown class: `[NEEDS the Library owner]`, do not guess.

### Stage 2 — Auth-break containment / fix the immediate break

**Goal:** Restore access. Stop treating a 200/inner-error as healthy; stop applying the wrong fix.

**Action:** For the connector's `invalid_grant`: follow the known-good order — publishing status, then token mint, then service env replace, then live tool call. Do not start with a client-side reconnect. For the Testing-mode expiry pattern: publish the OAuth app to production status and generate a new refresh token via the appropriate flow, using the app's own client credentials. Leave other client secrets/API keys untouched unless those are the failing secrets. Do not paste live tokens into Library entries, Chat volumes, or PATCH files. Record that rotation happened, where the secret lives, and the verification check — not the secret value. An IT service-desk ticket is not a substitute for the actual OAuth/service rotation. For other causes, apply the fix matching the diagnosed cause from Stage 1 — never guess a fix for an undiagnosed cause.

**Exit:** Access is restored and confirmed working with a real request, not just a successful-looking config change. Wrong-layer fixes ruled out; containment notes recorded without secret material.

### Stage 3 — Credential rotation (when class B/C/D or planned rotation)

**Goal:** New secret is in the running system and proven with a live call.

**Action (connector case, verified pattern):** publish the OAuth app if still Testing; use the service's own client ID and secret in the OAuth flow's own-credentials mode, adding the flow's redirect URI to the client's authorized redirect URIs or auth fails with a redirect mismatch; authorize, accept an unverified-app warning if shown, exchange the code, copy the full refresh token (the UI may truncate it on screen); deploy a new service revision with only the refresh-token variable replaced; confirm the new revision is serving 100 percent traffic; re-test with a direct tool call. An automatic revoke banner tied to the flow's own default client does not apply when using the service's own client — do not rotate again solely because of that banner.

**Action (Snowflake/dev-integration secrets):** credentials are environment-specific and must not be copied to production; secrets are not among object types supported by clone operations. If production access requires a new application, identity, secret or external-access design, stop and route that design to [[PLAY-0038]]. After an authorised rotation, prove with a live ingestion/auth call, not clone success.

New OAuth-client readiness is a pre-build design control owned by [[PLAY-0038]]; this playbook checks publishing status only while diagnosing or repairing a live integration.

**Exit:** Live proof recorded (tool/query succeeded after revision/secret change). No token values stored in the Library. If proof fails, loop to Stage 1; do not claim rotation done.

### Stage 4 — Rotation hygiene (address the structural cause)

**Goal:** The expiry mode cannot silently return.

**Action:** Confirm publishing status "In production" for the affected OAuth app. If a new connector/service was created in Testing, publish it now — do not wait for the next 7-day failure. Static env-var tokens have no in-app rotation clock. `[NEEDS the Library owner]` whether a reminder/review date should exist, and where. Update the canonical incident Knowledge entry in place if the procedure or publishing status changed; do not create a second incident doc. Do not expand one incident into a whole-estate review.

**Exit:** Publishing status confirmed; hygiene gap flagged or scheduled. Canonical incident Knowledge current. The structural cause is fixed or explicitly accepted as a known limitation with a stated reason.

### Stage 5 — Permission review

**Goal:** Grants and ownership match the intended role; silent non-monitoring is treated as a defect.

**Action (evidenced Snowflake facts only):** ownership transfer does not cascade — transferring a database leaves existing schemas on the old role, each schema needs its own transfer by the current owner; a schema with no ownership-expectations row is not monitored by the daily drift check and fails silent rather than flagging — a missing row is a review FAIL, not "no issues"; future grants on schemas are part of a specific setup script, do not assume they exist on unrelated databases; a named integration user's grants (usage + select on a specific ingested schema) should not be expanded to other roles without evidence; do not change Library sharing as a fix for connector auth (wrong layer) — `[NEEDS the Library owner]` who may be a writer on The Library besides the Library owner; the organisation’s joiner/leaver and platform access reviews are event-driven; the current system or service owner and system of record must be identified from evidence for each review.

**Exit:** Each in-scope surface reviewed with named objects and outcomes. Unscoped surfaces listed as `[NEEDS the Library owner]`, not marked clean.

### Stage 5A — Incremental credential inventory

**Goal:** Build reliable operational coverage from real work without launching or implying a whole-estate audit.

**Action:** For each incident, rotation or permission review, add verified metadata to the relevant system's canonical Knowledge, Project or access record: system; credential or identity class; authorised owner; approved storage location by name only; environment; evidenced expiry or rotation trigger; permission scope; recovery/escalation route; last verified date; and source evidence. Never store a credential, token, secret value or unsupported assumption. The union of these verified system records is the inventory; unreviewed systems remain unknown, not clean.

**Exit:** In-scope verified metadata is preserved or its precise gap is recorded.

### Stage 6 — Evidence close

**Goal:** Same gate as testing/validation — no terminal claim without inspected proof.

**Action:** Record: class, action taken (no secrets), live verification, publishing status, grant/ownership checks. Read back any Knowledge/Ticket update. When the Library owner lacks authority, identify the authorised owner from evidence and prepare a Freshservice note containing the blocker, required action, evidence, owner and waiting status for the Library owner to review and post. Record it as posted only after the Library owner confirms it. Missing authority or required sign-off means blocked, not done.

**Exit:** Evidence recorded; canonical entries updated in place; or explicit waiting-on.

## Decision gates / branches

- Error is `invalid_grant` on the connector: do not treat a client reconnect as the fix; do not hunt backend logs.
- OAuth still Testing: publish before or as part of minting a durable token; otherwise 7-day expiry will recur.
- Dev-integration secret: never clone/copy to production.
- Unknown credential class or human-access process: `[NEEDS the Library owner]`.
- Diagnosed cause doesn't match a known pattern → stop and investigate properly rather than applying the Testing-mode fix on the assumption it's the same issue.
- Fix requires authority the Library owner does not hold → identify the authorised system owner or administrator from current evidence, prepare a Freshservice note stating the blocker, required action, evidence, named owner and waiting status for the Library owner to review and post, then hand off without attempting a workaround. Never guess the owner; if unresolved, ask Service Desk to identify or route to the accountable owner and record that ownership gap.
- Live tool/query still failing after rotation: not done; reclassify (Stage 1). Check publishing status before assuming the mint failed.

## Loop-back rules

If Stage 2's fix doesn't actually restore access, return to Stage 1 — the diagnosis was wrong, don't keep trying variations of the same fix.

- Reconnect appeared to work but tools still `invalid_grant`: Stage 1, class B/C.
- New revision not at 100 percent traffic: Stage 3 deploy confirmation, then re-test.
- Redirect-URI mismatch: add the flow's redirect URI, then remint (Stage 3).
- Ownership drift silent: add the missing ownership-expectations row, then re-run Stage 5.
- Permission review finds excess grant: revoke with evidence; `[NEEDS the Library owner]` whether a Ticket is required to track it.

## Overall exit condition

Done only when the entered path is complete: auth-break (failing class identified; correct layer rotated or re-authed; live tool/query proof; publishing status not left in Testing for a real-use client; canonical incident Knowledge updated only if facts changed; no secrets in Library text); rotation (new secret in the running revision/system; live proof; old expiry mode addressed); permission review (every in-scope object checked; silent-unmonitored schemas treated as fail; out-of-scope items explicitly `[NEEDS the Library owner]`, not passed).

A successful deploy or client reconnect without a live tool proof is not exit.

## Hand-offs

- Canonical incident Knowledge — the connector rotation procedure and the specific OAuth Testing-mode expiry pattern this playbook is grounded in.
- Dev-integration setup/secrets/ownership/grants knowledge.
- Supplier-compliance role-grant knowledge, if that surface is in the review.
- PLAY-0019 — Testing & Validation, for confirming the fix actually restored access.
- Documentation knowledge — a runbook only after the live fix is proven.
- PLAY-0029 — Disaster Recovery & Rollback, if the auth break caused active data corruption alongside the access loss.
- The owner’s IT service desk — the organisation’s-side tickets only; not the OAuth/cloud side.

## Anti-patterns

- Reconnecting the client as the first (or only) response to `invalid_grant`.
- Searching backend logs for the string `invalid_grant`.
- Storing refresh tokens in Library Docs/Chats.
- Leaving a real-use OAuth client in Testing.
- Cloning dev-integration secrets to production.
- Treating an ownership transfer on a database as schema-complete.
- Treating "no drift alert" as "permissions are fine" when expectations rows are missing.
- Inventing a credential inventory or review calendar.
- Declaring auth fixed because HTTP was 200.


</details>
