from flask import Blueprint
from app.controllers.events_controller import create_events

bp = Blueprint("user", __name__, url_prefix="/events")

bp.post("")(create_events)

