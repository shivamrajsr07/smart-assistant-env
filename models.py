from pydantic import BaseModel
from typing import List, Optional


class Email(BaseModel):
    id: int
    priority: str
    requires_reply: bool


class AssistantState(BaseModel):
    step_count: int
    completed_tasks: int


class AssistantObservation(BaseModel):
    inbox: List[Email]
    meetings: List[str]
    time: str
    done: bool


class AssistantAction(BaseModel):
    action_type: str
    email_id: Optional[int] = None