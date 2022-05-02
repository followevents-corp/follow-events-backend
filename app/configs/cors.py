from flask import Flask
from flask_cors import CORS


def init(app: Flask):
    cors = CORS(app)
