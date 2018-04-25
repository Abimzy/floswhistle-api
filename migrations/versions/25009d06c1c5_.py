"""empty message

Revision ID: 25009d06c1c5
Revises: 818b53b95cbd
Create Date: 2018-04-24 21:45:54.283639

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '25009d06c1c5'
down_revision = '818b53b95cbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('whistles', sa.Column('end_date', sa.DateTime(), nullable=True))
    op.add_column('whistles', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.drop_column('whistles', 'shift')
    op.drop_column('whistles', 'report_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('whistles', sa.Column('report_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('whistles', sa.Column('shift', postgresql.ENUM('day', 'night', 'mid', name='shift_type'), autoincrement=False, nullable=False))
    op.drop_column('whistles', 'start_date')
    op.drop_column('whistles', 'end_date')
    # ### end Alembic commands ###