from typing import List

from app.db.database import get_db
from app.items.models import Item as ItemModel
from app.items.schemas import Item as ItemSchema
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[ItemSchema])
def get_items(db: Session = Depends(get_db)):
    items = db.query(ItemModel).all()
    return items
