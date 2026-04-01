def task_email_reply(state):
    return 1.0 if state["completed_tasks"] >= 1 else 0.0


def task_meeting_schedule(state):
    return 1.0 if state["completed_tasks"] >= 2 else 0.0


def task_efficiency(state):
    return 1.0 if state["step_count"] <= 3 else 0.0


TASKS = {
    "email_reply": task_email_reply,
    "meeting_schedule": task_meeting_schedule,
    "efficiency": task_efficiency,
}