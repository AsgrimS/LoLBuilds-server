from typing import List

from app.db.database import get_db
from app.users.models import User as UserModel
from app.users.schemas import User as UserSchema
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user


@router.delete("/{user_id}", response_model=UserSchema)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).get(user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
