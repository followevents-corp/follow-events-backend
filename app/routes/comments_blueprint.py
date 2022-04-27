from flask import Blueprint
from app.controllers import comment_controller

bp = Blueprint("comments", __name__, url_prefix="/events/<event_id>/comments")

bp.post("")(comment_controller.create_comment)
bp.get("")(comment_controller.get_comment)
bp.patch("/<comment_id>")(comment_controller.update_comment)
bp.delete("/<comment_id>")(comment_controller.delete_comment)
