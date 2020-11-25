from typing import List

from app.items.schemas import Item
from pydantic import BaseModel


class Build(BaseModel):
    id: int
    name: str
    description: str
    items: List[Item]

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Boots",
    #             "description": "<mainText><stats><attention> 25</attention> Move Speed</stats></mainText><br>",
    #             "plaintext": "Slightly increases Movement Speed",
    #             "image": {"full": "1001.png"},
    #         },
    #     }
