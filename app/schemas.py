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
        default=None,
        min_length=3,
        max_length=100
    )
    completed: bool | None = None


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str