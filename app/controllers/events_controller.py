from dataclasses import asdict
from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.events_model import Events
from app.models.user_model import User

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

    serialized_event = asdict(event)

    result = get_additonal_information_of_event(serialized_event)

    return jsonify(result), HTTPStatus.OK


def update_event(events_id):
    pass


def del_event(events_id):
    pass
