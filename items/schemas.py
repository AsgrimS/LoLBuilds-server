from typing import Dict

from pydantic import BaseModel

# class Image(BaseModel):
#     full: str


class Item(BaseModel):
    id: str
    name: str
    description: str
    plaintext: str
    image: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Boots",
                "description": "<mainText><stats><attention> 25</attention> Move Speed</stats></mainText><br>",
                "plaintext": "Slightly increases Movement Speed",
                "image": {"full": "1001.png"},
            },
        }


# class ItemsData(BaseModel):
#     id: str
#     item: Item
