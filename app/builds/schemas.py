from typing import Any, List

from app.items.schemas import Item
from pydantic import BaseModel


class Build(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    items: List[int] = []

    class Config:
        orm_mode = True


class BuildResponse(Build):
    items: List[Item] = []
