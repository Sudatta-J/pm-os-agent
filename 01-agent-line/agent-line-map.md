# Agent Line Map: Cortex PM Chief-of-Staff Agent

> Module 1 · The Agent Line
>
> ✅ **What this validates:** every risky action has a clear owner, by the end you'll have proven an above/below-the-line map with HITL checkpoints, scored on reversibility, blast radius, and measurability.

## The workflow, decision by decision

List every discrete decision or action in your agent's workflow, then score each one and place it **above** the line (a human owns it) or **below** (the agent owns it). Borderline calls get an HITL checkpoint.

| Decision / action | Reversibility (H/M/L) | Blast radius (H/M/L) | Measurability (H/M/L) | Rule result | Agent line | HITL checkpoint | First-pass reason |
|---|---|---|---|---|---|---|---|
| Pull project state + recent GitHub/Jira activity | H | L | H | All-green | Below | None | Cortex can safely gather read-only status, activity, and roadmap facts without changing anything. |
| Decide relevant context | H | M | M | Borderline | Below | Human spot-checks selected sources before the draft is treated as complete. | Cortex can narrow the working context from known sources, as long as the sources are bounded and traceable. |
| Draft the update | H | M | H | Borderline | Below | Human reviews the draft before it can be published or shared broadly. | Drafting is reversible and stays private until a human reviews it. |
| Decide tone / commitment level | M | H | M | Any-red | Above | Human approval required before tone or commitments are finalized. | Tone and commitment level can imply promises to leadership, so a human should own that judgment. |
| Flag at-risk escalation | H | M | H | Borderline | Below | Human reviews flagged risks before any action or escalation happens. | Cortex can identify possible risk signals from the data and surface them for review. |
| Choose what to escalate | M | H | M | Any-red | Above | Human approval required for the escalation decision. | Escalation changes stakeholder attention and priority, so the human should decide what actually gets raised. |
| Propose a capped story batch | M | M | H | Borderline | Below | Human approves, rejects, or edits the queued stories before sprint planning. | Cortex can suggest a limited set of next-sprint stories, with the cap preventing runaway backlog changes. |
| Post an update / approve a company-wide one | L | H | H | Any-red | Above | Human approval required before anything is posted. | Publishing creates external visibility and possible commitments, so it needs explicit human approval. |

## Agent anatomy (sketch)

- **Model:** Default to a fast, low-cost model for routine drafting and retrieval; escalate to a stronger frontier model when the critic rejects twice, context conflicts, or the update may affect leadership commitments.
- **Tools:** Read-only project lookup, recent activity lookup, past-update search, roadmap lookup, team norms lookup, and capped story proposal for human approval.
- **Memory:** Persist stable roadmap facts, past decisions, previous updates, and team norms; purge run-specific scratch notes, temporary drafts, and anything marked confidential unless it is needed for the current bounded run.
- **Loop:** Placeholder, defined in M2 `loop-spec.md`.
- **Bounds:** Placeholder, defined in M5 `bounds-and-evals.md`; current build includes max iterations, revision cap, cost cap, and story queue cap.
- **Evals:** Placeholder, defined in M5 `bounds-and-evals.md`; current build already uses a critic pass/fail check before anything reaches the human review checkpoint.

## The golden rule, applied

- Pull project state + recent GitHub/Jira activity sits below the line because it is all-green: high reversibility, low blast radius, and high measurability make read-only gathering safe for Cortex to own.
- Decide relevant context sits below the line with a HITL spot-check because the medium blast radius and medium measurability make it borderline, so Cortex can select sources but a human should verify the frame.
- Draft the update sits below the line with review before publish because the draft is highly reversible and highly measurable, while its medium blast radius is controlled by keeping it private.
- Decide tone / commitment level sits above the line because the high blast radius is a red score: tone can imply promises or leadership commitments even when the text is measurable.
- Flag at-risk escalation sits below the line with human review before action because Cortex's signal detection is reversible and measurable, but the medium blast radius means flags should not become escalation automatically.
- Choose what to escalate sits above the line because the high blast radius is a red score: escalation changes stakeholder attention and priorities, so the final call stays human-owned.
- Propose a capped story batch sits below the line with required approval because the medium reversibility and medium blast radius make it borderline, so Cortex may queue suggestions but not turn them into commitments.
- Post an update / approve a company-wide one sits above the line because low reversibility and high blast radius are red scores, making publication a human-owned action even when the content is easy to audit.

## Hardest call

The hardest call was whether Cortex should choose what to escalate. I resolved it above the line because the blast radius is too high: even a well-reasoned escalation can redirect leadership attention, change priorities, or create anxiety, so Cortex should flag risk signals but a human should decide what actually gets raised.
