from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home_page():
    return {"hello": "there"}
