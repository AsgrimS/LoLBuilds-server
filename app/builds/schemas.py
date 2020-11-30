from typing import List

from app.builds.models import BuildItem
from app.items.schemas import Item
from pydantic.main import BaseModel


class BuildItem(BaseModel):
    item: Item

    class Config:
        orm_mode = True


class Build(BaseModel):
    name: str
    description: str
    items: List[int] = []

    class Config:
        orm_mode = True


class BuildResponse(Build):
    id: int
    user_id: int
    items: List[BuildItem] = []
