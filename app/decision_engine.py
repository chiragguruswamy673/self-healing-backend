from recovery import recover_service
from llm_agent import llm_decide

def decide_action(snapshot: dict):
    decision = llm_decide(snapshot)

    action = decision["action"]
    reason = decision["reason"]

    print(f"🤖 LLM Agent Decision: {action} | Reason: {reason}")

    if action != "no_action":
        recover_service(reason, snapshot)

