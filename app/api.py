from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_session
from app.database.models.user import User


app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "world"}


@app.get("/users")
def get_all_users(db_session: Session = Depends(get_session)):

    users = db_session.query(User).all()

    return users
