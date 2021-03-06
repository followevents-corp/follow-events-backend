import json
from dataclasses import asdict
from http import HTTPStatus
from datetime import datetime as dt

from app.configs.database import db
from app.exceptions.category_exceptions import CategoryTypeError
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    FileTypeError,
    FormatDateError,
    IncorrectKeys,
    InvalidLink,
    MissingAttributeError,
    PastDateError,
)
from app.exceptions.user_exceptions import NotLoggedUserError
from app.models.events_model import Events
from app.models.user_model import User
from app.services.aws_s3 import AWS_S3
from app.services.categories_services import create_categories
from app.services.events_services import (
    check_format_date,
    check_type_of_file,
    delete_link_events_categories,
    get_additonal_information_of_event,
    link_categories_to_event,
)
from app.services.general_services import (
    check_id_validation,
    check_if_the_user_owner,
    check_keys,
    check_keys_type,
    incoming_values,
    require_jwt,
    remove_unnecessary_keys,
    save_changes,
)
from sqlalchemy.orm import Query
from flask import jsonify, request
from sqlalchemy.orm.session import Session
from werkzeug.datastructures import FileStorage
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity


def create_event():

    try:
        files = request.files
        file = files.get("file")
        data = request.form.get("data")
        session: Session = db.session

        require_jwt()

        current_user = get_jwt_identity()

        user: Query = (
            session.query(User)
            .select_from(User)
            .filter(User.id == current_user)
            .first()
        )

        if user.creator is False:
            return {
                "error": "Must be a content creator, to create a event."
            }, HTTPStatus.UNAUTHORIZED

        dict = {
            "name": str,
            "description": str,
            "event_date": str,
            "event_link": str,
            "categories": list,
        }

        request_body = {"data": data, "file": file}
        if data is None:
            request_body.pop("data")

        if file is None:
            request_body.pop("file")

        check_keys(request_body, ["data", "file"])

        data = json.loads(data)
        new_data = check_keys(data, [*dict.keys()])

        check_keys_type(new_data, dict)
        check_type_of_file(file)

        check_format_date(new_data["event_date"])

        formated_event_date = dt.strptime(
            new_data["event_date"], "%a, %d %b %Y %H:%M:%S %Z"
        )
        if formated_event_date < dt.utcnow():
            raise PastDateError

        categories = new_data["categories"]

        new_data.pop("categories")

        verify_values = incoming_values(new_data)

        if verify_values:
            return jsonify(verify_values), HTTPStatus.BAD_REQUEST

        create_categories(categories)

        new_data["creator_id"] = current_user

        event = Events(**new_data, link=file)
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
    except InvalidLink as e:
        return e.response, e.status_code
    except PastDateError as e:
        return {"error": "Event must be in the future"}, e.status_code
    except IntegrityError as e:
        if type(e.orig) is ForeignKeyViolation:
            return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
    except FormatDateError as e:
        return e.response, e.status_code

    return jsonify(new_event), HTTPStatus.CREATED


def get_events():
    session: Session = db.session

    events = session.query(Events).all()

    serialized_events = [asdict(event) for event in events]

    for event in serialized_events:
        event = get_additonal_information_of_event(event)

    return jsonify(serialized_events), HTTPStatus.OK


def get_events_by_id(user_id):
    try:
        check_id_validation(user_id, User)
    except InvalidIdError as err:
        return err.response, err.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    session: Session = db.session

    events = session.query(Events).filter_by(creator_id=user_id).all()

    if not events:
        return {"error": "Event not found"}, HTTPStatus.NOT_FOUND

    result = [get_additonal_information_of_event(asdict(event)) for event in events]

    return jsonify(result), HTTPStatus.OK


def update_event(event_id):
    values = {
        "name": str,
        "description": str,
        "event_date": str,
        "event_link": str,
        "creator_id": str,
        "categories": list,
        "link": FileStorage,
    }
    try:
        data = request.form.get("data") or {}
        file = request.files.get("file")
        check_id_validation(event_id, Events)

        check_if_the_user_owner(Events, event_id)

        session: Session = db.session

        event = session.query(Events).filter_by(id=event_id).first()

        if data:
            data = remove_unnecessary_keys(json.loads(data), [*values.keys()])[0]
            check_keys_type(data, values)
            if not data:
                raise MissingAttributeError([*values.keys()])
        key = ""
        if file:
            data["link"] = file
            key = event.link_banner.split("/")[-1]
            check_type_of_file(file)

        if not data and not file:
            return {"error": "No data to update"}, HTTPStatus.BAD_REQUEST
        
        if data.get("event_date"):
            check_format_date(data["event_date"])
            formated_event_date = dt.strptime(
                data["event_date"], "%a, %d %b %Y %H:%M:%S %Z"
            )
            if formated_event_date < dt.utcnow():
                raise PastDateError

    except FileTypeError as e:
        return e.response, e.status_code
    except InvalidIdError as err:
        return err.response, err.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code
    except NotLoggedUserError as e:
        return e.response, e.status_code
    except MissingAttributeError as e:
        return e.response, e.status_code
    except IncorrectKeys as e:
        return e.response, e.status_code
    except PastDateError as e:
        return {"error": "Event must be in the future"}, e.status_code
    except FormatDateError as e:
        return e.response, e.status_code

    try:
        for key, value in data.items():
            setattr(event, key, value)

        categories = []
        if data.get("categories"):
            categories = data["categories"]
            create_categories(data["categories"])
            delete_link_events_categories(event)
            link_categories_to_event(categories, event)

    except InvalidLink as e:
        return {"error": "Invalid link"}, HTTPStatus.BAD_REQUEST
    except CategoryTypeError as e:
        return e.response, e.status_code

    save_changes(event)
    if key:
        AWS_S3.delete_file(key)

    serialized_event = asdict(event)
    event = get_additonal_information_of_event(serialized_event)

    return jsonify(event), HTTPStatus.OK


def delete_event(event_id):
    try:
        check_id_validation(event_id, Events)
        check_if_the_user_owner(Events, event_id)
    except InvalidIdError as err:
        return err.response, err.status_code
    except NotLoggedUserError as err:
        return err.response, err.status_code
    session: Session = db.session

    event = session.query(Events).filter_by(id=event_id).first()

    key = event.link_banner.split("/")[-1]

    AWS_S3.delete_file(key)

    session.delete(event)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
