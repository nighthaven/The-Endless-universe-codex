"""create_table_anomaly

Revision ID: 852aa53f1355
Revises: 22258ca83f45
Create Date: 2024-10-17 23:31:07.082966

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "852aa53f1355"
down_revision: Union[str, None] = "22258ca83f45"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "anomaly",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("image", sa.String(), nullable=False),
        sa.Column("media_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["media_id"],
            ["media.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_anomaly_id"), "anomaly", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_anomaly_id"), table_name="anomaly")
    op.drop_table("anomaly")
    # ### end Alembic commands ###
