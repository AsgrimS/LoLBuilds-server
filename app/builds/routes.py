from typing import List

from app.builds.models import Build as BuildModel
from app.builds.models import BuildItem
from app.builds.schemas import Build as BuildSchema
from app.builds.schemas import BuildResponse
from app.core.security import get_current_user
from app.db.database import get_db
from app.items.models import Item
from app.users.models import User
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[BuildResponse], response_model_exclude_none=True)
def get_builds(db: Session = Depends(get_db)):
    builds = db.query(BuildModel).all()
    return builds


@router.get(
    "/{name}/builds",
    response_model=List[BuildResponse],
    response_model_exclude_none=True,
)
def get_user_builds(name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(name=name).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    builds = db.query(BuildModel).filter_by(user=user).all()
    return builds


@router.post("/", response_model=BuildResponse, status_code=status.HTTP_201_CREATED)
def create_build(
    build: BuildSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_build = BuildModel(
        name=build.name, description=build.description, user_id=current_user.id
    )
    item_list = []
    for item in build.items:
        for item_id, item_comment in item.items():
            db_item = db.query(Item).get(int(item_id))
            build_item = BuildItem(item=db_item, comment=item_comment)
            item_list.append(build_item)
    new_build.items = item_list

    db.add(new_build)
    db.commit()

    return new_build


@router.delete("/{build_id}", response_model=BuildResponse)
def remove_build(
    build_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    build = db.query(BuildModel).get(build_id)

    if not build:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Build not found"
        )

    if not build.user == current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    db.delete(build)
    db.commit()
    return build
