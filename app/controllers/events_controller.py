from dataclasses import asdict
from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.events_model import Events

from app.exceptions.invalid_id_exception import InvalidIdError
from app.services.invalid_id_services import check_id_validation

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
    pass


def get_by_id_event(events_id):
    try:
        check_id_validation(events_id, Events)
    except InvalidIdError as err:
        return err.response, err.status_code

    session: Session = db.session

    event = session.query(Events).filter_by(id=events_id).first()

    serialized_event = asdict(event)

    result = get_additonal_information_of_event(serialized_event)

    return jsonify(result), HTTPStatus.OK


def update_event(events_id):
    pass


def del_event(events_id):
    pass
