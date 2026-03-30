from fastapi import FastAPI
from openenv.core.env_server.http_server import create_app
from server.models import AssistantAction, AssistantObservation
from server.smart_assistant_env_environment import SmartAssistantEnvironment

# Create OpenEnv app
app = create_app(
    SmartAssistantEnvironment,
    AssistantAction,
    AssistantObservation,
    env_name="smart_assistant_env",
    max_concurrent_envs=1,
)

# ✅ Root endpoint (VERY IMPORTANT for HF + health check)
@app.get("/")
def root():
    return {"message": "Smart Assistant Environment is running 🚀"}