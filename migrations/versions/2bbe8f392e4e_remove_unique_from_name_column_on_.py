"""remove unique from name column on events table

Revision ID: 2bbe8f392e4e
Revises: 15659781d271
Create Date: 2022-04-29 00:17:59.128334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bbe8f392e4e'
down_revision = '15659781d271'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('events_name_key', 'events', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('events_name_key', 'events', ['name'])
    # ### end Alembic commands ###
