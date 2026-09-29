# Bounds & Evals: Cortex PM Chief-of-Staff Agent

> Module 5 · Bounds, Trust & Evals
>
> ✅ **What this validates:** the agent fails safe and is measured, by the end you'll have proven a bounds table, a failure-mode register, and a trajectory eval suite with pass thresholds.
>
> Real access = real blast radius. This is where you design for "when it goes sideways," and where you spec the agent by writing its evals.

## 1. Bounds table

| Bound | Value / policy | Which Cortex risk it caps |
|---|---|---|
| **Max iterations** | `8` model/tool steps per run, then stop and escalate with the trace. | Runaway reasoning loop on a stuck or ambiguous task. |
| **Timeout** | `90s` wall-clock timeout per run, then stop and escalate. | Hung tool or API call freezing the workflow. |
| **Token / cost budget** | `$0.50` hard cap per run; stop before the next model call if the estimated cost would exceed it. | Runaway spend or repeated retries burning budget. |
| **Auto-queue / commitment cap** | Max `10` queued stories/actions per run; no launch/date commitments may be queued automatically. | Flooding the backlog or creating implied commitments. |
| **Permissions (JIT / ephemeral)** | Cortex has standing read-only access only. Any write, publish, queue, escalation, or commitment action requires human approval at the relevant HITL checkpoint and receives a single-use, short-lived permission scoped to the exact action, project, destination, and time window. The permission expires after one use or timeout, cannot be reused for adjacent actions, and is logged with the approving human, requested action, evidence, and result. | Misused or leaked standing access, confidential leak, or unauthorized write/publish action. |
| **Kill switch** | A PM or admin kill switch immediately cancels active Cortex runs, blocks new runs, revokes unused JIT permissions, freezes all queued actions, and preserves the trace, draft, tool calls, and cost record for review. Restart requires an explicit human reset after the issue is classified and any unsafe queue items are cleared. | A misbehaving or compromised agent continuing to spend, loop, queue work, or act on temporary permissions. |
| **HITL checkpoints** | Cortex must pause for explicit human approval at seven checkpoints: before any update is posted or shared outside the draft, before tone or commitment language is finalized, before a launch/GA/date commitment is stated, before any risk is escalated to a stakeholder channel, before queued stories enter sprint planning or a backlog tool, before selected context is accepted as complete for a high-impact update, and before flagged risks are treated as the official escalation set. Enforcement is outside the model: Cortex can draft, flag, and queue, but write/publish/escalation permissions stay unavailable until a human approves that exact action. | Cortex acting above the agent line without a human, especially publication, commitments, escalation, or backlog impact. |

## 2. Failure-mode register

| Failure mode | How detected | PM lever |
|---|---|---|
| _Tool misuse_ | _…_ | _…_ |
| _Reasoning loop_ | _iteration count_ | _max-iterations bound_ |
| _Memory drift / poisoning_ | _…_ | _…_ |
| _Confidential leak / permission escalation_ | _…_ | _JIT permissions + confidential guard_ |
| _Coordination conflict_ | _…_ | _…_ |
| _Overconfidence (invented metric / date)_ | _…_ | _critic subagent / HITL_ |

## 3. Trajectory eval suite

Grade the *path*, not just the final answer.

| Dimension | What it checks | Pass threshold | Owner |
|---|---|---|---|
| **Tool-call accuracy** | _right tool, right args_ | _…_ | _…_ |
| **Path / trajectory quality** | _no redundant or unsafe steps_ | _…_ | _…_ |
| **Recovery** | _recovers from a failed step_ | _…_ | _…_ |
| **Task completion** | _outcome actually achieved (grounded update, no leak)_ | _…_ | _…_ |

## 4. Eval lifecycle

- **Offline (fixtures):** _…_
- **CI gate (every change):** _…_
- **Production traces (online):** _…_

> For judge calibration, family separation, and per-turn classifiers, see the sister certification **AI Evals**.

## 5. Replay set

_Which recorded runs become deterministic fixtures you replay on every change?_

## Runaway-loop check

_Describe one runaway scenario and the exact bound that stops it._
