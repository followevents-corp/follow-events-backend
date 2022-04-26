from flask import Blueprint

bp = Blueprint('bp_users', __name__, url_prefix='/users')

bp.post('')()
bp.get('/<int:user_id>')()
bp.patch('/<int:user_id>')()
bp.delete('/<int:user_id>')()