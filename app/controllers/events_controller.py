from dataclasses import asdict
from http import HTTPStatus
import json

from flask import jsonify, request
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.request_data_exceptions import AttributeTypeError, MissingAttributeError
from app.exceptions.user_exceptions import NotLoggedUser
from app.models.events_model import Events
from app.models.user_model import User

from app.exceptions.invalid_id_exception import InvalidIdError
from app.services.general_services import check_id_validation, check_if_the_user_owner, check_keys, check_keys_type, remove_unnecessary_keys, save_changes
from app.services.events_services import get_additonal_information_of_event

# def create_events():
#     files = request.files

#     for obj in files:
#         if obj == "file":
#             event = Events(name = "EVENtooosssteste", event_date = "01/12/2023", link = files[obj])
#             current_app.db.session.add(event)
#             current_app.db.session.commit()
#         return jsonify(event), HTTPStatus.CREATED
#     return {},HTTPStatus.OK


def create_event():
    pass


def get_events():
    session: Session = db.session

    events = session.query(Events).all()

    serialized_events = [asdict(event) for event in events]

    for event in serialized_events:
        event = get_additonal_information_of_event(event)

    return jsonify(serialized_events), HTTPStatus.OK


def get_event_by_id(user_id):
    try:
        check_id_validation(user_id, User)
    except InvalidIdError as err:
        return err.response, err.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    session: Session = db.session

    event = session.query(Events).filter_by(creator_id=user_id).first()

    if not event:
        return {"error": "Event not found"}, HTTPStatus.NOT_FOUND

    serialized_event = asdict(event)

    result = get_additonal_information_of_event(serialized_event)

    return jsonify(result), HTTPStatus.OK


def update_event(event_id):
    keys = ["name", "description", "event_link", "categories"]
    values = {"name": str, "description": str,
              "event_link": str, "categories": list}

    try:
        data = remove_unnecessary_keys(json.loads(request.form["file"]), keys)[0]
        if not data:
            return {"error": "No data to update"}, HTTPStatus.BAD_REQUEST
        check_id_validation(event_id, Events)
        check_if_the_user_owner(Events, event_id)
        check_keys_type(data, values)
    except InvalidIdError as err:
        return err.response, err.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code
    except NotLoggedUser as e:
        return e.response, e.status_code
    except MissingAttributeError as e:
        return e.response, e.status_code
    
    session: Session = db.session

    event = session.query(Events).filter_by(id=event_id).first()

    serialized_event = asdict(event)

    for key, value in data.items():
        setattr(event, key, value)

    save_changes(event)
   

    event = get_additonal_information_of_event(serialized_event)

    return jsonify(event), HTTPStatus.OK


def delete_event(event_id):
    try:
        check_id_validation(event_id, Events)
    except InvalidIdError as err:
        return err.response, err.status_code

    session: Session = db.session

    event = session.query(Events).filter_by(id=event_id).first()

    session.delete(event)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
