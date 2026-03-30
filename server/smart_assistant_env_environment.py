from openenv.core.env_server import Environment
from models import AssistantObservation, AssistantAction, AssistantState, Email


class SmartAssistantEnvironment(Environment):

    def __init__(self):
        self.reset()

    def reset(self):
        self.state = AssistantState()
        self.inbox = [
            Email(id=1, priority="high", requires_reply=True),
            Email(id=2, priority="low", requires_reply=False)
        ]
        self.meetings = []
        self.time = "09:00"
        self.done = False

        return AssistantObservation(
            inbox=self.inbox,
            meetings=self.meetings,
            time=self.time,
            done=self.done
        )

    def step(self, action: AssistantAction):
        reward = 0

        if action.action_type == "reply_email":
            for email in self.inbox:
                if email.id == action.email_id and email.requires_reply:
                    reward += 3
                    self.state.completed_tasks += 1

        elif action.action_type == "schedule_meeting":
            if action.meeting_time:
                self.meetings.append(action.meeting_time)
                reward += 4
                self.state.completed_tasks += 1

        else:
            reward -= 1

        self.state.step_count += 1

        if self.state.completed_tasks >= 2:
            self.done = True
            reward += 5

        return AssistantObservation(
            inbox=self.inbox,
            meetings=self.meetings,
            time=self.time,
            done=self.done,
            reward=reward
        )

    def get_state(self):
        return self.state