# Prototype: Cortex PM Chief-of-Staff Agent

> Module 6 · ★ Deliverable 1, the working agent demo
>
> ✅ **What this validates:** the agent actually runs end to end, by the end you'll have proven it with real screenshots of your Cortex across the six required moments (M2 to M6).

## What it does

_One paragraph: the agent in action, end to end._

## How you built it

- **Coding agent:** _which one you directed (Claude Code / Cursor / Codex)_
- **Model + bounds:** _model used, max iterations, cost cap, queue cap_
- **Repo / config:** _path to your build in `00-build/`_
- **Live link:** _[shareable URL, optional bonus]_

## Screenshots (required, collected M2 to M6)

Real screenshots of *your* Cortex running. These are the `00-build/CORTEX-ANATOMY.md` set and they are required, a link alone is not enough.

| # | Screenshot | What it shows | From |
|---|---|---|---|
| 1 | ![M2 task-happy revision cap](screenshots/m2-task-happy-revision-cap.svg) | `task-happy` run showing a real draft, critic rejection, revision-cap stop, and escalation: held for review, nothing posted | M2 |
| 2 | ![M3 critic rejection and escalation](screenshots/m2-task-happy-revision-cap.svg) | Independent critic rejects an unsupported draft twice; the two-revision bound fires and Cortex escalates to the PM with the draft held and nothing posted | M3 |
| 3 | ![M4 grounded happy path](screenshots/m4-grounded-happy-path.svg) ![M4 missing-data escalation](screenshots/m4-missing-data-escalation.svg) | Grounded `task-happy` update citing pulled activity (`#820`, `#823`, `#825`, activation `41% -> 43%`) plus `missing-data` probe where Cortex refused to invent a GA date for unknown `P-HALO` | M4 |
| 4 | _[img]_ | jailbreak refused + escalated | M5 |
| 5 | _[img]_ | an iteration/cost/queue bound halting a runaway | M5 |
| 6 | _[img]_ | end-to-end run | M6 |

### M2 Run Notes

- `task-happy` produced a real draft but hit the revision-cap stop after the critic rejected it twice; saved at `00-build/run-output/status-update-happy.md`.
- `missing-data` produced a validated escalation because `P-HALO` was not found and Cortex could not commit a GA date without project context; saved at `00-build/run-output/status-update-missing-data.md`.
- Additional M2 escalation evidence: ![M2 missing-data escalation](screenshots/m2-missing-data-escalation.svg)

### M3 Validator Evidence

- The captured `task-happy` trace is reused here because it is a real API-backed run showing the independent critic reject Cortex's draft, return reasons, and trigger the configured fail action at the revision cap.
- M3 subsequently tightened the validator into five named checks and three explicit actions: `PASS`, `REVISE`, and `ESCALATE`. Fixable failures may receive at most two revisions; unsafe or unresolvable failures escalate immediately.
- The critic remains independent because `00-build/critic.py` starts a fresh model call with only the validator instructions, source evidence, and proposed output; it does not inherit Cortex's drafting conversation.
- No new unconfirmed-date demonstration was run, avoiding an additional API charge. The screenshot therefore proves rejection and bounded escalation, while commit `b3e4b3b` contains the later tiered-action implementation.

### M4 Grounding Evidence

- `task-happy` was re-run after ingesting the week-of-2026-07-06 data pack. Cortex pulled `get_activity` for `P-NORTH` and grounded the draft in PR `#820`, PR `#823`, open issue `#825`, and activation `43%` with prior `41%`.
- The same run also retrieved current norms and roadmap context, then held the draft for human review after validator escalation; nothing was posted.
- `missing-data` was re-run as the grounding probe. `get_project(P-HALO)` and `get_activity(P-HALO)` both returned `project_not_found`, so Cortex escalated instead of inventing a Project Halo status or firm GA date.
- The critic also escalated the missing-data output because there was no valid project evidence, no grounded status/metric/date, and no authority to make a launch commitment.

## How to run it

_Minimal steps for someone to reproduce the demo (env vars, and the command or the coding-agent prompt you used)._
