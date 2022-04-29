from flask import Blueprint

from app.controllers import events_controller

bp = Blueprint("events", __name__, url_prefix="/events")

bp.get("")(events_controller.get_events)
bp.get("/<user_id>")(events_controller.get_event_by_id)
bp.post("")(events_controller.create_event)
bp.patch("/<event_id>")(events_controller.update_event)
bp.delete("/<event_id>")(events_controller.delete_event)
