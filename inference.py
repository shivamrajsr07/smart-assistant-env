import requests

BASE_URL = "http://localhost:7860"

print(requests.post(f"{BASE_URL}/reset").json())