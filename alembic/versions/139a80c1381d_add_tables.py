"""Add tables

Revision ID: 139a80c1381d
Revises: 
Create Date: 2020-07-12 11:34:20.503203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '139a80c1381d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('htt_prequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('method', sa.String(length=10), nullable=True),
    sa.Column('host', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=1000), nullable=True),
    sa.Column('version', sa.String(length=10), nullable=True),
    sa.Column('response_code_desc', sa.String(length=100), nullable=True),
    sa.Column('response_code', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('icmp_packet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('checksum_status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tcp_packet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_index', sa.Integer(), nullable=True),
    sa.Column('srcPort', sa.Integer(), nullable=True),
    sa.Column('dstPort', sa.Integer(), nullable=True),
    sa.Column('srcIP', sa.String(length=15), nullable=True),
    sa.Column('dstIP', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tcp_stream',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_index', sa.Integer(), nullable=True),
    sa.Column('value', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('top_talkers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src_ip', sa.String(length=15), nullable=True),
    sa.Column('dest_ip', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('udp_packet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('srcPort', sa.Integer(), nullable=True),
    sa.Column('dstPort', sa.Integer(), nullable=True),
    sa.Column('srcIP', sa.String(length=15), nullable=True),
    sa.Column('dstIP', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('udp_packet')
    op.drop_table('top_talkers')
    op.drop_table('tcp_stream')
    op.drop_table('tcp_packet')
    op.drop_table('icmp_packet')
    op.drop_table('htt_prequest')
    # ### end Alembic commands ###
