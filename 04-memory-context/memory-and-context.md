# Context Engineering & Memory: Cortex PM Chief-of-Staff Agent

> Module 4 · Context Engineering & Memory
>
> ✅ **What this validates:** the agent reasons on the right, safe inputs, by the end you'll have proven a context budget, per-source retrieve-vs-long-context decisions, and a memory map with risk mitigations.
>
> 🗂️ **How the lab maps to this file:** In **Part A** (before the lecture) you don't edit this file, you rough-draft on scratch, focused on the per-source calls in **section 2** plus a quick remember/forget + "how it rots" sketch. In **Part B** (after the lecture) you complete **all five sections**; the Lab Guide's guided builder writes this file for you to copy in and commit.

## 1. Context budget

Each Cortex loop should receive the smallest set of context that preserves intent, evidence, safety, and reviewability. Priority order:

1. **Current task brief (`get_task`)** - the source of intent, constraints, and the approval boundary for the run.
2. **Current project record (`get_project`)** - bounded project facts that scope the update and prevent project confusion.
3. **Current activity slice (`get_activity`)** - fresh PRs, issues, and metrics that support the claims in the update.
4. **Current team norms (`get_norms`)** - the guardrails that keep Cortex below the agent line.
5. **Relevant roadmap slice (`get_roadmap`)** - launch/confidentiality constraints and strategic context for the project.
6. **Relevant past updates and decisions (`search_past_updates`)** - format and precedent, used last because stale history should not override current evidence.

## 2. Retrieve vs. long-context: per source

For each data source, decide: **retrieve** (narrow a large/changing corpus to the relevant slice) or **long-context** (just include a bounded set you can reason over).

| Source | Size / volatility | Decision | Why |
|---|---|---|---|
| `get_activity` | Large and changing quickly as PRs, issues, and metrics accumulate. | Retrieve | Retrieve `get_activity` because engineering activity grows and changes quickly, and Cortex only needs the current project's relevant PRs/issues/metrics with citations, not the whole activity history in every prompt. |
| `search_past_updates` | Unbounded history; useful precedent can become stale. | Retrieve | Retrieve `search_past_updates` because prior updates and decision logs grow over time, and Cortex needs the relevant precedent or format example without dragging stale history into every run. |
| `get_roadmap` | Medium now, but contains unrelated projects and confidential flags. | Retrieve | Retrieve `get_roadmap` because the roadmap includes confidential and unrelated items, so Cortex should pull the relevant project slice plus safety flags instead of carrying the whole roadmap into every update. |
| `get_norms` | Medium and policy-like; must remain current. | Retrieve | Retrieve `get_norms` because the current team norms are the guardrails that keep Cortex below the agent line; pulling the relevant rule each run lets it cite the exact no-posting, no-GA-date, and confidential-handling constraint instead of relying on stale or assumed policy. |
| `get_task` | Small, bounded, and authoritative for the run. | Long-context | Keep `get_task` in long context because the task brief is the run's source of intent and authority; Cortex needs the full request, constraints, and "nothing goes out until review" boundary visible throughout the run, not reconstructed from a partial retrieval. |

## 3. Retrieval quality plan

Every retrieved source needs at least one agentic move so Cortex is not just embedding, stuffing, and hoping. The retrieval plan is:

| Source | Routing | Document grading | Reranking | Self-verification | Caching | Why |
|---|---|---|---|---|---|---|
| `get_activity` | Yes | Yes | No | Yes | No | Pull the right project's PRs/issues/metrics, reject irrelevant activity, and verify every metric or PR claim traces back to retrieved activity. |
| `search_past_updates` | Yes | Yes | Yes | No | No | Search the right project/theme, rank the closest precedent first, and avoid stale or unrelated matches overriding current evidence. |
| `get_roadmap` | Yes | Yes | No | Yes | No | Retrieve the relevant project slice plus safety flags, reject unrelated roadmap context, and verify the draft does not leak embargoed work or invent a GA commitment. |
| `get_norms` | Yes | Yes | No | Yes | Same-day | Pull the relevant rule, confirm it applies, verify the draft obeys no-posting/no-GA-date/confidentiality constraints, and refresh before a later run so stale policy does not linger. |

## 4. Memory map (your PM brain)

| Memory type | What Cortex stores | Scope / TTL |
|---|---|---|
| **Working** (in-loop) | _…_ | _this run_ |
| **Episodic** (past runs) | _past status updates, decisions_ | _…_ |
| **Semantic** (durable facts/prefs) | _team norms, roadmap facts_ | _…_ |
| **Shared** (across agents) | _…_ | _…_ |

## 5. Memory risks & mitigations

| Risk | Mitigation |
|---|---|
| _Drift_ | _…_ |
| _Poisoning_ | _…_ |
| _Staleness_ | _…_ |
| _Confidential / retention_ | _scoping + flags (Cortex touches embargoed roadmap)_ |
