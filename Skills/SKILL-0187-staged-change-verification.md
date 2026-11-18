---
id: SKILL-0187
type: skill
title: Staged Change Verification
status: current
created: 2026-09-20
updated: 2026-11-15
owner: Library owner

trigger_phrases: ["verify staged update", "read back github change", "candidate workflow result"]
links: [PLAY-0019, PLAY-0042, PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, verification, workflow]
---

# Staged Change Verification

Verifies that staged bytes and workflow status match the intended update.

## When to use

Use after each staged write and before claiming completion.

## Method

1. Read back each changed file from staging.
2. Confirm the final candidate contains the intended complete state.
3. Inspect an existing authorised candidate workflow result for the exact head when available. A source-write request does not authorise starting candidate validation or Actions; distinguish verified staged bytes from pending candidate acceptance.
4. Treat a cancelled older run as superseded only when a newer staging push exists.
5. Do not use tool-call success as evidence.

## Interactive write evidence

For an interactive write, distinguish request accepted, form delivery observed, user submission observed, and destination verified. A tool response saying a form was shown or is awaiting submission proves only the request/deferred state; it does not prove the user received a usable form or that the write occurred. Record the actual returned evidence and any uncertainty.

MUST NOT invent a form URL, button location, pending confirmation, or claim that opening another chat will restore the form. Give navigation only when observed or documented for the actual host. If delivery or submission cannot be established, read the destination to reconcile effects and apply the calling procedure's recovery within existing authority. Never spoof submission fields or bypass a required/pending confirmation. Missing destination access or uncertain effects block a retry and completion claim.

After an observed submission or alternate authorised write, compare the destination with the intended change and verify required surrounding state. The form's appearance, dismissal or successful submission response alone is insufficient.

Design cases: an awaiting-submission response without a visible form leaves delivery and write unconfirmed; a visible form without submission leaves the write pending; a submitted form with mismatched destination fails verification; exact destination readback establishes only the verified effect, not candidate acceptance. These are operator instructions, not a platform-rendering fix or executed UI tests.

## Benchmark case

A push succeeds but readback reveals a missing companion; verification fails until the final candidate is complete.

## Anti-patterns

- Equating API success with correctness
- Ignoring exact-head identity
- Reporting completion before readback

## Stop

Stop with verified staged bytes and the exact-head status of any authorised candidate run; otherwise explicitly report candidate validation as pending. Do not claim filing or candidate acceptance from readback alone.


