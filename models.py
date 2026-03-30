from pydantic import BaseModel
from typing import List, Optional, Dict


class Email(BaseModel):
    id: int
    priority: str
    requires_reply: bool


class AssistantState(BaseModel):
    step_count: int = 0
    completed_tasks: int = 0


class AssistantObservation(BaseModel):
    inbox: List[Email]
    meetings: List[str]
    time: str
    done: bool
    reward: float = 0.0
    info: Dict = {}


class AssistantAction(BaseModel):
    action_type: str
    email_id: Optional[int] = None
    reply_text: Optional[str] = None
    meeting_time: Optional[str] = None