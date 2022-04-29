from datetime import timedelta
from http import HTTPStatus

from flask import request, url_for
from flask_jwt_extended import create_access_token

from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    MissingAttributeError,
)
from app.models.user_model import User
from app.services.general_services import check_keys, check_keys_type


def login_user():
    user_data = request.get_json()

    valid_keys = ["email", "password"]
    try:
        new_data = check_keys(user_data, valid_keys)
    except MissingAttributeError as m:
        return m.response, HTTPStatus.BAD_REQUEST

    try:
        check_keys_type(new_data, {"email": str, "password": str})
    except AttributeTypeError as e:
        return e.response, HTTPStatus.BAD_REQUEST

    found_user = User.query.filter_by(email=new_data["email"]).first()
    if not found_user or not found_user.check_password(new_data["password"]):
        return {"error": "Invalid email or password."}, HTTPStatus.NOT_FOUND

    access_token = create_access_token(identity=found_user.id, expires_delta=timedelta(hours=1))
    schedule_url = url_for("schedule.get_schedule", user_id=found_user.id)
    events_url = url_for("events.get_event_by_id", user_id=found_user.id)

    return {
        "id": found_user.id,
        "name": found_user.name,
        "username": found_user.username,
        "email": found_user.email,
        "profile_picture": found_user.profile_picture,
        "creator": found_user.creator,
        "schedule": f"{request.host_url[:-1]}{schedule_url}",
        "events": f"{request.host_url[:-1]}{events_url}",
        "access_token": access_token,
    }, HTTPStatus.OK
