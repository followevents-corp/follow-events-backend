from flask import Blueprint
from app.controllers import comment_controller

bp = Blueprint('comments', __name__, url_prefix='/events')

bp.post('/<event_id>/comments')(comment_controller.create_comment)
bp.get('/<event_id>/comments')(comment_controller.get_comment)
bp.patch('/comments/<comment_id>')(comment_controller.update_comment)
bp.delete('/comments/<comment_id>')(comment_controller.delete_comment)
