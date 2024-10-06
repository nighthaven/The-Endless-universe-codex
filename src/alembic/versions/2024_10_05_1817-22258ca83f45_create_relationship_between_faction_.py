"""create_relationship_between_faction_factiondescription_and_media

Revision ID: 22258ca83f45
Revises: 0d88a007eb8e
Create Date: 2024-10-05 18:17:34.407891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22258ca83f45'
down_revision: Union[str, None] = '0d88a007eb8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('factions_descriptions', sa.Column('faction_id', sa.Integer(), nullable=False))
    op.add_column('factions_descriptions', sa.Column('media_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'factions_descriptions', 'factions', ['faction_id'], ['id'])
    op.create_foreign_key(None, 'factions_descriptions', 'media', ['media_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'factions_descriptions', type_='foreignkey')
    op.drop_constraint(None, 'factions_descriptions', type_='foreignkey')
    op.drop_column('factions_descriptions', 'media_id')
    op.drop_column('factions_descriptions', 'faction_id')
    # ### end Alembic commands ###
