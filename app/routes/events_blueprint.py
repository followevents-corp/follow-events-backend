from flask import Blueprint

from app.controllers import events_controller

bp = Blueprint("user", __name__, url_prefix="/events")

bp.get("")(events_controller.get_events)
bp.get("<str:events_id>")(events_controller.get_by_id_event)
bp.post("")(events_controller.create_event)
bp.patch("<str:events_id>")(events_controller.update_event)
bp.delete("<str:events_id>")(events_controller.del_event)