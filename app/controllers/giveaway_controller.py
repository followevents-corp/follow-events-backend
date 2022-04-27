from http import HTTPStatus

from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    MissingAttributeError,
)
from app.models.giveaway_model import Giveaway
from app.services.general_services import check_keys, check_keys_type, save_changes
from app.services.verify_values import incoming_values
from flask import jsonify, request


def create_giveaway(event_id: str):
    data = request.get_json()
    verified_values = incoming_values(data)
    if verified_values:
        return jsonify(verified_values), HTTPStatus.BAD_REQUEST

    try:
        valid_keys = ["name", "description", "award", "award_picture"]

        valid_type_keys = {
            "name": str,
            "description": str,
            "award": str,
            "award_picture": str,
        }

        verified_key = check_keys(data, valid_keys)

        check_keys_type(verified_key, valid_type_keys)

    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code

    verified_key["event_id"] = event_id
    new_giveaway = Giveaway(**verified_key)

    save_changes(new_giveaway)

    return jsonify(new_giveaway), HTTPStatus.OK


def get_giveaway(giveaway_id):
    pass


def update_giveaway(giveaway_id):
    pass


def delete_giveaway(giveaway_id):
    pass
