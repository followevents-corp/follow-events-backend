from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    # importar Giveaway model
    from app.models.categories_events_table import events_categories
    # importar Events model
    from app.models.categories_model import Categories
    from app.models.comment_model import Comment
    from app.models.schedule_table import schedule_table
    from app.models.user_model import User
    from app.models.users_giveaway_model import users_giveaway
