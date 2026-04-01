from openenv_core.env_server.http_server import create_app
from server.smart_assistant_env_environment import SmartAssistantEnvironment

env = SmartAssistantEnvironment()
app = create_app(env)