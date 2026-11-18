---
id: PLAY-0053
type: playbook
title: Governed Reporting Platform — Compliant Change & Migration Workflow
status: current
created: 2026-08-30
updated: 2026-10-28
owner: the Library owner
links: [PLAY-0014, PLAY-0046, PLAY-0064, PLAY-0065, PLAY-0072, PLAY-0074]
tags: [playbook, governed-reporting-platform, dbt, snowflake, azure-devops, engineering-workflow, migration]
---

# Governed reporting platform change gate

1. Identify the target repository, deployed revision, environment, role and approved change route. Read the current repository conventions, access rules, engineering workflow, migration guide, document catalogue and troubleshooting guidance. Stop if a required source or permission cannot be verified.
2. Check the proposed branch, naming, environment-neutral implementation, destination and validation against live repository policy. Require the named human reviewer and any production or documentation approval. Treat deployment and release as separate authority.
3. For a report migration, inventory the source, compare grain, metrics, filters, access and output parity, and verify the target. Obtain the route decision and release acceptance before cutover, monitor through the agreed hypercare, and retire only with explicit approval.
4. Keep generated documentation as draft until its owner accepts it. Use current platform evidence for troubleshooting and escalate any unrecognised case or contradiction.
5. Return the verified next action or precise blocker, with the source revision and evidence. Never infer a deployed state or overwrite newer work from an exported snapshot.

## Route and release checks

- Confirm ground truth before advising. Check current folder paths, target branch, naming, approved change class, actor and prerequisites. Stop the dependent action when any required item is unverified.
- For code and configuration, use the approved branch prefix and environment-neutral implementation. Add the asset’s required schema documentation and tests, inspect the exact diff, and identify the next CI gate. Record the PR and outstanding checks separately from approval, merge and deployment.
- For migration, use the applicable route Playbook and confirm the report’s current stage against the live inventory. Identify the next entry condition and any route decision or assurance sign-off required.
- For documentation, read the current catalogue and verify owner, status and destination. Keep generated material as draft until independent owner acceptance.
- For troubleshooting, check the current runbook. If it has no supported route, report the gap and investigate within the authorised scope. Recheck the repository revision after any evidence of drift.
