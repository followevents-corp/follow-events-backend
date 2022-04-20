from flask import Flask
from flask_jwt_extended import JWTManager


def init(app: Flask):
    JWTManager(app)
