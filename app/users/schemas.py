from typing import List

from app.builds.schemas import BuildResponse
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    name: str
    password: str
    builds: List[BuildResponse] = []

    class Config:
        orm_mode = True