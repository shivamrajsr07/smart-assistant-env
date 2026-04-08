def task_email_reply(state):
    # reward if at least 1 task done
    if state.get("completed_tasks", 0) >= 1:
        return 0.8
    return 0.2


def task_meeting_schedule(state):
    if state.get("completed_tasks", 0) >= 2:
        return 0.9
    return 0.3


def task_efficiency(state):
    steps = state.get("step_count", 10)

    if steps <= 3:
        return 0.7
    elif steps <= 5:
        return 0.5
    return 0.2


# 🔥 MUST HAVE AT LEAST 3 TASKS
TASKS = {
    "email_reply": task_email_reply,
    "meeting_schedule": task_meeting_schedule,
    "efficiency": task_efficiency,
}