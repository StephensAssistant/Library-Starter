---
id: SKILL-0263
type: skill
title: API Bulk-Operation Control
status: current
created: 2026-09-20
updated: 2026-10-17
owner: Library owner

links: [PLAY-0006, PLAY-0018, PLAY-0025, SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0053, SKILL-0054, SKILL-0055, SKILL-0056, SKILL-0057, SKILL-0058]
tags: [skill, api, bulk-operation, asynchronous-extraction]
trigger_phrases: ["control an API bulk operation", "poll an asynchronous extraction job", "retrieve a completed bulk API result"]
---

# SKILL-0263 — API Bulk-Operation Control

## Purpose

Submit, monitor and retrieve one asynchronous API or GraphQL bulk extraction through its complete state lifecycle.

## When to use

Use when the source creates a server-side extraction job whose result becomes available only after polling or callback completion. Do not use for synchronous page traversal or checkpoint selection.

## Method

1. Verify authorised scope, query/object definition, stable IDs and source concurrency limits.
2. Submit one idempotently identifiable bulk request and retain its source-issued operation ID.
3. Poll only documented states at an appropriate interval; distinguish running, completed, failed, cancelled and expired.
4. Stop submission duplication while the operation is non-terminal.
5. On completion, retrieve every source-issued result part and record retrieval evidence.
6. On failure, preserve the source error and decide whether a new operation is safe; never reinterpret failure as an empty result.
7. Return the operation receipt and raw result set for separate validation.

## Benchmark case

A GraphQL bulk query enters CREATED, RUNNING and COMPLETED states before exposing two result files. A passing application submits once, polls without duplicating the job, downloads both source-issued files and records terminal evidence.

## Anti-patterns

- Submitting a replacement job while the first is still running.
- Treating a failed operation as a successful empty extract.
- Polling without a terminal-state or timeout policy.
- Assuming one result file is the entire bulk output.
- Inventing operation identifiers.

## Stop

Stop when the operation reaches a verified terminal state and every declared result part is retrieved, or when authority, operation identity, state semantics or safe retry behaviour is unresolved.

## Verified GraphQL route and terminal-state controls — 4 October 2026

Trigger: adding nested fields to an existing bulk selection can violate source query-shape rules even when the same fields work through the regular API. Verify current query-shape restrictions with a representative probe.

1. Test the proposed bulk route with a narrow existing root-ID filter before changing production selection/pass plans. Regular introspection or one successful regular query does not prove bulk acceptance.
2. Count connections for each actual submitted pass, including the root and nested connections. Preserve any line-based top-level selection filter: nested selections must remain inside their parent field's line. Isolate a newly enlarged connection in a dedicated pass when necessary; only the final required pass may complete the existing watermark.
3. Distinguish connection parents from object lists and verify the required parent identity. Shopify rejected locationsForMove children because the parent nodes lack an unaliased ID field; it separately rejected connections inside Orders.fulfillments because that field is a list. Do not retry either unchanged; hand unsupported routes to complete regular pagination.
4. Before another submission, require a recognised terminal state or a confirmed submission rejection with no operation created. Missing/unknown status can leave an operation running; a cancellation request is not confirmation of cancellation. Stop and reconcile before consuming another slot.
5. A polling-loop budget is not a strict wall-clock deadline when sleeps and HTTP timeouts can extend it. State the actual limits accurately.
6. Do not place an invented Shopify bulk operation ID in a NOT NULL journal field to represent regular extraction. Give regular capture an explicit operating contract rather than falsifying source receipts.

Representative evidence: the Fulfillment Order root + fulfillments + events + fulfillmentLineItems + fulfillmentOrders query completed with one root/four objects, operation gid://shopify/BulkOperation/11146916430158. Its two unsupported alternative routes returned SUBMIT_ERROR with the identity/list restrictions above. the Library owner then accepted an existing-loader three-pass configuration: first lineItems/fulfillmentOrdersForMerge/locationsForMove; second fulfillments with its three child connections; third merchantRequests final. This proved route acceptance and installation, not population parity or scheduled landing.

Keep the query and reproducible probe results with the owner’s canonical extraction record.


## Repeated bulk-export groups and cancelled owners — verified 17 October 2026

Trigger: physical source root count exceeds an exact seeded native-ID set, or an interrupted polling owner leaves a lease.

1. Preserve operation ID, submitted query/hash, source physical counts, seed IDs/versions and cursor. A guard that raises before persisting the last response may leave an older count in the operation journal; inspect the same source operation directly without resubmission.
2. Retrieve the completed bounded result. Compare root rows versus distinct seeded IDs, bounds, versions, duplicates, missing/extra IDs and full associated child groups. A matching root alone does not authorize deletion of its different detail.
3. Normalize only repeated complete rooted groups with identical canonical root payload and child-row multiset. Preserve multiplicity within each retained group. Reject changed detail, unknown/missing roots, changed versions, invalid grouping/parents and advertised physical-count mismatches before COPY. Keep source physical counts separate from normalized row/ID counts and retain downstream quantity/money/relationship checks; never disguise normalization by rewriting source counts.
4. Verify in a controlled existing-operation pilot before broader recovery. Compare physical rows, normalized rows and exact seeded roots before increasing scope.
5. Cancellation is not rollback and may bypass finally/lease cleanup. Identify the precise parent/child query IDs, confirm terminal status and current actor visibility, preserve partial durable effects, and compare the exact lease token/expiry/update timestamp before a one-row release. Do not clear a possibly live or newer owner. Resume existing operations and cursor rather than reset or submit duplicates. Keep a recovery poll budget distinct from a strict wall-clock timeout.

Keep recovery within the separately authorized extraction scope.
