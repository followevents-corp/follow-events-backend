from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, DataError
from app.exceptions.user_exceptions import EmailFormatError
from app.configs.database import db
from app.models.user_model import User
from app.services.verify_values import incoming_values

session: Session = db.session

def create_user():
    data = request.get_json()

    empty_values = incoming_values(data)

    if empty_values:
        return empty_values, HTTPStatus.BAD_REQUEST

    try:
        new_user = User(**data)
    except TypeError as e:
        return {'error': f'{e}'}, HTTPStatus.BAD_REQUEST
    except EmailFormatError:
        return {'error': f'Email format not acceptable: {data["email"]}, try ex.: your_mail@your_provider.com'}, HTTPStatus.BAD_REQUEST

    try:
        session.add(new_user)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        error = str(e)

        if 'Key (email)' in error:
            return {'error': 'Email already exists.'}, HTTPStatus.CONFLICT
        return {'error': 'Username already exists.'}, HTTPStatus.CONFLICT
    except DataError as e:
        session.rollback()
        error = str(e)
        if 'varying(30)' in error:
            return {'error': 'Username has to be 6 to 30 characters.'}, HTTPStatus.BAD_REQUEST
        return {'error': 'Name has to be less than 100 characters. If your name is greater than that, try abbreviate it. :D'}, HTTPStatus.BAD_REQUEST

    return jsonify(new_user), HTTPStatus.CREATED


def get_user(user_id):
    pass

def update_user(user_id):
    pass

def delete_user(user_id):
    pass