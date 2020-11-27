from typing import List, Union

from app.db.database import get_db
from app.users.models import User as UserModel
from app.users.schemas import User as UserSchema
from app.users.schemas import UserResponse
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user


@router.delete("/{user_id}", response_model=Union[UserResponse])
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db.delete(user)
    db.commit()
    return user
