from enum import StrEnum

from pydantic import BaseModel, Field


class Status(StrEnum):
    active = "active"
    unactive = "unactive"
    completed = "completed"

class TaskCreate(BaseModel):
    task: str

class TaskModel(BaseModel):
    task: str|None = Field(default="новый запрос или пустая строка")
    status: Status = Field(default="completed,active,unactive")
