"""empty message

Revision ID: 421e5d0d4ac6
Revises: 34818f6caae7
Create Date: 2023-07-15 07:13:49.991790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '421e5d0d4ac6'
down_revision = '34818f6caae7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Numeric(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
