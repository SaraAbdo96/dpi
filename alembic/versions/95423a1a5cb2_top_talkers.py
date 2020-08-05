"""top_talkers

Revision ID: 95423a1a5cb2
Revises: 21e0ef0dc429
Create Date: 2020-08-05 18:49:35.901030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95423a1a5cb2'
down_revision = '21e0ef0dc429'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('top_talkers', sa.Column('dst_ip', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('top_talkers', 'dst_ip')
    # ### end Alembic commands ###
