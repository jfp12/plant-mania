from app.database.base import Base
import sqlalchemy as sa


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    username = sa.Column(sa.String, nullable=False, unique=True)
    password = sa.Column(sa.String, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    created_timestamp = sa.Column(sa.DateTime, nullable=False)
    updated_timestamp = sa.Column(sa.DateTime, nullable=False)
