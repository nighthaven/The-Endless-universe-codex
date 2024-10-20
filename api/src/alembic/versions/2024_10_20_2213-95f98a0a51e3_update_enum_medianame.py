"""update_enum_MediaName

Revision ID: 95f98a0a51e3
Revises: a0e7e1b29850
Create Date: 2024-10-20 22:13:42.381792

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '95f98a0a51e3'
down_revision: Union[str, None] = 'a0e7e1b29850'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


type_name = 'medianame'
new_enum_value = 'SHADOW_OF_THE_ENDLESS'


def upgrade():
    op.execute(f"ALTER TYPE {type_name} ADD VALUE '{new_enum_value}'")

def downgrade():
    raise NotImplementedError("Downgrade n'est pas supporté car la suppression d'une valeur ENUM est impossible.")
