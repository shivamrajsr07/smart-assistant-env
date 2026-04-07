import os
import requests
from openai import OpenAI
from graders import TASKS

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

ENV_URL = "http://localhost:7860"


def reset():
    return requests.post(f"{ENV_URL}/reset").json()


def step(action):
    return requests.post(f"{ENV_URL}/step", json=action).json()


# 🔥 FIXED SAFE ACTION GENERATOR
def get_action(obs):
    try:
        observation = obs.get("observation", {})

        inbox = observation.get("inbox", [])
        meetings = observation.get("meetings", [])

        # simple deterministic logic (safe)
        if len(inbox) > 0:
            return {"action_type": "reply_email", "email_id": 1}
        else:
            return {"action_type": "schedule_meeting"}

    except Exception:
        # fallback (IMPORTANT)
        return {"action_type": "reply_email", "email_id": 1}


def run():
    print("[START]")

    obs = reset()
    done = False

    while not done:
        action = get_action(obs)
        print(f"[STEP] action={action}")

        step_result = step(action)

        obs = step_result
        done = step_result.get("done", False)

    state = requests.get(f"{ENV_URL}/state").json()

    scores = {}
    for name, grader in TASKS.items():
        try:
            scores[name] = grader(state)
        except Exception:
            scores[name] = 0.0

    print(f"[END] scores={scores}")


if __name__ == "__main__":
    run()