from enum import StrEnum

from pydantic import BaseModel, Field


class Status(StrEnum):
    active = "active"
    unactive = "unactive"
    completed = "completed"

class TaskCreate(BaseModel):
    task: str

class TaskUpdate(BaseModel):
    new_task: str | None = None
    new_status: Status | None = Field(default="completed,active,unactive or None")
