from http import HTTPStatus
from flask import jsonify, request
from app.models.user_model import User
from app.configs.database import db
from sqlalchemy.orm import Session

session: Session = db.session

def create_user():

    data = request.get_json()

    new_user = User(**data)

    session.add(new_user)
    session.commit()

    return jsonify(new_user), HTTPStatus.CREATED


def get_user(user_id:int):
    pass

def update_user(user_id:int):
    pass

def delete_user(user_id:int):
    pass