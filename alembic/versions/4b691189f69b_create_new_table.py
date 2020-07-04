"""create new table

Revision ID: 4b691189f69b
Revises: 
Create Date: 2020-07-03 22:55:06.976312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b691189f69b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('top_talkers',
                    sa.Column('id',sa.Integer,primary_key=True),
                    sa.Column('source Ip',sa.String(15)),
                    sa.Column('dest Ip',sa.String(15))
    )


def downgrade():
    op.drop_table('top_talkers')
