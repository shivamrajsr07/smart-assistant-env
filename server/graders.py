def task1(state):
    if not isinstance(state, dict):
        return 0.5
    return 0.6

def task2(state):
    if not isinstance(state, dict):
        return 0.5
    return 0.7

def task3(state):
    if not isinstance(state, dict):
        return 0.5
    return 0.8


TASKS = {
    "task1": task1,
    "task2": task2,
    "task3": task3,
}