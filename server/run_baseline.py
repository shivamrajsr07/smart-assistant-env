import requests

BASE_URL = "http://localhost:8000"

# Reset environment
print("Resetting environment...")
res = requests.post(f"{BASE_URL}/reset")
print(res.json())

# Run steps
for i in range(3):
    action = {
        "action_type": "reply_email",
        "email_id": 1
    }

    res = requests.post(f"{BASE_URL}/step", json=action)
    print(f"Step {i+1}:", res.json())