# Loop Spec: Cortex PM Chief-of-Staff Agent

> Module 2 · Loop Engineering, ★ Deliverable 2
>
> ✅ **What this validates:** the agent knows when to run and when to stop, by the end you'll have proven a one-page Loop Spec with a trigger, a definition of "done," and explicit stop conditions.
>
> Your one-page blueprint for how the work you handed to the agent (M1) actually *runs*.
> An agent is just a prompt that fires itself, this spec says when it fires, what "done" means, and what it needs to do the job. Living document; refine as the course progresses.

## 1. Trigger & loop type

**Chosen type:** cron primary, with high-signal hooks for exceptions and bounded goal-style iteration inside each run.

Cortex should fire on a fixed schedule first: Monday morning before the VP/product leadership sync, ideally 60-90 minutes before the meeting so there is time for human review. It should also fire on high-signal events: a launch gate changes, a Sev-1 or launch-blocking issue appears, a major PR merges, sprint planning is coming up, or someone explicitly asks for a status update.

I am ruling out heartbeat as the default because it would waste runs when nothing has changed, and I am not using goal as the trigger because goal loops are powerful but risky without tight exits. Cortex can still use goal-style iteration inside one run: draft, validate, revise until success, a stop condition, or a human handoff.

**Dedupe rule:** scheduled runs dedupe on `project_id + week + sync_type`; hook-triggered runs dedupe on `source_event_id`, so the same schedule or event cannot create duplicate drafts.

## 2. Goal / definition of done

One run is done when Cortex produces either a grounded draft for review or a validated escalation note, then stops without posting, committing dates, or changing source systems.

The finish line is not always a polished update. If the project is missing, the data conflicts, or the request asks for a commitment Cortex is not allowed to make, a clear handoff is also a valid finished run.

## 3. Stop conditions

| Condition | What it looks like | What happens |
|---|---|---|
| **Success** | Cortex produces a grounded update, any proposed stories are within the cap, and the critic passes. | Queue the draft for human review; nothing is posted automatically. |
| **Successful escalation** | Cortex cannot safely complete the requested update but can explain the blocker with evidence, such as missing project data or an unconfirmed GA date. | Queue the escalation note for human review; nothing is invented or posted. |
| **Stuck / give-up** | The critic rejects twice, max iterations are reached, the same tool failure repeats, or source data conflicts cannot be reconciled. | Stop revising, save the last draft or trace, and escalate with the exact stop reason. |
| **Escalate-to-human** | Cortex reaches anything above the M1 agent line: public update, GA-date commitment, launch status judgment, confidential data, Sev-1/launch hold, story batch over cap, or uncertain escalation. | Refuse the autonomous action and route to the HITL checkpoint. |

## 4. Observed starter runs

| Fixture | What happened | Loop lesson |
|---|---|---|
| `task-happy` | Cortex gathered project/activity/roadmap/norms, drafted an update and story batch, but the critic rejected the draft until the revision cap stopped the loop. | The loop needs a revision-cap stop and should treat validator failure as a clean handoff, not an endless retry. |
| `missing-data` | Cortex could not find P-HALO, refused to invent a GA date, passed the critic, and saved an escalation note for human review. | Missing source data can still be a successful run if Cortex explains the blocker and avoids making commitments. |

## 5. State

Cortex state should stay narrow and auditable: project ID, run timestamp, source snapshot IDs or links, previous approved update, critic verdict, stop reason, human approval/rejection, and proposed story batch count.

It should not persist scratch drafts, confidential cross-project data, private reasoning traces, or stale roadmap memory outside the source-of-record docs. Roadmap facts, PRD details, and team norms should be pulled fresh from their source each run instead of quietly becoming model memory.

## 6. The five things a loop can lean on

_`state` is always-on. `connectors` only if you already have one wired (e.g. a Jira key or Google MCP), otherwise just note it as a plan. `skills`, `subagents`, `work tree` scale with autonomy; "not needed yet, because…" is a valid answer._

| Component | For Cortex |
|---|---|
| **Work tree** (isolated workspace per run, a git worktree) | Not needed yet because Cortex drafts PM artifacts rather than changing code or repo files; useful later for generated artifacts, run logs, screenshots, and reviewable changes. |
| **Skills** (reusable capabilities) | Status-update drafting, PRD-to-story proposal, risk summarization, confidentiality checking, prompt-injection checking, and critic validation. |
| **Plugins / connectors** (tools & access, optional if you don't have one yet) | Current: fixture-backed project lookup, activity lookup, roadmap, past updates, team norms, and story proposal. Future: GitHub, Jira/Linear, roadmap docs, metrics dashboard, incident tracker, and human review queue. |
| **Subagents** (independent check when the loop can't grade itself) | Not fully needed yet beyond the current critic because M3 will formalize orchestration and independent validators. |
| **State tracking** | Project ID, run timestamp, source snapshot IDs, previous approved update, critic verdict, stop reason, human approval/rejection, story batch count, cost, and iterations. |

> Context plan (M4) and the hand-off to bounds & evals (M5) come in later modules, you'll add them to their own deliverables then, not here.

## 7. Link to live loop

[`../00-build/agent.py`](../00-build/agent.py)
