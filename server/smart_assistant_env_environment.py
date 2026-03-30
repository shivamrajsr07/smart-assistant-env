from openenv_core.env_server import Environment
from models import AssistantObservation, AssistantAction, AssistantState, Email


class SmartAssistantEnvironment(Environment):

    def __init__(self):
        self.reset()

    def reset(self):
        self.state = AssistantState(
            step_count=0,
            completed_tasks=0
        )

        return AssistantObservation(
            inbox=[
                Email(id=1, priority="high", requires_reply=True),
                Email(id=2, priority="low", requires_reply=False)
            ],
            meetings=[],
            time="09:00",
            done=False
        )

    def step(self, action: AssistantAction):
        reward = 0.0

        if action.action_type == "reply_email" and action.email_id == 1:
            reward = 3.0
            self.state.completed_tasks += 1

        elif action.action_type == "schedule_meeting":
            reward = 4.0
            self.state.completed_tasks += 1

        else:
            reward = -1.0

        self.state.step_count += 1
        done = self.state.completed_tasks >= 2

        return (
            AssistantObservation(
                inbox=[],
                meetings=["10:00"],
                time="10:00",
                done=done
            ),
            reward,
            done,
            {}
        )

    def get_state(self):
        return self.state