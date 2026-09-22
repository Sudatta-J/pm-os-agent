# Orchestration Map: Cortex PM Chief-of-Staff Agent

> Module 3 · Orchestration & Subagents, ★ Deliverable 3
>
> ✅ **What this validates:** nothing advances unchecked, by the end you'll have proven a justified topology, a roster, and a validator with a defined fail action.
>
> Builds on your M2 Loop Spec. Only split one agent into a team when there's a real reason, coordination has a cost.

## 1. Why split? (or why not)

Cortex gathers project evidence on a schedule or high-signal event, drafts a grounded status update, validates the result, and either sends it to the PM review checkpoint or escalates when it cannot proceed safely.

| Reason | Applies? | Why / why not |
|---|---|---|
| Separation of concerns | No | Evidence gathering and drafting are one coherent workflow, so splitting them would add coordination without a clear benefit. |
| Parallelism | No | Drafting depends on the evidence pull, and validation depends on the draft, so the workflow is primarily sequential. |
| Independent validator | Yes | Having an independent validator review the draft provides fresh context, an additional perspective, and a meaningful safety check that may identify gaps, unsupported claims, unauthorized commitments, and missing evidence before PM review. |
| Context-window pressure | No, for now | The current fixture-backed workflow is small enough that context size does not justify splitting the drafting work. |

**Decision:** Split minimally. One independent validator subagent will review the draft, bring a fresh perspective, and identify any gaps without turning the whole workflow into a multi-agent system.

## 2. Topology

**Pattern:** _single+subagents · sequential · parallel+aggregate · hierarchical_

```
[ simple text diagram of the flow ]
e.g.  task → [Research] + [GitHub/Jira reader] → [Writer] → [Critic ✓] → human checkpoint → queued
```

## 3. Roster

| Agent / subagent | Responsibility | Runs which Loop Spec |
|---|---|---|
| _Chief-of-staff (Cortex)_ | _orchestrates + assembles the update_ | _M2 loop_ |
| _Research subagent_ | _pulls competitive / market context_ | _research loop_ |
| _GitHub/Jira reader_ | _summarizes recent activity_ | _read loop_ |
| _Critic / Validator_ | _checks the draft before it advances_ | _validation loop_ |
| _…_ | | |

## 4. Communication & hand-offs

_What passes between the parts? Any protocol (MCP / A2A, optional, note if used)._

## 5. The validator

- **What the critic checks:** _grounded claims · norms compliance · no confidential leak · nothing posted/committed_
- **Fail action:** _what happens when it fails (retry · revise · escalate to human)_

## 6. State: shared vs isolated

_What's shared across the fleet vs kept isolated per subagent (carry from M2)._

## 7. Cost & latency budget

_Coordination has a price. Rough token/latency cost of the fleet vs a single agent. (Forward-link to M5 bounds.)_
