from http import HTTPStatus
from pprint import pprint
import json

from flask import jsonify, request
from app.exceptions.category_exceptions import CategoryTypeError
from app.exceptions.request_data_exceptions import AttributeTypeError, FileTypeError, MissingAttributeError

from app.models.events_model import Events
from app.models.user_model import User
from app.models.categories_model import Categories
from app.models.categories_events_model import EventsCategories
from app.services.general_services import check_keys, check_keys_type, incoming_values, save_changes
from app.services.categories_services import create_categories
from dataclasses import asdict

from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.user_exceptions import NotLoggedUser


from app.exceptions.invalid_id_exception import InvalidIdError

from app.services.events_services import get_additonal_information_of_event, link_categories_to_event
from app.services.general_services import check_id_validation, check_if_the_user_owner
from flask_jwt_extended import jwt_required


@jwt_required()
def create_event():
    try:
        dict = {"name": str, "description": str, "event_date": str, "event_link": str, "creator_id": str, "categories": list}

        files = request.files
        file = files["file"]
        data = json.loads(request.form["data"])

        new_data = check_keys(data, [*dict.keys()])
        check_keys_type(new_data, dict, file)

        categories = new_data["categories"]

        new_data.pop("categories")
    
        
        verify_values = incoming_values(new_data)

        if verify_values:
            return jsonify(verify_values), HTTPStatus.BAD_REQUEST

        create_categories(categories)

        event = Events(**new_data,  link = file)
        save_changes(event)
  
        link_categories_to_event(categories, event)

        new_event = get_additonal_information_of_event(asdict(event))

    except FileTypeError as e:
        return e.response, e.status_code
    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code
    except CategoryTypeError as e:
        return e.response, e.status_code
    return jsonify(new_event), HTTPStatus.CREATED



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

    session: Session = db.session

    event = session.query(Events).filter_by(creator_id=user_id).first()

    if not event:
        return {"error": "Event not found"}, HTTPStatus.NOT_FOUND

    serialized_event = asdict(event)

    result = get_additonal_information_of_event(serialized_event)

    return jsonify(result), HTTPStatus.OK

@jwt_required()
def update_event(event_id):
    pass


def delete_event(event_id):
    try:
        check_if_the_user_owner(Events, event_id)
        check_id_validation(event_id, Events)
    except InvalidIdError as err:
        return err.response, err.status_code
    except NotLoggedUser as err:
        return err.response, err.status_code
    session: Session = db.session

    event = session.query(Events).filter_by(id=event_id).first()

    session.delete(event)
    session.commit()

    return '', HTTPStatus.NO_CONTENT
