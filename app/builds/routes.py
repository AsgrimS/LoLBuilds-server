from typing import Dict, List

import requests
from app.builds.schemas import ItemsData
from fastapi import APIRouter, Depends

router = APIRouter()

ITEMS_URL = "http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/item.json"


def get_items():
    r = requests.get(ITEMS_URL)
    if r.status_code == 200:
        items_data = r.json()["data"]
        response = []
        for id, item in items_data.items():
            response.append({"id": id, "item": item})
        return response


@router.get(
    "/",
    response_model=List[ItemsData],
    response_model_exclude_unset=True,
    description="List of items",
)
async def home_page(data: List[dict] = Depends(get_items)):
    return data


# @router.get("/")
# def test():
#     return get_items()
