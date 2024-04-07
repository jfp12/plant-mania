from http import HTTPStatus

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database.models.user import User


def get_user_by_id(db_session: Session, user_id: int) -> User:
    user = db_session.query(User).filter(User.id == user_id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User with ID={user_id} not found."
        )

    return user
