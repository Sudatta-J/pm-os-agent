"""Independent validator (M3). A separate model call that never saw the drafting
context, so it can't inherit the draft's blind spots. Returns a pass/fail verdict.
The revision cap that stops a critic<->drafter loop lives in `agent.py`.
"""

from __future__ import annotations

import json

from prompts import CRITIC_SYSTEM


def review(client, model: str, proposed_output: str, source_data: str) -> dict:
    """Return the independent critic's verdict, action, checks, and reasons."""
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": CRITIC_SYSTEM},
            {"role": "user", "content":
                f"SOURCE DATA Cortex used:\n{source_data}\n\n"
                f"CORTEX PROPOSED OUTPUT:\n{proposed_output}"},
        ],
        response_format={"type": "json_object"},
    )
    usage = resp.usage
    try:
        verdict = json.loads(resp.choices[0].message.content)
    except (json.JSONDecodeError, TypeError):
        verdict = {
            "verdict": "fail",
            "action": "ESCALATE",
            "failed_checks": ["CRITIC-OUTPUT"],
            "reasons": ["critic returned unparseable output"],
        }
    action = str(verdict.get("action", "")).upper()
    if action not in {"PASS", "REVISE", "ESCALATE"}:
        action = "PASS" if verdict.get("verdict") == "pass" else "ESCALATE"
    verdict["action"] = action
    verdict["verdict"] = "pass" if action == "PASS" else "fail"
    verdict.setdefault("failed_checks", [])
    verdict.setdefault("reasons", [])
    verdict["_usage"] = {"prompt": usage.prompt_tokens, "completion": usage.completion_tokens}
    return verdict
