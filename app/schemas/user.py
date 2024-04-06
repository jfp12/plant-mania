from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    created_timestamp: datetime
    updated_timestamp: datetime
