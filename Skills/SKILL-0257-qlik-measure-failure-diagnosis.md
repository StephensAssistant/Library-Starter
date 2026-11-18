---
id: SKILL-0257
type: skill
title: Qlik Expression-Evaluation Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-21
trigger_phrases: ["diagnose Qlik expression evaluation", "trace Qlik set-analysis failure", "debug Qlik aggregation result"]
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047]
tags: [qlik, measure, diagnosis]
---

# Qlik Expression-Evaluation Diagnosis

Locate the first expression-evaluation boundary causing a blank or incorrect Qlik measure after source fields and associations are proven.

## Intent routing contract

Activate only for Qlik expression, set-analysis or aggregation evaluation diagnosis. Source-field mapping belongs to SKILL-0175; association and key-model diagnosis belongs to SKILL-0206.

## When to use

Use only after required fields, aliases, source rows, associations and key populations are proven. Diagnose the accepted expression under the active selections and expected result.

## Method

1. Read the accepted expression exactly and record the active selections and expected result.
2. Verify modifier quoting, date state, null handling, case, alternate-state and evaluation-grain semantics.
3. Expose intermediate sums, counts, set populations and inner aggregation results in dependency order.
4. Identify the first expression component whose evaluated result diverges.
5. Change only that proven component, then reconcile the final result and edge populations.

## Benchmark case

With fields and associations already proven, a blank five-week-cover measure is traced through set modifiers and intermediate Aggr output until one evaluation boundary fails; only that component is corrected.

## Anti-patterns

- Reopening source-field mapping or association design inside this Skill.
- Rewriting the whole expression before exposing intermediate evaluation.
- Treating a syntactically valid expression as a correct result.
- Proceeding without the accepted expression, selections or expected result.

## Output and evidence

Record authoritative inputs, prerequisite proofs, evaluated intermediates, first failed component, result, residual uncertainty, owner and next action.

## Stop

Stop when the first expression-evaluation failure is proven and revalidated, or when source-field or association prerequisites are unproven and must route to SKILL-0175 or SKILL-0206.

## Worked period-end tier/component cases —15October2026


- For period-end-tier attribution, test Aggr dimensional grain as well as dates: customer-only assigned30points to an old tier; customer+tier put all30underGold as required. Voucher breakdown adds voucher while preserving blank-voucher activity.
- Green end3July/Silver start3July: From<=periodEnd and To>periodEnd gave0ambiguous customers; inclusive To>=periodEnd gave305. This is this tier contract, not a universal SCD convention.
- Display labels can conceal multiple components: restricting earned to Earned/Earned& Redeemed omitted positive points on Earned& Returned rows. Authoritative signed fields, not the single label, define movements.
- Test variable expansion and the displayed selected-date range separately from source/customer scope. Quote expanded dates in diagnostic text.
- In this app Yotpo_Transaction_Returned means earning reversed; visible Return Points/Finance Return means Yotpo_Transaction_Reimbursed. Correct untiered grand totals do not prove tier placement.

Positive case: customer3280521225 Silver→Gold,10before+20after=30underGold. Negative: customer-only Aggr or inclusive end misattributes/repeats points. Boundary: missing voucher must not drop legitimate redemptions. These are scoped examples, not a universal replacement master expression or business-approved netting definition.



## Verified shared-endpoint reporting expressions — 21 October 2026


- First read the actual button variables and mappings. This app uses vYotpoRnR (1 Yotpo, 2 Reward & Retain) and vPointsToPounds (0 points, 1 pounds). Earlier assumed vLiabilityBasis and unexplained helper-dependent suggestions were rejected.
- Preserve the user's DD/MM/YYYY date search formatting. Opening and closing select the relevant basis's first/last selected reporting date; movements sum the selected scope.
- Precomputed RnR endpoint rows still need exactly one [RnR Scope End] filter. In this financial-period report it is Floor(Max({<[Liability Basis]={'Reward & Retain'}>} [Reporting Date])). Plain Sum over every endpoint repeats values.
- Apply Num(...,'#,##0.00') in points mode and Money(.../100,'£#,##0.00') in pounds mode. Keep reversals/redemptions/expiry negative only once; reimbursements positive and other adjustments signed.
- Successful single-period totals are insufficient: P4–P5 and all-history were tested using one shared endpoint. This does not prove daily drill-down, non-adjacent selections or universal SCD semantics.

A field/loader failure routes back to the source/association prerequisite owners rather than being hidden by a measure rewrite. Existing trigger, authority and core method remain unchanged.
