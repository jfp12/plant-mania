from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_session
from app.database.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.domains.users.helpers import get_user_by_id


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("", response_model=List[UserOut])
def get_all_users(db_session: Session = Depends(get_session)):
    users = db_session.query(User).all()
    return users


@user_router.get("/{user_id}", response_model=UserOut)
def get_single_user(
        user_id: int,
        db_session: Session = Depends(get_session)
):
    return get_user_by_id(db_session, user_id)


@user_router.post("", response_model=UserOut)
def create_user(
        user_create: UserCreate,
        db_session: Session = Depends(get_session)
):
    new_user = User(**user_create.model_dump())

    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)

    return new_user


@user_router.delete("/{user_id}", response_model=UserOut)
def delete_user(
        user_id: int,
        db_session: Session = Depends(get_session)
):
    user = get_user_by_id(db_session, user_id)

    db_session.delete(user)
    db_session.commit()

    return user
