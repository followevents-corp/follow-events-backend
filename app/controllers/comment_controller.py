from http import HTTPStatus
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import AttributeTypeError, MissingAttributeError
from app.models.comment_model import Comment
from app.services.invalid_id_services import check_id_validation
from app.services.verify_values import incoming_values
from flask import jsonify, request
from app.configs.database import db
from app.services.general_services import check_keys, check_keys_type, save_changes
from sqlalchemy.orm import Query
from app.models.events_model import Events
from sqlalchemy.orm.session import Session


def create_comment(event_id: str):
    comment_data = request.get_json()

    verified_values = incoming_values(comment_data)
    if verified_values:
        return jsonify(verified_values), HTTPStatus.BAD_REQUEST

    try:
        check_id_validation(event_id)
        verified_key = check_keys(comment_data, ['user_id', 'comment'])
        check_keys_type(verified_key, {'user_id': str, 'comment': str})

    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code
    except InvalidIdError as e:
        return e.response, e.status_code

    verified_key["event_id"] = event_id
    new_comment = Comment(**verified_key)

    save_changes(new_comment)

    return jsonify({
        "user_id": new_comment.user_id,
        "comment": new_comment.comment,
    }), HTTPStatus.CREATED


def get_comment(event_id: str):

    try:
        check_id_validation(event_id, Events)
    except InvalidIdError as e:
        return e.response, e.status_code

    session: Session = db.session
    all_comments: Query = (
        session.query(Comment)
        .select_from(Events)
        .join(Comment)
        .filter(Events.id == event_id)
        .all()
    )

    return jsonify(all_comments), HTTPStatus.OK


def update_comment(comment_id: str, event_id: str):
    pass


def delete_comment(comment_id: str):
    try:
        check_id_validation(comment_id, Comment)
    except InvalidIdError as e:
        return e.response, e.status_code
    
    comment = Comment.query.filter_by(id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
