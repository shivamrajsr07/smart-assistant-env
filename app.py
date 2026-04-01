from openenv_core.env_server.http_server import create_app
from server.smart_assistant_env_environment import SmartAssistantEnvironment
from models import AssistantAction, AssistantObservation

app = create_app(
    SmartAssistantEnvironment,   # class (correct)
    AssistantAction,
    AssistantObservation,
)