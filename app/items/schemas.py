from typing import Dict

from pydantic import BaseModel

# class Image(BaseModel):
#     full: str


class Item(BaseModel):
    id: int
    name: str
    description: str
    plaintext: str
    image: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1001,
                "name": "Boots",
                "description": "<mainText><stats><attention> 25</attention> Move Speed</stats></mainText><br>",
                "plaintext": "Slightly increases Movement Speed",
                "image": "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/item/1001.png",
            },
        }


# class ItemsData(BaseModel):
#     id: str
#     item: Item
