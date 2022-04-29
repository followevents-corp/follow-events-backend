from flask import Blueprint

from app.controllers import schedule_controller

bp = Blueprint("schedule", __name__, url_prefix="/users/<user_id>/schedule")

bp.post("")(schedule_controller.create_schedule)
bp.get("")(schedule_controller.get_schedule)
bp.delete("/<event_id>")(schedule_controller.delete_schedule)
