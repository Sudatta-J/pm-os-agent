# Extra Exercise: Before Module 2

## 1. Re-score a Decision in My Product

| Product decision | Reversibility | Blast radius | Measurability | Agent line today |
|---|---|---|---|---|
| Let Cortex recommend next-sprint priorities from the PRD, roadmap, and recent engineering activity | M | M | H | Below with HITL approval |

This decision is not safe for full autonomy yet because the story batch is measurable against the PRD, but priority choices are only medium-reversible and can affect sprint planning, so Cortex may recommend the batch while a human approves the final priority call.

## 2. Spot an Agent in the Wild

GitHub Copilot coding agent is an agent, not just a workflow or copilot, because it can take a task, inspect repository context, edit files, run checks, and return a proposed change with a reviewable outcome.

Its agent line should stay at "propose code changes for review" rather than "merge to production" because edits are reviewable, but merging has lower reversibility and a much larger blast radius.

## 3. Add a HITL Checkpoint

Add a HITL checkpoint after Cortex drafts the leadership update and before it is marked ready to share: the human reviewer must confirm that the selected context, tone, and risk language are accurate before the draft can move from "generated" to "approved for posting."
