"""Add creator_id to Auction

Revision ID: e90271175b14
Revises: 134a51dfb6bd
Create Date: 2024-09-25 03:15:29.210138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e90271175b14'
down_revision: Union[str, None] = '134a51dfb6bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auctions', sa.Column('creator_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'auctions', 'users', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'auctions', type_='foreignkey')
    op.drop_column('auctions', 'creator_id')
    # ### end Alembic commands ###
