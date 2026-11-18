"use strict";

const {
  CANDIDATE_STATUS_CONTEXTS,
  CANDIDATE_ATTESTATION_CONTEXT,
} = require("./candidate_contexts.js");

function attemptUrl(context, attempt) {
  if (!Number.isSafeInteger(Number(attempt)) || Number(attempt) < 1) {
    throw new Error("A positive run attempt is required for status ownership");
  }
  return `${context.serverUrl}/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}/attempts/${attempt}`;
}

async function closePendingStatuses({ github, context, sha, attempt, result }) {
  if (!["failure", "cancelled"].includes(result)) return [];
  if (!/^[0-9a-f]{40}$/.test(sha)) throw new Error("An exact candidate SHA is required");
  const targetUrl = attemptUrl(context, attempt);
  const closed = [];
  for (const statusContext of [...CANDIDATE_STATUS_CONTEXTS, CANDIDATE_ATTESTATION_CONTEXT]) {
    // Refresh for each write; never replace another run/attempt's status or a
    // terminal result. GitHub returns newest statuses first, including ties.
    const statuses = await github.paginate(github.rest.repos.listCommitStatusesForRef, {
      ...context.repo, ref: sha, per_page: 100,
    });
    const latest = statuses.find(status => status.context === statusContext);
    if (latest?.state !== "pending" || latest.target_url !== targetUrl) continue;
    // Commit statuses have no compare-and-swap. A race can produce only a
    // conservative failure, never success; the next clean run must re-attest.
    await github.rest.repos.createCommitStatus({
      ...context.repo, sha, state: "failure", context: statusContext,
      description: result === "cancelled"
        ? "Candidate validation cancelled; rerun before readiness"
        : "Candidate validation failed; repair before retry",
      target_url: targetUrl,
    });
    closed.push(statusContext);
  }
  return closed;
}

module.exports = { attemptUrl, closePendingStatuses };
