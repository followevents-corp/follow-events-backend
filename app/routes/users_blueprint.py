from flask import Blueprint
from app.controllers.users_controller import create_user, get_user, update_user, delete_user

bp = Blueprint('bp_users', __name__, url_prefix='/users')

bp.post('')(create_user)
bp.get('/<int:user_id>')(get_user)
bp.patch('/<int:user_id>')(update_user)
bp.delete('/<int:user_id>')(delete_user)