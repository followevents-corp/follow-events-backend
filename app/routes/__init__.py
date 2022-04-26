from flask import Flask

from app.routes.events_blueprint import bp as bp_events
from app.routes.users_blueprint import bp as bp_users
from app.routes.comments_blueprint import bp as bp_comments
from app.routes.login_blueprint import bp as bp_login


def init_app(app: Flask):
    app.register_blueprint(bp_events)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_comments)
    app.register_blueprint(bp_login)
