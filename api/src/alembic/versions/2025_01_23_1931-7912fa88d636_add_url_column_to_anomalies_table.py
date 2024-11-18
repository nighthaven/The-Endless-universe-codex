"""add_url_column_to_anomalies_table

Revision ID: 7912fa88d636
Revises: f79a89c06474
Create Date: 2025-01-23 19:31:18.320026

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7912fa88d636"
down_revision: Union[str, None] = "f79a89c06474"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("anomaly", sa.Column("url", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("anomaly", "url")
