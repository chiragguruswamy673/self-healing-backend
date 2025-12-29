def llm_decide(snapshot: dict):
    """
    Mock LLM-powered recovery agent.
    Designed to be replaced with a real LLM later.
    """

    status = snapshot.get("status")
    cpu = snapshot.get("cpu", 0)
    memory = snapshot.get("memory", 0)

    # Simulated LLM reasoning
    if status != "UP":
        return {
            "action": "restart_service",
            "reason": "Service health is DOWN or unreachable"
        }

    if memory > 80:
        return {
            "action": "clear_cache",
            "reason": "Memory usage is critically high"
        }

    if cpu > 80:
        return {
            "action": "throttle_requests",
            "reason": "CPU usage is critically high"
        }

    return {
        "action": "no_action",
        "reason": "System operating within safe limits"
    }
