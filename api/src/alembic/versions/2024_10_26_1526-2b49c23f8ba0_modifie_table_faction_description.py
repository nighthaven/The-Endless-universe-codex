"""modifie_table_faction_description

Revision ID: 2b49c23f8ba0
Revises: 95f98a0a51e3
Create Date: 2024-10-26 15:26:25.740682

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2b49c23f8ba0"
down_revision: Union[str, None] = "95f98a0a51e3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "factions_descriptions", sa.Column("description", sa.Text(), nullable=False)
    )
    op.add_column(
        "factions_descriptions", sa.Column("image_url", sa.String(), nullable=False)
    )
    op.add_column(
        "factions_descriptions", sa.Column("government", sa.String(), nullable=True)
    )
    op.add_column(
        "factions_descriptions", sa.Column("ideology", sa.String(), nullable=True)
    )
    op.add_column(
        "factions_descriptions", sa.Column("home_planet", sa.String(), nullable=True)
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("affinity", sa.ARRAY(sa.String()), nullable=True),
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("populations", sa.ARRAY(sa.String()), nullable=True),
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("traits", sa.ARRAY(sa.String()), nullable=True),
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("starting_technology", sa.ARRAY(sa.String()), nullable=True),
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("units", sa.ARRAY(sa.String()), nullable=True),
    )
    op.add_column(
        "factions_descriptions",
        sa.Column("heroes", sa.ARRAY(sa.String()), nullable=True),
    )
    op.add_column(
        "factions_descriptions", sa.Column("major", sa.Boolean(), nullable=False)
    )
    op.drop_column("factions_descriptions", "size")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "factions_descriptions",
        sa.Column(
            "size",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_column("factions_descriptions", "major")
    op.drop_column("factions_descriptions", "heroes")
    op.drop_column("factions_descriptions", "units")
    op.drop_column("factions_descriptions", "starting_technology")
    op.drop_column("factions_descriptions", "traits")
    op.drop_column("factions_descriptions", "populations")
    op.drop_column("factions_descriptions", "affinity")
    op.drop_column("factions_descriptions", "home_planet")
    op.drop_column("factions_descriptions", "ideology")
    op.drop_column("factions_descriptions", "government")
    op.drop_column("factions_descriptions", "image_url")
    op.drop_column("factions_descriptions", "description")
    # ### end Alembic commands ###