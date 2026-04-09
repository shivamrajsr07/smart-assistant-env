def task_email_reply(state):
    try:
        completed = getattr(state, "completed_tasks", None)
        if completed is None and isinstance(state, dict):
            completed = state.get("completed_tasks", 0)

        # always safe range
        if completed >= 1:
            return 0.6
        return 0.4
    except:
        return 0.5


def task_meeting_schedule(state):
    try:
        completed = getattr(state, "completed_tasks", None)
        if completed is None and isinstance(state, dict):
            completed = state.get("completed_tasks", 0)

        if completed >= 2:
            return 0.7
        return 0.5
    except:
        return 0.5


def task_efficiency(state):
    try:
        steps = getattr(state, "step_count", None)
        if steps is None and isinstance(state, dict):
            steps = state.get("step_count", 5)

        if steps <= 3:
            return 0.65
        return 0.45
    except:
        return 0.5


TASKS = {
    "email_reply": task_email_reply,
    "meeting_schedule": task_meeting_schedule,
    "efficiency": task_efficiency,
}