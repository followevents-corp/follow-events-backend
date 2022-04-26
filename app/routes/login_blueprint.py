from flask import Blueprint

from app.controllers.login_controller import login_user

bp = Blueprint("login", __name__, url_prefix="/login")

bp.post("")(login_user)
