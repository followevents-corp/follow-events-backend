from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.events_model import Events


def create_events():
    files = request.files

    for obj in files:
        if obj == "file":
            event = Events(name = "EVENTO2", event_date = "01/12/2023", link = files[obj], type_banner = "png")
        return jsonify(event), HTTPStatus.CREATED
    return {},HTTPStatus.OK