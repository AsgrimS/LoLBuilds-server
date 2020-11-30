from typing import List

from app.core.security import oauth2_scheme
from app.db.database import get_db
from app.items.models import Item as ItemModel
from app.items.schemas import Item as ItemSchema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[ItemSchema])
def get_items(db: Session = Depends(get_db), _: str = Depends(oauth2_scheme)):
    items = db.query(ItemModel).all()
    return items
