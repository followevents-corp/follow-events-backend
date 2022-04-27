from http import HTTPStatus
from app.configs.database import db
from app.models.events_model import Events
from app.models.giveaway_model import Giveaway
from flask import jsonify
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def create_giveaway():
    pass


def get_giveaway(event_id: str):
    session: Session = db.session

    giveaways: Query = (
        session.query(Giveaway)
        .select_from(Events)
        .join(Giveaway)
        .filter(Events.id == event_id)
        .all()
    )

    return jsonify(giveaways), HTTPStatus.OK


def update_giveaway(giveaway_id):
    pass


def delete_giveaway(giveaway_id):
    pass
