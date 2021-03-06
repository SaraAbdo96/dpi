"""changing database

Revision ID: 89df3d9ed697
Revises: 1e9e89155fc1
Create Date: 2020-08-06 15:58:45.464603

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '89df3d9ed697'
down_revision = '1e9e89155fc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('top_talkers', 'dst_ip',
               existing_type=mysql.VARCHAR(length=1000),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('top_talkers', 'src_ip',
               existing_type=mysql.VARCHAR(length=1000),
               type_=sa.String(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('top_talkers', 'src_ip',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=1000),
               existing_nullable=True)
    op.alter_column('top_talkers', 'dst_ip',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###
