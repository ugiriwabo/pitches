"""Initial Migration

Revision ID: c471a34aa953
Revises: 9b95d2cc37ee
Create Date: 2019-03-03 09:06:31.592801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c471a34aa953'
down_revision = '9b95d2cc37ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitch_categories')
    op.drop_column('pitch', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_table('pitch_categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name_of_category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('category_description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pitch_categories_pkey')
    )
    # ### end Alembic commands ###