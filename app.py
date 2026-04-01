from openenv_core.env_server.http_server import create_app
from server.smart_assistant_env_environment import SmartAssistantEnvironment
from models import AssistantAction, AssistantObservation

env = SmartAssistantEnvironment()

app = create_app(
    env,
    AssistantAction,
    AssistantObservation,
)