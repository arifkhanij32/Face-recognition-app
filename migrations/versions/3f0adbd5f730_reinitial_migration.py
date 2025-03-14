"""Reinitial migration

Revision ID: 3f0adbd5f730
Revises: 
Create Date: 2025-03-11 12:25:38.794364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f0adbd5f730'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('image_data', sa.LargeBinary(), nullable=False),
    sa.Column('encoding', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_detail')
    # ### end Alembic commands ###
