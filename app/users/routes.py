from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
def home_page():
    return {"hello": "user"}
