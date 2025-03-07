from __future__ import annotations

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    password: str
    email: str
