from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import (AttributeTypeError,
                                                    MissingAttributeError)
from app.models.events_model import Events
from app.models.schedule_model import Schedule
from app.models.user_model import User
from app.services.general_services import check_keys, check_keys_type
from app.services.invalid_id_services import check_id_validation
from app.services.verify_values import incoming_values


def create_schedule(user_id):
    data = request.get_json()

    try:
        check_id_validation(user_id, User)
        check_id_validation(data["event_id"], Events)
    except InvalidIdError as e:
        return e.response, e.status_code

    session: Session = db.session

    try:
        new_data = check_keys(data, ["event_id"])
        check_keys_type(new_data, {"event_id": str})
        incoming_error = incoming_values(new_data)

        if incoming_error:
            return incoming_error, 400

    except MissingAttributeError as e:
        return e.response, e.status_code

    except AttributeTypeError as e:
        return e.response, e.status_code

    event_id = new_data.get("event_id")

    existing_schedule = (
        session.query(Schedule).filter_by(user_id=user_id, event_id=event_id).first()
    )

    if existing_schedule:
        return {"error": "Event already added to user's schedule"}, HTTPStatus.CONFLICT

    new_data.update({"user_id": user_id})
    new_schedule = Schedule(**new_data)

    session.add(new_schedule)
    session.commit()

    return (
        {"message": "Event added to calendar."},
        HTTPStatus.CREATED,
    )


def get_schedule():
    pass


def delete_schedule(event_id):
    pass
