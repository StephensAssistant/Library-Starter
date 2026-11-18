# Permanent ID reservation

All new governed Library records, including Chat entries inside daily files, must receive a serialized permanent-ID reservation before the consuming record is created. Never guess the next ID and never edit `.github/id-reservations.json` manually.

## Preferred path

Run the **Reserve permanent IDs** workflow with the required prefix and count.

## AI / connector fallback

If the connected AI cannot dispatch GitHub Actions workflows, first ensure the authorised `staging` branch exists, then create a GitHub Issue with one of these exact titles:

- `[ID-RESERVE] TICK`
- `[ID-RESERVE] CHAT`
- `[ID-RESERVE] DEC`
- `[ID-RESERVE] ART 2`

The issue-triggered reservation workflow validates the prefix/count and requester write permission, serializes allocation under the same global concurrency lock, commits the receipt to `staging`, comments the reserved ID(s), and closes the issue. The AI must wait for that returned ID before creating the governed record.

Valid prefixes are sourced from `.github/type-prefixes.json`. One-file-per-ID record types use `folders`; daily shared-file Chat entries use `shared_files`. The common allocator scans existing Chat headings plus outstanding reservations, while `check_chat_ids.py` independently enforces Chat sequence, uniqueness and receipt consumption at release.

A reservation may exist temporarily on `staging`, but the main PR gate rejects orphan reservations. Therefore every reservation required by the final staged candidate must be consumed before merge.

If the intended work for an unconsumed reservation cannot be recovered, only the Library owner may mark that identity unused. Keep the original reservation receipt unchanged and add a permanent `.github/deleted-ids.json` tombstone with the authorisation, reason and `replacement: null`. This retires the identity without a filler record, renumbering or reuse; ordinary orphan reservations still fail. The checker validates that a human authorizer is recorded; the operator and reviewer must verify that the Library owner supplied this exception.

## Manual checkout path

If GitHub Actions is unavailable, a sole authorised writer can use the same allocator in a clean checkout of `staging`. Refresh `staging` first and confirm that no reservation workflow or other allocator is running. Run `python .github/scripts/allocate_ids.py TICK 1 --requested-by YOUR_GITHUB_LOGIN`. Use the returned ID with the Ticket template, include any required companion, and commit the ledger and consuming record together. Push normally with no force. If the remote rejects the push because `staging` advanced, reconcile from the latest head and reallocate before relying on the local ID. In a shared Library, use the GitHub workflow to serialize reservations.
