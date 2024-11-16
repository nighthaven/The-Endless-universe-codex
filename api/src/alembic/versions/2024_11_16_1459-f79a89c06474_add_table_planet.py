"""add_table_planet

Revision ID: f79a89c06474
Revises: 2b49c23f8ba0
Create Date: 2024-11-16 14:59:59.156360

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = "f79a89c06474"
down_revision: Union[str, None] = "2b49c23f8ba0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "planet",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("home_planet_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        "fk_factions_descriptions_home_planet",
        "factions_descriptions",
        "planet",
        ["home_planet_id"],
        ["id"],
    )
    op.drop_column("factions_descriptions", "home_planet")


def downgrade() -> None:
    conn = op.get_bind()
    inspector = inspect(conn)
    constraints = [
        fk["name"] for fk in inspector.get_foreign_keys("factions_descriptions")
    ]
    op.add_column(
        "factions_descriptions",
        sa.Column("home_planet", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    if "fk_factions_descriptions_home_planet" in constraints:
        op.drop_constraint(
            "fk_factions_descriptions_home_planet",
            "factions_descriptions",
            type_="foreignkey",
        )
    op.drop_column("factions_descriptions", "home_planet_id")
    tables = inspector.get_table_names()
    if "planet" in tables:
        op.drop_table("planet")
