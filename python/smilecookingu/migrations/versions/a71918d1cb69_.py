"""empty message

Revision ID: a71918d1cb69
Revises: c887a8292c07
Create Date: 2022-08-03 17:07:34.454926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a71918d1cb69'
down_revision = 'c887a8292c07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('cover_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'cover_image')
    # ### end Alembic commands ###
