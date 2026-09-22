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

**Pattern:** Single agent + one sequential validator subagent

```
[Scheduled run or high-signal event]
                |
                v
[Cortex: pull evidence and draft update + proposed stories]
                |
                v
[Validator]
    fail, fixable -> Cortex revises (maximum 2 revisions)
    fail, unsafe/unresolvable -> escalate to PM
    pass -> PM review checkpoint -> queued
```

## 3. Roster

| Agent / subagent | Responsibility | Runs which Loop Spec |
|---|---|---|
| Cortex PM Chief of Staff | Pulls project evidence, drafts the status update and proposed stories, responds to fixable validator feedback, and routes the result. | M2 Loop Spec |
| Independent Validator | Checks grounding, identifiers, commitments, queue limits, and output completeness; returns fixable failures or escalates unsafe or unresolvable ones. | M3 validation loop |

## 4. Communication & hand-offs

The current build uses a plain in-process structured hand-off; MCP or A2A is not needed yet.

1. Cortex sends the validator the source evidence, drafted update, proposed stories, project and issue identifiers, and current revision number.
2. The validator returns `PASS`, `REVISE`, or `ESCALATE`, plus failed rule IDs and concise reasons.
3. On `REVISE`, Cortex receives only the verdict and actionable failures.
4. On `PASS` or `ESCALATE`, Cortex packages the draft, evidence references, verdict, and stop reason for the PM review checkpoint.

## 5. The validator

- **What the critic checks:**
  1. The update references the correct project and valid PR/issue IDs.
  2. Every status, figure, and claim is traceable to the pulled source data.
  3. The draft makes no unauthorized commitments, including dates, scope, pricing, or discounts.
  4. Proposed stories stay within the queue cap and are supported by evidence.
  5. The output either meets the required format or clearly escalates missing, conflicting, or insufficient data.
- **Fail action:** Use a tiered response. Return fixable formatting, traceability, or identifier failures to Cortex with the failure noted. Immediately escalate missing evidence, conflicting data, or unauthorized commitments rather than repeatedly guessing.
- **Revision cap:** Allow a maximum of 2 revisions, then escalate to the PM. Cortex gets one opportunity to address the critic's feedback and another to correct anything remaining; the cap also bounds cost and delay and prevents repetitive model calls from delaying PM review.
- **Pass action:** Advance the validated draft to the PM review checkpoint, where it remains queued. Passing validation does not authorize Cortex to post, commit, or make an external commitment.

## 6. State: shared vs isolated

- **Shared:** Source evidence, project and issue IDs, current draft, proposed stories, revision number, validation verdict, failed rule IDs, and final stop reason.
- **Isolated to Cortex:** Drafting scratch work and private reasoning.
- **Isolated to the validator:** Evaluation reasoning and internal analysis; Cortex receives only the verdict and concise actionable failures.

Isolation helps avoid bias or influence, preserves the evaluator's independent perspective, and retains its gap analysis for the PM's final discretion.

## 7. Cost & latency budget

Use the single-agent Cortex run as the baseline (`1x`): it has no independent validation call and reaches PM review with the lowest token use and latency, but it also grades its own work.

The recommended Cortex + validator fleet adds one serial critic call in the normal case, so plan for roughly `1.5-2x` the baseline token use and one additional model-round-trip of latency. At the two-revision cap, the worst case adds three critic calls and two Cortex redrafts, so plan for roughly `3-5x` the baseline token use and up to five additional serial model round trips before escalation. These are planning estimates, not measured benchmarks; the existing `$0.50` whole-run cost cap remains the hard upper bound.
