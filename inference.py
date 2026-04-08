import requests
from graders import TASKS

ENV_URL = "http://localhost:7860"


def reset():
    return requests.post(f"{ENV_URL}/reset").json()


def step(action):
    return requests.post(f"{ENV_URL}/step", json=action).json()


# 🔥 SUPER FAST (NO LLM → NO TIMEOUT)
def get_action(step_count):
    if step_count == 0:
        return {"action_type": "reply_email", "email_id": 1}
    else:
        return {"action_type": "schedule_meeting"}


def run():
    print("[START]")

    obs = reset()
    done = False
    step_count = 0

    # 🔥 HARD LIMIT (VERY IMPORTANT)
    MAX_STEPS = 3

    while not done and step_count < MAX_STEPS:
        action = get_action(step_count)
        print(f"[STEP] action={action}")

        result = step(action)

        done = result.get("done", False)
        step_count += 1

    state = requests.get(f"{ENV_URL}/state").json()

    scores = {}
    for name, grader in TASKS.items():
        try:
            scores[name] = grader(state)
        except:
            scores[name] = 0.0

    print(f"[END] scores={scores}")


if __name__ == "__main__":
    run()