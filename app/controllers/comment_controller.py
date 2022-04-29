from http import HTTPStatus
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import AttributeTypeError, MissingAttributeError
from app.exceptions.user_exceptions import NotLoggedUser
from app.models.comment_model import Comment
from app.models.user_model import User
from flask import jsonify, request
from app.configs.database import db
from app.services.general_services import (
    check_id_validation,
    check_if_the_user_owner,
    check_keys,
    check_keys_type,
    incoming_values,
    save_changes,
)
from sqlalchemy.orm import Query
from app.models.events_model import Events
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_comment(event_id: str):
    comment_data = request.get_json()
    comment_data["user_id"] = get_jwt_identity()
    verified_values = incoming_values(comment_data)
    if verified_values:
        return jsonify(verified_values), HTTPStatus.BAD_REQUEST

    try:
        check_id_validation(event_id, Events)
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

    return (
        jsonify(
            {
                "comment": new_comment.comment
            }
        ),
        HTTPStatus.CREATED,
    )


def get_comment(event_id: str):

    try:
        check_id_validation(event_id, Events)
    except InvalidIdError as e:
        return e.response, e.status_code

    session: Session = db.session
    all_comments: Query = (
        session.query(Comment.id, Comment.comment, Comment.created_at,
                      Comment.user_id, User.username, User.profile_picture)
        .select_from(Events)
        .join(Comment)
        .join(User)
        .filter(Events.id == event_id)
        .filter(Comment.user_id == User.id)
        .all()
    )

    response = [comment._asdict() for comment in all_comments]

    return jsonify(response), HTTPStatus.OK


@jwt_required()
def update_comment(comment_id: str):
    data = request.get_json()
    try:
        check_if_the_user_owner(Comment, comment_id)
        check_id_validation(comment_id, Comment)
        verified_key = check_keys(data, ['comment'])
        check_keys_type(verified_key, {'comment': str})

    except MissingAttributeError as e:
        return e.response, e.status_code
    except AttributeTypeError as e:
        return e.response, e.status_code
    except InvalidIdError as e:
        return e.response, e.status_code
    except NotLoggedUser as e:
        return e.response, e.status_code

    comment = Comment.query.filter_by(id=comment_id).first()

    for key, value in data.items():
        setattr(comment, key, value)

    save_changes(comment)

    user_creator = User.query.filter_by(id=Comment.user_id).first()

    return jsonify({
        "id": comment.id,
        "comment": comment.comment,
        "created_at": comment.created_at,
        "user_id": comment.user_id,
        "username": user_creator.username,
        "profile_picture": user_creator.profile_picture
    }), HTTPStatus.OK


@jwt_required()
def delete_comment(comment_id: str):
    try:
        check_id_validation(comment_id, Comment)
        check_if_the_user_owner(Comment, comment_id)
    except InvalidIdError as e:
        return e.response, e.status_code
    except NotLoggedUser as e:
        return e.response, e.status_code
    
    comment = Comment.query.filter_by(id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT

