from typing import List

from app.builds.models import Build as BuildModel
from app.builds.models import BuildItem
from app.builds.schemas import Build as BuildSchema
from app.builds.schemas import BuildResponse
from app.db.database import get_db
from app.items.models import Item
from app.users.models import User
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[BuildResponse])
def get_builds(db: Session = Depends(get_db)):
    builds = db.query(BuildModel).all()
    return builds


@router.post("/", response_model=BuildResponse, status_code=status.HTTP_201_CREATED)
def create_build(build: BuildSchema, db: Session = Depends(get_db)):

    if not db.query(User).get(build.user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found for given user_id",
        )

    new_build = BuildModel(
        name=build.name, description=build.description, user_id=build.user_id
    )
    item_list = []
    for item_id in build.items:
        db_item = db.query(Item).get(item_id)
        build_item = BuildItem(item=db_item)
        item_list.append(build_item)
    new_build.items = item_list

    db.add(new_build)
    db.commit()

    return new_build


@router.delete("/{build_id}", response_model=BuildResponse)
def remove_build(build_id: int, db: Session = Depends(get_db)):
    build = db.query(BuildModel).get(build_id)
    if not build:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Build not found"
        )
    db.delete(build)
    db.commit()
    return build
