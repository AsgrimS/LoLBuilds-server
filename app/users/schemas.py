from typing import List

from app.builds.schemas import BuildResponse
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: str

    class Config:
        orm_mode = True


class User(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_admin: bool
    builds: List[BuildResponse] = []
