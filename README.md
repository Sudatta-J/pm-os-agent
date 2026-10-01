# Cortex: PM Chief-of-Staff Agent

Cortex is a bounded PM agent that turns current project evidence into a leadership status draft and a capped set of next-sprint proposals. An independent validator checks every output before it reaches the PM review checkpoint. Cortex never publishes, commits a launch date, changes incident status, or writes to a source system without explicit human approval.

**Current Trust Ladder rung:** Assisted<br>
**Launch recommendation:** Approve a serverless assisted pilot for experienced PMs, then widen autonomy only after the defined four-week evidence gate passes.

## Final pitch

Open [`pitch.html`](pitch.html) for the 10-slide capstone deck. Use the on-screen controls or the arrow keys to navigate.

## What Cortex does

1. A Monday schedule, approved high-signal hook, or human request starts a run.
2. Cortex retrieves current project, engineering, roadmap, norms, and historical context.
3. It drafts a grounded status update and queues at most 10 story proposals for approval.
4. An independent validator returns `PASS`, `REVISE`, or `ESCALATE`.
5. Cortex stops at PM review or preserves the trace and escalates. Nothing is posted automatically.

## Safety and operating bounds

| Control | Production policy |
|---|---|
| Iterations | Maximum `8` model/tool steps |
| Validator revisions | Maximum `2` |
| Timeout | `90` seconds per run |
| Cost | `$0.10` hard cap per run |
| Queue | Maximum `10` proposed stories |
| Permissions | Standing read-only access; scoped, single-use approval for any write |
| Kill switch | John Doe can stop runs; Jane Doe owns technical containment and recovery |

## Promotion gate

Cortex moves one segment up one rung only after at least `50` runs over `4` consecutive weeks, `>=95%` pass on EV-1 through EV-4, `100%` pass on EV-5 and EV-6, every open replay passing, zero high-severity incidents, a contained near-miss rate below `2%`, at least `80%` first-review acceptance, and at least `50%` lower median PM preparation-plus-review time.

## Run the prototype

```bash
cd 00-build
cp .env.example .env
# Add OPENAI_API_KEY to .env
python3 -m pip install -r requirements.txt
python3 agent.py happy
```

Additional proofs:

```bash
python3 agent.py missing-data
python3 agent.py jailbreak
CORTEX_MAX_ITERATIONS=2 python3 agent.py happy
```

The fixtures contain mock product data. A normal run costs a fraction of the `$0.10` cap.

## Capstone artifacts

| Module | Artifact | What it proves |
|---|---|---|
| M1 | [`01-agent-line/agent-line-map.md`](01-agent-line/agent-line-map.md) | Risky actions have a human owner |
| M2 | [`02-loop-design/loop-spec.md`](02-loop-design/loop-spec.md) | The loop has explicit triggers and exits |
| M3 | [`03-orchestration/orchestration-map.md`](03-orchestration/orchestration-map.md) | An independent validator checks every draft |
| M4 | [`04-memory-context/memory-and-context.md`](04-memory-context/memory-and-context.md) | Context is current, scoped, and governed |
| M5 | [`05-bounds-evals/bounds-and-evals.md`](05-bounds-evals/bounds-and-evals.md) | External bounds and trajectory evals fail safely |
| M6 | [`06-autonomy/production-and-autonomy.md`](06-autonomy/production-and-autonomy.md) | Autonomy widens only through measured evidence |

Supporting M6 deliverables:

- [`06-autonomy/prototype.md`](06-autonomy/prototype.md): real run evidence from M2 through M6
- [`06-autonomy/build-insights.md`](06-autonomy/build-insights.md): build reflection and lessons

## Status

Cortex is ready for a bounded assisted pilot. It is not yet a supervised or autonomous production agent, and the repository does not claim that the promotion gate has been met.
