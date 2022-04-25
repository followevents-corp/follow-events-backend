from flask import Flask
from app.routes.events_blueprint import bp as bp_events

def init_app(app: Flask):
    app.register_blueprint(bp_events)
