"""database schema update:  added Styles table

Revision ID: e8a5890deb33
Revises: 97eb43767c8a
Create Date: 2021-07-05 23:30:31.685478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8a5890deb33'
down_revision = '97eb43767c8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('style',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('major', sa.String(length=25), nullable=False),
    sa.Column('sub_styles', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('major')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('style')
    # ### end Alembic commands ###
