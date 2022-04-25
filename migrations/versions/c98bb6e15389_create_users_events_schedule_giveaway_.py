"""create users, events, schedule, giveaway, users_giveaway, comments, categories and events_categories models

Revision ID: c98bb6e15389
Revises: 
Create Date: 2022-04-25 20:50:43.978822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c98bb6e15389'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hash_password', sa.String(length=50), nullable=True),
    sa.Column('profile_picture', sa.String(), nullable=True),
    sa.Column('creator', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('events',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('event_date', sa.String(), nullable=False),
    sa.Column('type_banner', sa.String(), nullable=False),
    sa.Column('link_banner', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('creator_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('comments',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events_categories',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('category_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('giveaway',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('award', sa.String(length=50), nullable=False),
    sa.Column('award_picture', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('events_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['events_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_giveaway',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('giveaway_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['giveaway_id'], ['giveaway.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_giveaway')
    op.drop_table('schedule')
    op.drop_table('giveaway')
    op.drop_table('events_categories')
    op.drop_table('comments')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
