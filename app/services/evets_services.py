from flask import request, url_for
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.categories_events_model import EventsCategories
from app.models.categories_model import Categories
from app.models.events_model import Events
from app.models.schedule_model import Schedule


def get_additonal_information_of_event(data: dict) -> dict:
    """
    Args:
        data (dict): corpo da requisição

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
        .filter(data["id"] == EventsCategories.event_id)
        .filter(Categories.id == EventsCategories.category_id)
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
