# 🚀 Smart Assistant OpenEnv Environment

A real-world reinforcement learning environment where an AI agent learns to manage emails and schedule meetings efficiently.

Built using OpenEnv framework with a standardized HTTP API (`/reset`, `/step`, `/state`).

---

## 🧠 Problem Statement

Modern assistants must:

- Prioritize emails  
- Respond to urgent requests  
- Schedule meetings intelligently  
- Avoid unnecessary actions  

This environment simulates a **real productivity workflow**, not a toy problem.

---

## 🎯 Tasks (Easy → Medium → Hard)

### 🟢 Task 1 — Email Handling (Easy)
- Identify emails requiring reply  
- Respond correctly to high-priority emails  

### 🟡 Task 2 — Meeting Scheduling (Medium)
- Schedule meetings at valid times  
- Avoid duplicate or invalid scheduling  

### 🔴 Task 3 — Multi-Task Decision Making (Hard)
- Balance email replies + meeting scheduling  
- Optimize actions under limited steps  
- Avoid penalties from wrong actions  

---

## ⚙️ Action Space

```json
{
  "action_type": "reply_email | schedule_meeting",
  "email_id": "int (optional)",
  "reply_text": "string (optional)",
  "meeting_time": "string (optional)"
}
👁️ Observation Space
{
  "inbox": [{"id": 1, "priority": "high", "requires_reply": true}],
  "meetings": ["10:00"],
  "time": "09:00",
  "done": false,
  "reward": 0.0
}
🏆 Reward Function (Key Design)
Action	Reward
Correct email reply	+3
Correct meeting scheduling	+4
Wrong/invalid action	-1
Completing all tasks	+5

✔ Supports partial rewards
✔ Penalizes incorrect behavior
✔ Encourages optimal strategy

🧪 API Endpoints
Endpoint	Description
POST /reset	Start new episode
POST /step	Perform action
GET /state	Current internal state
GET /schema	Action & observation schema
GET /health	Service status
▶️ Run Locally
1. Activate environment
.\.venv\Scripts\Activate.ps1
2. Start server
python -m uvicorn server.app:app --host 0.0.0.0 --port 8000
3. Open API
http://localhost:8000/docs
🤖 Baseline Script

Run:

python run_baseline.py

✔ Demonstrates environment interaction
✔ Produces reproducible outputs

🐳 Docker Support
Build:
docker build -t smart-assistant-env .
Run:
docker run -p 7860:7860 smart-assistant-env
🌐 Deployment

Deployed on Hugging Face Spaces using OpenEnv:

👉 (Add your HF link here)

📁 Project Structure
smart_assistant_env/
│
├── server/
│   ├── app.py
│   ├── smart_assistant_env_environment.py
│
├── models.py
├── openenv.yaml
├── run_baseline.py
├── Dockerfile
├── requirements.txt
├── README.md
🧩 Design Highlights
Real-world simulation (not a toy problem)
Multi-step decision making
Reward shaping for RL training
Modular OpenEnv-compatible design
Fully reproducible baseline
✅ Compliance Checklist

✔ OpenEnv API implemented
✔ Typed models (Pydantic)
✔ 3 task levels (easy → hard)
✔ Reward function with signals
✔ Baseline script included
✔ Dockerfile included
✔ Ready for Hugging Face deployment

👨‍💻 Author

Shivam Raj
CSE | AI & Systems Builder