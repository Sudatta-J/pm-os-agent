# Agent Line Map: Cortex PM Chief-of-Staff Agent

> Module 1 · The Agent Line
>
> ✅ **What this validates:** every risky action has a clear owner, by the end you'll have proven an above/below-the-line map with HITL checkpoints, scored on reversibility, blast radius, and measurability.

## The workflow, decision by decision

List every discrete decision or action in your agent's workflow, then score each one and place it **above** the line (a human owns it) or **below** (the agent owns it). Borderline calls get an HITL checkpoint.

| Decision / action | First-pass placement | Reason |
|---|---|---|
| Pull project state + recent GitHub/Jira activity | Below | Cortex can safely gather read-only status, activity, and roadmap facts without changing anything. |
| Decide relevant context | Below | Cortex can narrow the working context from known sources, as long as the sources are bounded and traceable. |
| Draft the update | Below | Drafting is reversible and stays private until a human reviews it. |
| Decide tone / commitment level | Above | Tone and commitment level can imply promises to leadership, so a human should own that judgment. |
| Flag at-risk escalation | Below | Cortex can identify possible risk signals from the data and surface them for review. |
| Choose what to escalate | Above | Escalation changes stakeholder attention and priority, so the human should decide what actually gets raised. |
| Propose a capped story batch | Below | Cortex can suggest a limited set of next-sprint stories, with the cap preventing runaway backlog changes. |
| Post an update / approve a company-wide one | Above | Publishing creates external visibility and possible commitments, so it needs explicit human approval. |

## Agent anatomy (sketch)

- **Model:** _your default fast model + when you escalate to a frontier model, and why_
- **Tools:** _project + activity lookup (read) · past-update search · roadmap · team norms · story proposal (capped) …_
- **Memory:** _what persists across runs (roadmap, decisions, norms) vs. purged_
- **Loop:** _placeholder, defined in M2 loop-spec.md_
- **Bounds:** _placeholder, defined in M5 bounds-and-evals.md_
- **Evals:** _placeholder, defined in M5 bounds-and-evals.md_

## The golden rule, applied

_One sentence per above-the-line decision: why it stays human (which of reversibility / blast radius / measurability failed)._

## Hardest call

_Your toughest "above vs below" decision and how you resolved it. (Share this in `#cohort-channel`.)_
