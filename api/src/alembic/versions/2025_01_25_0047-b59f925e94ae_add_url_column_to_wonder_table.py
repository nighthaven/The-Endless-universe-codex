"""add_url_column_to_wonder_table

Revision ID: b59f925e94ae
Revises: 7912fa88d636
Create Date: 2025-01-25 00:47:39.311852

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b59f925e94ae"
down_revision: Union[str, None] = "7912fa88d636"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("wonder", sa.Column("url", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("wonder", "url")
