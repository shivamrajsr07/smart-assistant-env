from fastapi import FastAPI
from openenv.core.env_server.http_server import create_app
from server.models import AssistantAction, AssistantObservation
from server.smart_assistant_env_environment import SmartAssistantEnvironment

app = create_app(
    SmartAssistantEnvironment,
    AssistantAction,
    AssistantObservation,
    env_name="smart_assistant_env",
    max_concurrent_envs=1,
)

@app.get("/")
def root():
    return {"message": "Running"}