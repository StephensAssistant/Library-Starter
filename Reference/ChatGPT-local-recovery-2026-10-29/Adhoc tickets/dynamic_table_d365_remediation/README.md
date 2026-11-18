# D365 dynamic-table dependency remediation

Scope: non-Loyalty Snowflake dynamic tables that still depend on
`INGESTION_D365_PROD.INGESTED` after the move to
`D365_DIRECT_INGESTION.INGESTED`.

These scripts are deliberately split into diagnosis and operator-controlled
remediation. They do not change, resume, replace, grant, or transfer ownership
of any Snowflake object.

## Important correction to the reported cause

Current Snowflake behaviour supports a dynamic table reading a regular view
whose dependencies include another dynamic table **only when the view reference
is wrapped in `DYNAMIC_TABLE_REFRESH_BOUNDARY()`**. Without that boundary,
Snowflake cannot coordinate the refresh graph. Reading the replacement dynamic
table directly is still the preferred option when the view adds no required
business logic and coordinated snapshots are required.

Do not assume that every suspended table has this cause. The analysis captures
the scheduling reason, latest refresh result, direct query text, dependency
edges, replacement-object evidence, owner, warehouse, and possible downstream
consumers before proposing a route.

## Run order

1. Run `01_analyse_dynamic_table_dependencies.sql` using a role with sufficient
   `MONITOR`/metadata access. Keep the results from every numbered result set.
2. Classify each candidate:
   - `DIRECT_REPOINT_CANDIDATE`: the old view adds no required semantics and the
     corresponding object in `D365_DIRECT_INGESTION.INGESTED` is verified as a
     dynamic table.
   - `REFRESH_BOUNDARY_CANDIDATE`: the view logic is intentional and independent
     refresh consistency is acceptable.
   - `MANUAL_REVIEW`: target/type/definition/ownership/consumer evidence is not
     complete. Do not change it.
3. Run `02_prepare_remediation.sql`. It emits evidence-capture, grant, validation,
   and resume commands; all state-changing commands remain commented templates.
4. Before editing an existing legacy object, export its deployed `GET_DDL` result
   and retain it in the governed Library. Confirm the required owner from current
   rules and multiple comparable production objects.
5. Recreate only one approved root object at a time, using its exact captured DDL,
   preserving explicit columns, target lag, warehouse, refresh mode, clustering,
   comments, grants and owner. `COPY GRANTS` does not preserve ownership.
6. Run the validation result sets. Resume the root only after source freshness,
   parity, ownership and grants pass. Snowflake can cascade a resume to downstream
   objects that were suspended because of the upstream object; objects manually
   suspended by a user require separate review.
7. Verify every named consumer. A successful refresh or `RUNNING` state alone is
   not proof of restoration.

## Evidence/authority gaps that remain until the scripts are run

- Exact affected objects and suspension reasons.
- Whether each legacy view adds required filters, aliases, joins or policies.
- Exact replacement-object type and schema parity.
- Required owner and authorised production operator/change window.
- Downstream Qlik, Sigma, Streamlit, Public Reporting or other consumers.
- Business priority and whether incorrect/stale data has already been served.

Loyalty matches are reported only as an excluded count and are not included in
candidate or remediation output.

## Evidence returned on 26 October 2026

The initial run proved matching replacement objects are dynamic tables and
identified four non-Loyalty production dynamic tables still referencing the
legacy compatibility views:

- `REPORTING_PROD.AUTOREPLEN.BACKORDERS`
- `REPORTING_PROD.AUTOREPLEN.BACKORDERS_TEST`
- `REPORTING_PROD.FACTTABLES.FACT_GORAMP_DELIVERIES_PO_DETAIL`
- `REPORTING_PROD.SUPPLIER_COMPLIANCE.STG_GORAMP_DELIVERIES_PO_DETAIL`

The returned evidence later corrected an early inference: the GoRamp staging
table does not feed `FACT_GORAMP_DELIVERIES_PO_DETAIL`; they are parallel roots.
The staging table does feed two other production dynamic tables, so it remains
the first technical dependency to assess and repair. `BACKORDERS` feeds the
production `V_RECEIVED_AWAITING_PUTAWAY` view. The returned evidence found no
production object dependencies for `BACKORDERS_TEST` or
`FACT_GORAMP_DELIVERIES_PO_DETAIL`, although external query-text consumers still
require separate confirmation. Stock Position dependencies already use
`D365_DIRECT_INGESTION` directly.

The first script was corrected after the run: candidate discovery now uses
`ACCOUNT_USAGE.OBJECT_DEPENDENCIES` to find view-mediated dependencies, and the
unsupported `suspend_reason_code` field was removed from `SHOW DYNAMIC TABLES`
post-processing. Suspension reason is read from
`DYNAMIC_TABLE_GRAPH_HISTORY.SCHEDULING_STATE` instead.

Subsequent evidence proved all four objects were suspended after five refresh
errors. It also showed that `INVENTDIM` casts two timestamp fields to `VARCHAR`.
The direct-repoint candidates are therefore retained only as diagnostic evidence,
not the recommended execution path. The recommended minimal repair is generated
by `05_generate_refresh_boundary_fix.sql`: keep each compatibility view and wrap
it with `DYNAMIC_TABLE_REFRESH_BOUNDARY()` in the downstream dynamic-table DDL.
This preserves the view contract while breaking the unsupported coordinated
refresh edge. Use `06_validate_after_boundary_fix.sql` after each individual
replacement.

The pre-change validation run showed all four objects still `SUSPENDED` and all
legacy-view inputs outside a refresh boundary. The first generator result also
showed 8 and 9 boundary insertions for `BACKORDERS` and `BACKORDERS_TEST`, because
those definitions reference some of the same inputs more than once. Script 05
was corrected to calculate the required boundary count from every reference in
the deployed DDL while retaining the separate 5/4/1/1 distinct-input safety
floor. Discard the earlier generated candidate rows and rerun script 05 before
executing any replacement DDL.

The corrected generator was rerun successfully. All four candidates passed the
boundary-count, `COPY GRANTS`, and changed-definition gates. Calculated reference
counts were 1 for staging GoRamp, 8 for `BACKORDERS`, 1 for fact GoRamp, and 9
for `BACKORDERS_TEST`; the latter two exceed their distinct-input counts because
some views are referenced more than once. The subsequent validation output was
still pre-change: all four objects remained suspended and every legacy view was
outside a boundary. These results validate the candidate generation only; they
do not evidence execution or recovery.

