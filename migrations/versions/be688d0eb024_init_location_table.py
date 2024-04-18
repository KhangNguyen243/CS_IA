"""Init Location Table

Revision ID: be688d0eb024
Revises: a156607ceb5c
Create Date: 2024-04-18 19:48:40.783627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be688d0eb024'
down_revision = 'a156607ceb5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('ID_Location', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('street', sa.String(length=20), nullable=False),
    sa.Column('ward', sa.String(length=20), nullable=False),
    sa.Column('district', sa.String(length=20), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('principal', sa.String(length=20), nullable=False),
    sa.Column('telephone', sa.Integer(), nullable=False),
    sa.Column('location_type', sa.String(length=10), nullable=False),
    sa.Column('group', sa.String(length=10), nullable=False),
    sa.Column('NumClassTotal', sa.Integer(), nullable=False),
    sa.Column('NumF1', sa.Integer(), nullable=False),
    sa.Column('NumF2', sa.Integer(), nullable=False),
    sa.Column('NumF3', sa.Integer(), nullable=False),
    sa.Column('NumInfant', sa.Integer(), nullable=False),
    sa.Column('office', sa.Boolean(), nullable=False),
    sa.Column('extra', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('ID_Location'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locations')
    # ### end Alembic commands ###
