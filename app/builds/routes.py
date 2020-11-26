from typing import List

from app.builds.models import Build as BuildModel
from app.builds.schemas import Build as BuildSchema
from app.builds.schemas import BuildResponse
from app.db.database import get_db
from app.items.models import Item
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[BuildResponse])
def get_builds(db: Session = Depends(get_db)):
    builds = db.query(BuildModel).all()
    return builds


@router.post("/", response_model=BuildResponse, status_code=status.HTTP_201_CREATED)
def create_build(build: BuildSchema, db: Session = Depends(get_db)):

    b_items = []
    for id in build.items:
        db_item = db.query(Item).get(int(id))
        if db_item:
            b_items.append(db_item)
    build.items = b_items

    new_build = BuildModel(**build.dict())
    db.add(new_build)
    db.commit()

    return new_build


@router.delete("/{build_id}", response_model=BuildResponse)
def remove_build(build_id: int, db: Session = Depends(get_db)):
    build = db.query(BuildModel).get(build_id)
    db.delete(build)
    db.commit()
    return build
