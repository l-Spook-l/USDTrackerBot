"""initial

Revision ID: 4c897344d9a6
Revises: 
Create Date: 2024-05-07 12:04:25.393961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c897344d9a6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency_rate_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Currency_pair', sa.String(), nullable=False),
    sa.Column('Exchange_rate', sa.Float(), nullable=False),
    sa.Column('Timestamp', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currency_rate_table')
    # ### end Alembic commands ###
