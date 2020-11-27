from typing import List

from app.builds.models import BuildItem
from app.items.schemas import Item
from fastapi.param_functions import Depends
from pydantic.main import BaseModel


class BuildItem(BaseModel):
    item: Item

    class Config:
        orm_mode = True


class Build(BaseModel):
    name: str
    description: str
    user_id: int
    items: List[int] = []

    class Config:
        orm_mode = True


class BuildResponse(Build):
    id: int
    items: List[BuildItem] = []
