def get_val(state, key, default=0):
    try:
        # works for both dict and object
        return getattr(state, key, state.get(key, default))
    except:
        return default


def task_email_reply(state):
    completed = get_val(state, "completed_tasks", 0)

    if completed >= 1:
        return 0.8
    return 0.2


def task_meeting_schedule(state):
    completed = get_val(state, "completed_tasks", 0)

    if completed >= 2:
        return 0.9
    return 0.3


def task_efficiency(state):
    steps = get_val(state, "step_count", 10)

    if steps <= 3:
        return 0.7
    elif steps <= 5:
        return 0.5
    return 0.2


TASKS = {
    "email_reply": task_email_reply,
    "meeting_schedule": task_meeting_schedule,
    "efficiency": task_efficiency,
}