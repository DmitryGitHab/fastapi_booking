"""add users, bookings, rooms tables

Revision ID: 14483d867205
Revises: 221bd5abef9b
Create Date: 2023-12-10 21:08:25.629060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '14483d867205'
down_revision: Union[str, None] = '221bd5abef9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('services', sa.JSON(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_from', sa.Date(), nullable=False),
    sa.Column('date_to', sa.Date(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('total_cost', sa.Integer(), sa.Computed('(date_to - date_from) * price', ), nullable=False),
    sa.Column('total_days', sa.Integer(), sa.Computed('date_to - date_from', ), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('hotels', sa.Column('rooms_quantity', sa.Integer(), nullable=False))
    op.alter_column('hotels', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('hotels', 'image_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('hotels', 'room_quantity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('room_quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.alter_column('hotels', 'image_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('hotels', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.drop_column('hotels', 'rooms_quantity')
    op.drop_table('bookings')
    op.drop_table('rooms')
    op.drop_table('users')
    # ### end Alembic commands ###