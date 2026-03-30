import requests

BASE_URL = "http://localhost:7860"

# reset
res = requests.post(f"{BASE_URL}/reset")
print("RESET:", res.json())

# step
action = {
    "action_type": "reply_email",
    "email_id": 1
}

res = requests.post(f"{BASE_URL}/step", json=action)
print("STEP:", res.json())