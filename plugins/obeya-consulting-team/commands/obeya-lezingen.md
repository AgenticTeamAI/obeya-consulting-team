---
name: "obeya-lezingen"
description: "Draai de 6 parallelle lezingen van een Obeya-review, in golven naast elkaar. Gebruik bij \"/obeya-lezingen\", als het systeem al gelezen is en de review bij de lezingen staat."
---

Run the 6 parallel readings of an Obeya review.

**Act as the Lead.** If you have not fetched the Lead's playbook yet, do that
first with `get_playbook` — it holds the rules for this step, including what has
to be done before the readings start. This command only covers how to run them
side by side.

## Before you launch anything

You need the reference of the Obeya under review: its `client_organization_id`
and `obeya_id`. That reference is all a reading gets. **Do not pass the model
itself, and do not pass one role's findings to another** — each reading reads
the Obeya on its own, and six independent readings are only independent if
nobody hands them a summary.

## Run the waves

1. **Wave 1** — launch `obeya-strategy-translator`, `obeya-flow-analyst`, `obeya-facilitation-designer` as subagents **in a single message**, so they run
   at the same time. Give each one the same reference and nothing else.
   Wait until all 3 have handed back, and check each handover before you go on.
2. **Wave 2** — launch `obeya-data-sensemaker`, `obeya-information-architect`, `obeya-visual-designer` as subagents **in a single message**, so they run
   at the same time. Give each one the same reference and nothing else.
   Wait until all 3 have handed back, and check each handover before you go on.

- **Never more than 3 at a time.** Fewer is always allowed; lower it if
  this environment struggles, not to save cost — running them in sequence costs
  the same.
- **An incomplete handover goes back** to the role that made it. Do not fill it
  in yourself.
- **If a reading fails,** run that reading again and keep only its new handover.
  A retry must never leave two sets from the same role for the Assessor.

## If this environment cannot run subagents

Run the readings one at a time, in the order above. The outcome is the same;
only the waiting time differs.

## When all 6 are in

The Assessor consolidates them, in a separate call. Hand the Assessor the
6 handovers as they are — do not merge or smooth them first; contradictions
between readings are part of what the Assessor needs to see.
