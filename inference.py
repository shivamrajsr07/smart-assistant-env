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


def get_action(obs):
    prompt = f"Inbox: {obs['inbox']}, meetings: {obs['meetings']}"

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )

    # simple rule fallback
    return {"action_type": "reply_email", "email_id": 1}


def run():
    print("[START]")

    obs = reset()
    done = False

    while not done:
        action = get_action(obs)
        print(f"[STEP] action={action}")

        obs, reward, done, _ = step(action)

    state = requests.get(f"{ENV_URL}/state").json()

    scores = {}
    for name, grader in TASKS.items():
        scores[name] = grader(state)

    print(f"[END] scores={scores}")


if __name__ == "__main__":
    run()