from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.categories_events_table import events_categories
    from app.models.categories_model import Categories
    from app.models.comment_model import Comment
    from app.models.events_model import Events
    from app.models.giveaway_model import Giveaway
    from app.models.schedule_model import Schedule
    from app.models.user_model import User
    from app.models.users_giveaway_model import users_giveaway
