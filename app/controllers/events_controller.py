from http import HTTPStatus
from pprint import pprint
import json

from flask import current_app, jsonify, request

from app.models.events_model import Events
from app.services.verify_values import incoming_values
from app.services.general_services import check_keys, save_changes
from app.services.categories_services import create_categories

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
    keys = ["name", "description", "event_date", "event_link","creator_id"]
    files = request.files

    file = files["file"]
    data = json.loads(request.form["data"])

    categories = data["categories"]
    create_categories(categories)

    data.pop("categories")

    new_data = check_keys(data, keys)
    verify_values = incoming_values(data)

    if verify_values:
        return jsonify(verify_values), HTTPStatus.BAD_REQUEST

    event = Events(**data,  link = file)
    # save_changes(event)
    return jsonify(event), HTTPStatus.CREATED

def get_events():
    pass

def get_by_id_event(events_id):
    pass

def update_event(events_id):
    pass

def del_event(events_id):
    pass