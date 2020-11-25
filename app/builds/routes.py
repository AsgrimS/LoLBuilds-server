from typing import List

from app.builds.schemas import Build as BuildSchema
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=List[BuildSchema])
def get_builds():
    return [{"build": 1}]
