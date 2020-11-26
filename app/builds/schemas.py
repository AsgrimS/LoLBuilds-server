from typing import List

from app.items.schemas import Item
from pydantic import BaseModel


class Build(BaseModel):
    id: int
    name: str
    description: str
    items: List[int] = []

    class Config:
        orm_mode = True


class BuildResponse(Build):
    items: List[Item] = []
