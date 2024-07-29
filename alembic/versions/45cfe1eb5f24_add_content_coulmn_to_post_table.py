"""add content coulmn to post table

Revision ID: 45cfe1eb5f24
Revises: 0150cf465d4a
Create Date: 2024-07-29 21:11:44.973443

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '45cfe1eb5f24'
down_revision: Union[str, None] = '0150cf465d4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
