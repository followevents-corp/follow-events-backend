from http import HTTPStatus
from flask import Flask

from app import commands, routes
from app.configs import database, env_configs, jwt, migration, cors


def create_app() -> Flask:
    app = Flask(__name__)

    cors.init(app)
    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init(app)
    commands.init_app(app)
    routes.init_app(app)

    @app.errorhandler(413)
    def error413(_):
        return {
            "error": "The suported file is until 10MB"
        }, HTTPStatus.REQUEST_ENTITY_TOO_LARGE

    return app
