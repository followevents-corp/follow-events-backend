from datetime import datetime as dt
from http import HTTPStatus

from app.configs.database import db
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    MissingAttributeError,
)
from app.models.events_model import Events
from app.models.giveaway_model import Giveaway
from app.services.general_services import (
    check_id_validation,
    check_keys,
    check_keys_type,
    incoming_values,
    remove_unnecessary_keys,
    save_changes,
)
from flask import jsonify, request
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def create_giveaway(event_id: str):
    data = request.get_json()
    verified_values = incoming_values(data)

    if verified_values:
        return jsonify(verified_values), HTTPStatus.BAD_REQUEST

    try:
        valid_keys = ["name", "description", "award", "award_picture"]

        valid_key_types = {
            "name": str,
            "description": str,
            "award": str,
            "award_picture": str,
        }

        verified_key = check_keys(data, valid_keys)

        check_keys_type(verified_key, valid_key_types)

    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    session: Session = db.session
    event: Query = (
        session.query(Events).select_from(Events).filter(Events.id == event_id).first()
    )

    evt_date = dt.strptime(event.event_date, "%a, %d %b %Y %H:%M:%S %Z")
    if evt_date < dt.utcnow():
        return {"Error": f"Event {event.name} already happened"}, HTTPStatus.BAD_REQUEST

    verified_key["event_id"] = event_id

    new_giveaway = Giveaway(**verified_key)

    save_changes(new_giveaway)

    return jsonify(new_giveaway), HTTPStatus.CREATED


def get_giveaway(event_id: str):
    session: Session = db.session

    giveaways: Query = (
        session.query(Giveaway)
        .select_from(Events)
        .join(Giveaway)
        .filter(Events.id == event_id)
        .all()
    )

    return jsonify(giveaways), HTTPStatus.OK


def update_giveaway(giveaway_id, event_id):

    try:
        check_id_validation(giveaway_id, Giveaway)
    except InvalidIdError as e:
        return e.response, e.status_code

    data = request.get_json()

    verified_values = incoming_values(data)

    if verified_values:
        return jsonify(verified_values), HTTPStatus.BAD_REQUEST

    try:
        valid_keys = ["name", "description", "award", "award_picture", "active"]

        valid_key_types = {
            "name": str,
            "description": str,
            "award": str,
            "award_picture": str,
            "active": bool,
        }

        verified_key = remove_unnecessary_keys(data, valid_keys)[0]
        if not verified_key:
            return {"error": "No data to update"}, HTTPStatus.BAD_REQUEST

        check_keys_type(verified_key, valid_key_types)

    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    session: Session = db.session

    giveaway: Query = (
        session.query(Giveaway)
        .select_from(Events)
        .join(Giveaway)
        .filter(Events.id == event_id, Giveaway.id == giveaway_id)
        .first()
    )

    for key, value in verified_key.items():
        setattr(giveaway, key, value)

    session.add(giveaway)
    session.commit()

    return jsonify(giveaway), HTTPStatus.OK


def delete_giveaway(event_id, giveaway_id):
    session: Session = db.session

    try:
        check_id_validation(giveaway_id, Giveaway)
    except InvalidIdError as e:
        return e.response, e.status_code

    del_giveaway: Query = (
        session.query(Giveaway)
        .select_from(Events)
        .join(Giveaway)
        .filter(Events.id == event_id, Giveaway.id == giveaway_id)
        .first()
    )

    session.delete(del_giveaway)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
