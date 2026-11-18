---
id: SKILL-0169
type: skill
title: Snowflake Streamlit Interface Reconstruction
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0013]
tags: [skill, streamlit, snowflake, interface]
trigger_phrases: [rebuild streamlit interface, screenshot to streamlit, restyle snowflake streamlit]
---

# Snowflake Streamlit Interface Reconstruction

Reconstruct an approved interface in Streamlit in Snowflake while preserving working application contracts.

## When to use

Use when a screenshot or mock-up is being implemented in an existing or new Snowflake-hosted Streamlit application.

## Method

1. Start from the current working script when one exists.
2. Preserve Snowpark loaders, stored-procedure calls, permissions, validation, dialogs, session state and mutations unless scope explicitly changes them.
3. Use functional Streamlit inputs where Python value or file exchange is required.
4. Initialise required state before any read path and verify a clean session.
5. Verify width, padding, scrolling and host behaviour in deployed UAT.
6. Keep credentials and database authority server-side and safely serialize browser-bound values.
7. Verify mutation, rerun, refresh and actionable error paths.

## Decision and evidence details

Retain the working script baseline, authorised reconstruction scope and deployed UAT revision for each clean-session, mutation, rerun and refresh result. Inspect durable effects before repeating a failed or ambiguous mutation; visible stale data does not prove the procedure did nothing.

Boundary design case: local rendering works but Snowflake UAT is inaccessible. Report the local observations separately and keep host behaviour and runtime acceptance unverified.

## Benchmark case

An upload workflow is redesigned. A passing implementation retains file validation and procedure execution, survives a clean session and refreshes visible data after mutation.

## Anti-patterns

- Replacing inputs with styled HTML.
- Testing only outside the Snowflake host.
- Exposing credentials client-side.

## Stop

Stop with separate visual and functional verdicts in the target runtime.
