"""changing

Revision ID: 7beba35db512
Revises: c7b3cc68fb34
Create Date: 2020-07-29 15:22:56.086937

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7beba35db512'
down_revision = 'c7b3cc68fb34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('top_talkers', 'src_ip',
               existing_type=mysql.VARCHAR(length=15),
               type_=sa.String(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('top_talkers', 'src_ip',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=15),
               existing_nullable=True)
    # ### end Alembic commands ###
