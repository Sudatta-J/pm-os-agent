# Production & Autonomy: Cortex PM Chief-of-Staff Agent

> Module 6 · ★ Deliverable 5, how you'd ship it, govern it, and widen trust over time
>
> ✅ **What this validates:** you can ship it, govern it, and widen trust deliberately, by the end you'll have proven an autonomy dial, a Trust Ladder rung with its eval gate, and a governance plan.

## Autonomy Dial by segment

_Autonomy is a product decision per user, not one global setting._

| Segment | Desired autonomy | Why |
|---|---|---|
| **Experienced PM or product lead** | **Supervised** | Cortex can independently assemble grounded drafts and recommendations, while the PM adds business context, resolves trade-offs, and approves any commitment or external action. |
| **New PM or newly assigned project owner** | **Assisted** | The PM initiates each run and reviews Cortex's sources and draft so they can build project context, add real-world perspective, and catch gaps before any downstream action. |
| **Engineering lead** | **Supervised** | Cortex can proactively synthesize engineering activity and flag delivery risks, while the engineering lead validates technical interpretation; prioritization, roadmap commitments, and external messaging still require PM approval. |

## Trust Ladder

- **Current rung:** **Assisted.** A human initiates each run while Cortex gathers evidence, drafts, and validates. It remains at this rung until sustained production results show that it can operate reliably with less monitoring.
- **Eval gate to reach supervised:** Complete at least `50` assisted runs over `4` consecutive weeks, achieve a `>=95%` pass rate across M5 evals EV-1 through EV-4, maintain a `100%` pass rate on EV-5 and EV-6, and record zero unauthorized writes, confidential disclosures, or unsupported commitments. This window is long enough to reveal recurring failures and behavioral drift while allowing Cortex to advance once it has produced credible operating evidence.
- **Clean incident record:** Zero high-severity incidents during the four-week window. Every contained lower-severity failure or near-miss must be reviewed within one business day, added to the deterministic replay suite, and pass before the affected behavior resumes. This keeps serious failures disqualifying while using safely contained near-misses to strengthen Cortex.

## Deployment plan

- **Runtime:** Deploy Cortex as a serverless function invoked by the Monday pre-sync schedule and approved high-signal hooks. This matches the intermittent workload, scales to zero between runs, and gives each execution an isolated timeout, cost record, and trace.
- **Operator / on-call owner:** John Doe is the primary product operator. He owns the production runbook, reviews held drafts and escalations, activates the kill switch when needed, and authorizes recovery. Jane Doe is the engineering escalation owner for runtime, connector, bound-enforcement, and model-service failures. A safety-critical incident immediately pauses Cortex and alerts both owners; Jane restores technical service only after John approves resumption of the affected workflow.
- **Rollback:** For a serious incident, John activates the kill switch and preserves the trace. Jane disables the affected connector or tool, restores the last approved prompt, policy, tool schema, and model configuration, and moves the affected segment down one autonomy rung. Cortex resumes only after the incident becomes a replay fixture and the corrected version passes it.
- **Monitoring:** A production dashboard reports M5 eval pass rate, escalation and human-override rates, latency, cost per run, tool failures, source freshness, approval-queue age, policy violations, confidential-data flags, unsupported commitments, and kill-switch activations. Results are segmented by user type and Cortex version so autonomy decisions rely on operating evidence rather than aggregate averages.

## ROI metrics (beyond adoption & tokens)

| Metric | Target and capture method |
|---|---|
| **First-review acceptance** | At least `80%` of Cortex drafts receive PM approval on first review without a material factual, scope, or commitment correction over four consecutive weeks. Capture approve, revise, and reject decisions in the review queue. |
| **PM time saved / cost-to-serve** | Reduce median PM preparation-plus-review time by at least `50%` over four weeks versus a two-week manual baseline, while keeping every run at or below the `$0.10` hard cap. Capture run start, draft-ready, and PM decision timestamps. |
| **Trust incidents** | Record zero high-severity incidents and fewer than `2%` of runs with a contained lower-severity policy or grounding near-miss over four consecutive weeks. Measure from the incident log, validator outcomes, PM overrides, and cases promoted into the replay suite. |

## Widen-autonomy decision rule

Move one segment up one rung only after it completes at least `50` runs over `4` consecutive weeks, passes EV-1 through EV-4 at `>=95%` and EV-5 and EV-6 at `100%`, achieves `>=80%` first-review acceptance and `>=50%` median time reduction, records zero high-severity incidents and a lower-severity incident rate below `2%`, and passes every open replay case.

## Governance & forward strategy

- **Compliance:** Credentials, secrets, regulated or customer PII, HR records, and confidential data from unrelated projects must never enter a Cortex prompt. Project-scoped confidential context may be retrieved only through approved, access-controlled connectors when the task requires it. Cortex minimizes retrieved fields, isolates context by project, redacts sensitive trace content, restricts reviewer access, and deletes or archives episodic records after the `90`-day TTL. Confidential content never appears in an external draft without explicit human authorization.
- **Safety:** Human approval remains mandatory for external publication, tone or commitment language, launch dates, official risk escalation, backlog changes, confidential disclosure, any source-system write, permission increase, incident-status change, or cross-project data use. These actions remain above the agent line for every segment and autonomy rung. John Doe can activate the kill switch immediately; Jane Doe contains the affected capability, preserves the trace, and follows the approved recovery process.
- **Reliability:** Cortex enforces limits of `8` iterations, `2` validator revisions, `90` seconds, `$0.10` per run, and `10` queued stories. It retries a transient model or connector failure once, then fails closed by preserving the trace, holding any draft, and routing the task to human completion. It also stops on repeated tool failure, conflicting evidence, or any exceeded bound. The assisted pilot does not switch models automatically because a backup model must pass the replay suite before production use.
- **Strategy:** Widen first for experienced PMs or product leads by allowing Cortex to trigger routine status-drafting runs under supervision. This segment provides the strongest business judgment for detecting missing context and resolving trade-offs during the first autonomy increase. Promotion occurs only after this segment independently meets the `50`-run, four-week widening rule and passes every open replay case.
