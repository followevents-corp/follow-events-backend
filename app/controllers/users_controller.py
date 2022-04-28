from http import HTTPStatus
from flask import jsonify, request, url_for
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError, DataError
from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    MissingAttributeError,
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions.user_exceptions import EmailFormatError
from app.configs.database import db
from app.models.user_model import User
from app.services.general_services import check_keys, check_keys_type
from app.services.verify_values import incoming_values

session: Session = db.session


def create_user():
    data = request.get_json()

    empty_values = incoming_values(data)

    if empty_values:
        return empty_values, HTTPStatus.BAD_REQUEST

    valid_keys = ["username", "name", "email", "password"]
    try:
        new_data = check_keys(data, valid_keys)
    except MissingAttributeError as m:
        return m.response, HTTPStatus.BAD_REQUEST

    keys_types = {"username": str, "name": str, "email": str, "password": str}
    try:
        check_keys_type(new_data, keys_types)
    except AttributeTypeError as e:
        return e.response ,HTTPStatus.BAD_REQUEST

    try:
        new_user = User(**new_data)
    except EmailFormatError:
        return {
            "error": f'Email format not acceptable: {new_data["email"]}, try ex.: your_mail@your_provider.com'
        }, HTTPStatus.BAD_REQUEST

    try:
        session.add(new_user)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        error = str(e)

        if "Key (email)" in error:
            return {"error": "Email already exists."}, HTTPStatus.CONFLICT
        return {"error": "Username already exists."}, HTTPStatus.CONFLICT
    except DataError as e:
        session.rollback()
        error = str(e)
        if "varying(30)" in error:
            return {
                "error": "Username has to be 6 to 30 characters."
            }, HTTPStatus.BAD_REQUEST
        return {
            "error": "Name has to be less than 100 characters. If your name is greater than that, try abbreviate it. :D"
        }, HTTPStatus.BAD_REQUEST

    return jsonify(new_user), HTTPStatus.CREATED

@jwt_required()
def get_user(user_id):

    current_user = get_jwt_identity()
    
    user: Query = (
        session.query(User)
        .select_from(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return {'error': 'Id not found in database.'}, HTTPStatus.NOT_FOUND

    if user.id != current_user:
        return {'error': 'Unauthorized.'}, HTTPStatus.UNAUTHORIZED
    
    schedule_url = url_for("schedule.get_schedule", user_id=user.id)
    events_url = url_for("user.get_event_by_id", user_id=user.id)

    return {
        "id": user.id,
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "profile_picture": user.profile_picture,
        "creator": user.creator,
        "schedule": f"{request.host_url[:-1]}{schedule_url}",
        "events": f"{request.host_url[:-1]}{events_url}",
    }, HTTPStatus.OK


def update_user(user_id):
    pass


def delete_user(user_id):
    pass
