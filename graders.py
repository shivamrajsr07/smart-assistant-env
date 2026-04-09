def safe_get(state, key, default):
    # works for both dict and object
    try:
        if isinstance(state, dict):
            return state.get(key, default)
        return getattr(state, key, default)
    except:
        return default


def clamp(val):
    # force value strictly inside (0,1)
    if val <= 0:
        return 0.1
    if val >= 1:
        return 0.9
    return val


def task1(state):
    try:
        steps = safe_get(state, "step_count", 3)
        score = 0.5 + (0.1 if steps <= 3 else -0.1)
        return clamp(score)
    except:
        return 0.5


def task2(state):
    try:
        completed = safe_get(state, "completed_tasks", 1)
        score = 0.4 + (0.2 if completed >= 1 else 0.1)
        return clamp(score)
    except:
        return 0.5


def task3(state):
    try:
        completed = safe_get(state, "completed_tasks", 1)
        score = 0.6 if completed >= 2 else 0.3
        return clamp(score)
    except:
        return 0.5


TASKS = {
    "task1": task1,
    "task2": task2,
    "task3": task3,
}