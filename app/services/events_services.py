from flask import request, url_for
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.request_data_exceptions import FileTypeError, FormatDateError
from app.models.categories_events_model import EventsCategories
from app.models.categories_model import Categories
from app.models.events_model import Events
from app.models.schedule_model import Schedule
from app.services.general_services import save_changes
from werkzeug.datastructures import FileStorage
from datetime import datetime as dt


def get_additonal_information_of_event(data: dict) -> dict:
    """
    Args:
        data (dict): dicionário de evento

    Returns:
        dict: um dicionário da model Events adiconando a quantidade de usuários
        cadastrados neste evento, as categorias do evento, a url dos
        comentários do evento e a url dos eventos de sorte deste evento.
    """
    session: Session = db.session

    categories_class = (
        session.query(Categories)
        .select_from(EventsCategories)
        .join(Events)
        .join(Categories)
        .filter(Events.id == data["id"])
        .all()
    )

    data.update(
        {
            "quantity_users": session.query(Schedule)
            .filter(data["id"] == Schedule.event_id)
            .count()
        }
    )

    data.update({"categories": [category.name for category in categories_class]})

    comment_url = url_for("comments.get_comment", event_id=data["id"])
    giveaway_url = url_for("giveaway.get_giveaway", event_id=data["id"])
    data.update({"comments": f"{request.host_url[:-1]}{comment_url}"})
    data.update({"giveaway": f"{request.host_url[:-1]}{giveaway_url}"})

    return data


def link_categories_to_event(categories: list, event: Events):
    for category in categories:
        category_uuid = (
            db.session.query(Categories).filter_by(name=category.title()).first().id
        )
        events_category = EventsCategories(event_id=event.id, category_id=category_uuid)
        save_changes(events_category)


def delete_link_events_categories(event: Events):
    session: Session = db.session

    connections = session.query(EventsCategories).filter_by(event_id=event.id).all()

    for connection in connections:
        session.delete(connection)
    session.commit()


def check_type_of_file(file):
    if type(file) is not FileStorage:
        raise FileTypeError
    else:
        file_type = file.content_type.split("/")[0]
        if file_type not in ["image", "video"]:
            raise FileTypeError(message="Only image and video files are supported")

def check_format_date(date):
    try:
        dt.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError:
        raise FormatDateError

