from typing import Dict, List, Optional

from app.builds.models import BuildItem
from app.items.schemas import Item
from pydantic.main import BaseModel


class BuildItem(BaseModel):
    item: Item
    comment: Optional[str]

    class Config:
        orm_mode = True


class Build(BaseModel):
    name: str
    description: str
    items: List[Dict[int, str]] = [{}]


class BuildResponse(Build):
    id: int
    user_id: int
    items: List[BuildItem] = []

    class Config:
        orm_mode = True
