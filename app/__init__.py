from flask import Flask

from app import routes
from app.configs import database, env_configs, jwt, migration


def create_app() -> Flask:
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init(app)
    routes.init_app(app)

    return app
