"""create plants table

Revision ID: d4b860d74a2c
Revises: 6a02bbb960cd
Create Date: 2024-04-05 21:21:30.297995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b860d74a2c'
down_revision = '6a02bbb960cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "species",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("country", sa.String, nullable=True),
        sa.Column("water_frequency", sa.Integer, nullable=False),
        sa.Column("lighting", sa.String, nullable=False),
    )

    op.create_table(
        "plants",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("name", sa.String, nullable=True, unique=True),
        sa.Column("location", sa.String, nullable=False),
        sa.Column("species_id", sa.Integer, sa.ForeignKey("species.id"), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("plants")
    op.drop_table("species")
