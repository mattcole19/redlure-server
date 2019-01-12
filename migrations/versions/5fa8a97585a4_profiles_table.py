"""profiles table

Revision ID: 5fa8a97585a4
Revises: 64c858a2a629
Create Date: 2019-01-10 09:39:34.582366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa8a97585a4'
down_revision = '64c858a2a629'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('from_address', sa.String(length=64), nullable=True),
    sa.Column('smtp_host', sa.String(length=64), nullable=True),
    sa.Column('smtp_port', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('tls', sa.Boolean(), nullable=False),
    sa.Column('ssl', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###
