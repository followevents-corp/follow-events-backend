from dataclasses import asdict
from http import HTTPStatus
from multiprocessing import Event

from flask import jsonify, request
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    MissingAttributeError,
)
from app.exceptions.user_exceptions import NotLoggedUserError
from app.models.events_model import Events
from app.models.schedule_model import Schedule
from app.models.user_model import User
from app.services.events_services import get_additonal_information_of_event
from app.services.general_services import check_id_validation, check_if_the_user_owner, check_keys, check_keys_type, incoming_values, save_changes
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_schedule(user_id):
    key = {'event_id': str}
    data = request.get_json()
    session: Session = db.session

    try:
        verified_key = check_keys(data, ["event_id"])
        check_id_validation(user_id, User)
        check_keys_type(verified_key, key)
        check_id_validation(data["event_id"], Events)
        if not get_jwt_identity() == user_id:
            return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        incoming_error = incoming_values(verified_key)

        if incoming_error:
            return incoming_error, HTTPStatus.BAD_REQUEST

    except InvalidIdError as e:
        return e.response, e.status_code
    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    event_id = verified_key.get("event_id")

    existing_schedule = (
        session.query(Schedule).filter_by(
            user_id=user_id, event_id=event_id).first()
    )

    if existing_schedule:
        return {"error": "Event already added to user's schedule"}, HTTPStatus.CONFLICT

    verified_key.update({"user_id": user_id})
    new_schedule = Schedule(**verified_key)

    save_changes(new_schedule)

    return (
        {"message": "Event added to calendar."},
        HTTPStatus.CREATED,
    )


@jwt_required()
def get_schedule(user_id):
    session: Session = db.session
    try:
        check_id_validation(user_id, Schedule)
        if not get_jwt_identity() == user_id:
            return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
    except InvalidIdError as e:
        return e.response, e.status_code

    scheduled_events_users = (
        session.query(Events)
        .select_from(Events)
        .join(Schedule)
        .filter(Schedule.user_id == user_id)
        .all()
    )

    dict_events = [asdict(event) for event in scheduled_events_users]
    scheduled_events = [
        get_additonal_information_of_event(event) for event in dict_events
    ]

    return jsonify(scheduled_events), HTTPStatus.OK


@jwt_required()
def delete_schedule(user_id, event_id):
    session: Session = db.session

    try:
        check_id_validation(user_id, User)
        check_id_validation(event_id, Events)

        schedule_to_delete = (
            session.query(Schedule).filter_by(
                user_id=user_id, event_id=event_id).first()
        )

        if not schedule_to_delete:
            return {"error": "Schedule not found"}, HTTPStatus.NOT_FOUND

        check_if_the_user_owner(Schedule, event_id)
    except InvalidIdError as e:
        return e.response, e.status_code
    except NotLoggedUserError as e:
        return e.response, e.status_code

    session.delete(schedule_to_delete)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
