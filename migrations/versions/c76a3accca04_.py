"""empty message

Revision ID: c76a3accca04
Revises: 
Create Date: 2020-04-03 13:14:49.952840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c76a3accca04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bug',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('domain', sa.String(length=20), nullable=False),
    sa.Column('ip', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=30), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('status_code', sa.Integer(), nullable=False),
    sa.Column('Server', sa.String(length=30), nullable=False),
    sa.Column('bugdetail', sa.Text(), nullable=False),
    sa.Column('response', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('log',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ip', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('log')
    op.drop_table('bug')
    # ### end Alembic commands ###