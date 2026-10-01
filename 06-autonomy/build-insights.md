# Build Insights: Cortex PM Chief-of-Staff Agent

> Module 6 · ★ Deliverable 4, what you learned building it
>
> ✅ **What this validates:** you can reflect on what building it taught you, by the end you'll have proven the friction, the learning, and the aha that changes how you'd design your next agent.

## Friction

The hardest part was converting "stop when uncertain" into conditions Cortex and its operator could actually detect and enforce. Missing evidence, conflicting sources, repeated critic rejection, prompt injection, and exceeded cost or iteration limits each needed a distinct stop reason and handoff path. The work was less about producing a draft and more about defining exactly when Cortex had earned the right to continue.

## Learning

First, autonomy is a product decision for each user segment, and Cortex should gain it only through measured operating evidence. Second, output quality depends on selecting fresh, authoritative, project-scoped context rather than maximizing prompt size. Third, safety cannot depend on instructions alone; iteration, timeout, cost, permission, and kill-switch controls must be enforced outside the model.

## Aha moment

The quality of an agent is defined as much by its exits as by its output. A polished draft does not make Cortex trustworthy; explicit success, refusal, bound-trip, and human-handoff conditions do. I would design those exits before expanding tools or autonomy in any future agent.

## What you'd do differently

I would define the success, refusal, escalation, bound-trip, and human-handoff conditions before writing the main prompt. I would also start with a narrower pilot focused on weekly status drafting for experienced PMs, collect real traces against the eval suite, and add story proposals or event hooks only after the first capability meets its promotion gate.
