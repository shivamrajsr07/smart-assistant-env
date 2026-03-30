from openenv.core.env_server import Environment
from models import AssistantObservation, AssistantAction, AssistantState


class SmartAssistantEnvironment(Environment):

    def __init__(self):
        self.reset()

    def reset(self):
        self.state = AssistantState(
            step_count=0,
            completed_tasks=0
        )

        observation = AssistantObservation(
            inbox=[
                {"id": 1, "priority": "high", "requires_reply": True},
                {"id": 2, "priority": "low", "requires_reply": False}
            ],
            meetings=[],
            time="09:00",
            done=False
        )

        return observation

    def step(self, action: AssistantAction):
        reward = 0

        if action.action_type == "reply_email" and action.email_id == 1:
            reward += 3
            self.state.completed_tasks += 1

        elif action.action_type == "schedule_meeting":
            reward += 4
            self.state.completed_tasks += 1

        else:
            reward -= 1

        self.state.step_count += 1

        done = self.state.completed_tasks >= 2

        observation = AssistantObservation(
            inbox=[],
            meetings=["10:00"],
            time="10:00",
            done=done
        )

        return observation, reward, done, {}

    def get_state(self):
        return self.state