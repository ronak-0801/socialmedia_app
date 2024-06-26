"""v_04

Revision ID: f5333cec7e66
Revises: a19ce9e4838f
Create Date: 2024-04-24 18:32:45.603576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5333cec7e66'
down_revision: Union[str, None] = 'a19ce9e4838f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Likesofposts', 'is_deleted')
    op.drop_column('Likesofposts', 'is_active')
    op.drop_column('follower', 'is_deleted')
    op.drop_column('follower', 'is_active')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('follower', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('follower', sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Likesofposts', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Likesofposts', sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
