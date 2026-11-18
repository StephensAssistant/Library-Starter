---
id: SKILL-0028
type: skill
title: Reproduction knowledge — write it so it can be rebuilt
status: current
created: 2026-09-05
updated: 2026-10-13
owner: Library owner

trigger_phrases: [write it so it can be rebuilt, reproduction detail, capture the method]
links: [PLAY-0046]
tags: [skill, library-mechanics, evidence, documentation]
---

# Reproduction knowledge

Writing a record so an AI can rebuild the work from it, without the original files.

**Used by:** `PLAY-0041` (learning capture), `PLAY-0051` (closure) — and any task that records how something was built.

## The principle

**The Library holds the knowledge to rebuild things, not an archive of the things themselves.**

A stored file goes stale, costs tokens to traverse, and answers only the question it was captured for. A well-written record answers questions nobody asked yet.

**The test:** could a competent AI, reading this record alone, produce working code that does the same thing?

If not, the record is incomplete. If yes, the original working file may be redundant only when its owning contract does not require retention; reproduction prose does not supersede required native evidence or deployed definitions.

This is language-agnostic. SQL, Python, C#, JavaScript, Qlik script, shell — same discipline.

## What must be in the record

### Business logic — exact, not descriptive

Not: "filter to full price sales"

But: "Full price = `DISCOUNT_PCT = 0` AND `SALE_TYPE NOT IN ('STAFF','CLEARANCE')`. Note `DISCOUNT_PCT` is null for concession lines — treat null as 0."

The difference is that the second can be written into code. The first requires asking someone.

### Field mappings — source to target, every transformation named

```
SOURCE.ORDER_DT        → FACT.ORDER_DATE       CAST to DATE, source is VARCHAR 'DD/MM/YYYY'
SOURCE.CUST_REF        → DIM.CUSTOMER_KEY      LTRIM zeros, then join
SOURCE.AMT             → FACT.NET_AMOUNT       Divide by 100 — source is in pence
(derived)              → FACT.IS_FULL_PRICE    See business logic above
```

### Join patterns — keys, cardinality, and the edges

```
FACT_SALES ⋈ DIM_STORE on STORE_KEY
  - Left join: sales exist for closed stores no longer in the dimension
  - ~40 orphans per month, expected, excluded from store-level reporting
  - Duplicate STORE_KEY rows exist pre-2023 — filter DIM.IS_CURRENT = 1
```

**The edges are the part people forget and the part that breaks rebuilds.** Nulls, duplicates, missing matches, late-arriving rows.

### Dependencies and order

What must exist first, and in what sequence. Include the reason where it is not obvious.

### Validation criteria

- Expected row counts or ranges
- Reconciliation points — what this should tie back to, and to what tolerance
- Known exceptions, with the reason each is acceptable
- What a wrong result looks like

### Architecture decisions

What was chosen, **what was rejected, and why**.

The rejected options are the expensive knowledge. Without them, the next person re-evaluates the same dead ends.

### Where the source data lives

Enough to pull it again — system, schema, object, and any access route or filter that matters.

## Preserve exactly

When compressing or summarising, these survive verbatim:

**Constraints. Negations. Thresholds. Units. Dates. IDs. Authority. Sources. Exceptions. Rollback steps. Failure evidence.**

These are the things that turn a right answer into a wrong one. "Amounts are in pence" is not a detail.

## When a file is still warranted

| Case | Verdict |
|---|---|
| An accepted reusable or runnable script, including validation code retained for rerun | **Native Artifact** under the current artifact filing rules; retain the executable file and its authoritative context, with reproduction prose alongside it. |
| A new or changed Snowflake definition, or the current legacy definition before change | Store the exact definition under AGENTS.md Library rule 12, with explicit verification provenance; reproduction prose supplements it. |
| A snapshot of external code as evidence of prior state | **Reference** — you cannot reproduce a past state |
| A large irreproducible binary (a .qvf, a supplier's one-off export) | **Reference** — genuinely irreproducible |
| Everything else | **Inline.** File the knowledge. |

Unaccepted exploratory queries, exports and proofs of concept remain in AI-local scratch. Capture their verified reusable learning in its existing owner; when the Library owner accepts a working script for reuse, retain its native form under the current artifact filing rules and AGENTS.md rather than discarding it because prose can describe the logic.

## The 15-line flag

`check_embedded_scripts.py` flags fenced code blocks over 15 lines as extraction candidates.

It is **informational only and never blocks**. Its own docstring says the judgement is not cleanly automatable.

A long block that is reproduction knowledge rather than a runnable tool is correct where it is. The flag is a prompt to think, not an instruction to extract.

## Worked contrast

> **Illustrative only.** The field names, figures, and logic below are invented to show the shape of a good record. Do not treat any of it as fact about a real production system.

**Insufficient:**

> Fixed the full price logic in the Trade KPI report. Updated the Qlik script and the Snowflake view.

Rebuilds nothing. Names no logic, no fields, no validation.

**Sufficient:**

> **Full price definition (corrected 2026-09-02)**
>
> Previously `DISCOUNT_PCT = 0` alone, which wrongly included staff and clearance sales.
>
> Corrected to: `DISCOUNT_PCT = 0 AND SALE_TYPE NOT IN ('STAFF','CLEARANCE')`
>
> `DISCOUNT_PCT` is null on concession lines — `COALESCE(DISCOUNT_PCT, 0)` before comparing, or concessions drop out entirely.
>
> **Applied in:** the Snowflake view's `IS_FULL_PRICE` flag, and the Qlik Transform section's equivalent.
>
> **Validation:** FY2021 full-price total moved from £X to £Y, a Z% reduction, matching the finance team's independent figure to within £N. Staff sales now reconcile separately.
>
> **Rejected:** a `PRICE_TYPE` lookup table — the field is unpopulated before 2023, so historical reporting would have broken silently.

Rebuildable. Every claim is checkable.

## Anti-patterns

- "Updated the logic" with no logic
- Describing a transformation instead of stating it
- Omitting edge cases because they were handled at the time
- Recording the chosen approach without the rejected ones
- Naming a validation without its expected value
- Assuming the reader has the source file
- Using a code fence as a substitute for explanation — the fence shows *what*, the prose must give *why*
- Compressing away a unit, a threshold, or a negation

## Benchmark case

Document a data-processing repair with its exact inputs, prerequisites, ordered commands, expected outputs and verification checks so a fresh authorised operator can rebuild the same result without relying on chat history.

## Stop

Stop when an independent operator has enough current, source-backed detail to reproduce and verify the outcome, or when an unresolved dependency prevents a faithful rebuild.
