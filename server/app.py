from openenv.env_server.http_server import create_app
from models import AssistantAction, AssistantObservation
from server.smart_assistant_env_environment import SmartAssistantEnvironment

app = create_app(
    SmartAssistantEnvironment,
    AssistantAction,
    AssistantObservation,
    env_name="smart_assistant_env",
    max_concurrent_envs=1,
)