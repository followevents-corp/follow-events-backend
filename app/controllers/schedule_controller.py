from sqlalchemy.orm.session import Session
from app.exceptions.request_data_exceptions import AttributeTypeError, MissingAttributeError
from app.models.schedule_model import Schedule
from flask import jsonify, request
from app.services.general_services import check_keys, check_keys_type
import uuid

def create_schedule(user_id):
    # data = request.get_json()
    data = {"event_id": uuid.uuid4()}
    try:
        new_data = check_keys(data, ["event_id"])
        check_keys_type(new_data, {"event_id": uuid.UUID})
    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    return ""

    


def get_schedule():
    pass


def delete_schedule(event_id):
    pass
