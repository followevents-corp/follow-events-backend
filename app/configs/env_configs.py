from os import getenv

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = bool(
        getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    )
    app.config["JWT_SECRET_KEY"] = getenv("SECRET_KEY")
    app.config["JSON_SORT_KEYS"] = bool(getenv("JSON_SORT_KEYS"))
    app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 10
