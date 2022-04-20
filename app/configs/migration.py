from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    Migrate(app=app, db=app.db, compare_type=True)
