from openenv.core.env_server import Environment
from models import AssistantObservation, AssistantAction, AssistantState, Email


class SmartAssistantEnvironment(Environment):

    def __init__(self):
        super().__init__()
        self.state = None

    # 🔁 RESET
    def reset(self) -> AssistantObservation:
        self.state = AssistantState(
            step_count=0,
            completed_tasks=0
        )

        observation = AssistantObservation(
            inbox=[
                Email(id=1, priority="high", requires_reply=True),
                Email(id=2, priority="low", requires_reply=False),
            ],
            meetings=[],
            time="09:00",
            done=False
        )

        return observation

    # ⚡ STEP
    def step(self, action: AssistantAction):
        reward = 0.0

        # Validate action
        if action.action_type == "reply_email":
            if action.email_id == 1:
                reward = 3.0
                self.state.completed_tasks += 1
            else:
                reward = -1.0

        elif action.action_type == "schedule_meeting":
            if action.meeting_time:
                reward = 4.0
                self.state.completed_tasks += 1
            else:
                reward = -1.0

        else:
            reward = -1.0

        # update state
        self.state.step_count += 1

        done = self.state.completed_tasks >= 2

        observation = AssistantObservation(
            inbox=[],
            meetings=["10:00"],
            time="10:00",
            done=done
        )

        return observation, reward, done, {}

    # 📊 STATE
    def get_state(self) -> AssistantState:
        return self.state