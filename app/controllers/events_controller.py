from dataclasses import asdict
from http import HTTPStatus

from flask import jsonify, request, url_for
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.categories_events_model import EventsCategories
from app.models.categories_model import Categories
from app.models.events_model import Events
from app.models.schedule_model import Schedule

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

    url_base = request.host_url[:-1]

    for event in serialized_events:
        categories_class = (
            session.query(Categories)
            .select_from(EventsCategories)
            .join(Events)
            .join(Categories)
            .filter(event["id"] == EventsCategories.event_id)
            .filter(Categories.id == EventsCategories.category_id)
            .all()
        )

        event["quantity_users"] = (
            session.query(Schedule).filter(event["id"] == Schedule.event_id).count()
        )
        event["categories"] = [category.name for category in categories_class]
        comment_url = url_for("comments.get_comment", event_id=event["id"])
        giveaway_url = url_for("giveaway.get_giveaway", event_id=event["id"])
        event["comments"] = f"{url_base}{comment_url}"
        event["giveaway"] = f"{url_base}{giveaway_url}"

    return jsonify(serialized_events), HTTPStatus.OK


def get_by_id_event(events_id):
    pass


def update_event(events_id):
    pass


def del_event(events_id):
    pass
