"""create_table_media_and_faction

Revision ID: c9d6dac1cb38
Revises: de90e472558c
Create Date: 2024-10-02 19:05:13.287032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9d6dac1cb38'
down_revision: Union[str, None] = 'de90e472558c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('factions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'media',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Enum('ENDLESS_SPACE', 'ENDLESS_SPACE_2', 'ENDLESS_LEGEND', 'DUNGEON_OF_THE_ENDLESS', 'ENDLESS_DUNGEON', name='medianame'), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_media_id'), 'media', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_media_id'), table_name='media')
    op.drop_table('media')
    op.drop_table('factions')
    # ### end Alembic commands ###