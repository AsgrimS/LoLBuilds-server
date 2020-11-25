from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    return [{"hello": "number_1"}]
