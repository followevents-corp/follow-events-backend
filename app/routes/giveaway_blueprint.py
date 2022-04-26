from app.controllers import giveaway_controller
from flask import Blueprint

bp = Blueprint("giveaway", __name__, url_prefix="/events/<event_id>/giveaway")

bp.post("")(giveaway_controller.create_giveaway)
bp.get("")(giveaway_controller.get_giveaway)
bp.patch("/<giveaway_id>")(giveaway_controller.update_giveaway)
bp.delete("/<giveaway_id>")(giveaway_controller.delete_giveaway)
