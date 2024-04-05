"""Create users table

Revision ID: 6a02bbb960cd
Revises: 
Create Date: 2023-03-26 16:53:25.430495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a02bbb960cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("username", sa.String, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
        sa.Column("created_timestamp", sa.DateTime, nullable=False),
        sa.Column("updated_timestamp", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
