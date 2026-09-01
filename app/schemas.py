from pydantic import BaseModel, Field
from datetime import datetime

class TodoCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    completed: bool = False

class TodoUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    completed: bool

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: datetime

    class Config: 
        from_attributes = True


class TodoPatch(BaseModel):
    title: str | None = Field(
        default= None,
        min_length=3,
        max_length=100
    )

    completed: bool | None = None
    