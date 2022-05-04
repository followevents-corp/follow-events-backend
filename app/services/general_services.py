from difflib import SequenceMatcher

from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.invalid_id_exception import InvalidIdError
from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    IncorrectKeys,
    MissingAttributeError,
)
from app.exceptions.user_exceptions import NotLoggedUserError
from app.models.events_model import Events
from app.models.giveaway_model import Giveaway
from app.models.schedule_model import Schedule
from app.models.user_model import User


def remove_unnecessary_keys(data: dict, necessary_keys: list):
    """Função que remove chaves desnecessárias do corpo da requisição

    Args:
        data (dict): corpo da requisição
        necessary_keys (list): lista com as chaves que o corpo da requisição deve conter

    Returns:
        tuple: (dicionário contendo apenas os atributos obrigatórios, lista com as chaves que não constam no dicionário retornado)
    """
    new_data = data.copy()
    not_used_keys = necessary_keys.copy()

    for key in data.keys():
        if key in necessary_keys:
            not_used_keys.remove(key)
        else:
            new_data.pop(key)

    return (new_data, not_used_keys)


def check_keys(data: dict, mandatory_keys: list):
    """
    Args:
        data (dict): corpo da requisição
        mandatory_keys (list): lista com as chaves que o corpo da requisição deve conter

    Raises:
        MissingAttributeError: error levantado caso falte algum atributo obrigatório no corpo da requisição

    Returns:
        dict: dicionário contendo apenas os atributos obrigatórios
    """
    new_data, missing_keys = remove_unnecessary_keys(data, mandatory_keys)

    if missing_keys:
        raise MissingAttributeError(missing_keys)

    return new_data


def check_keys_type(data: dict, keys_type: dict):
    """

    Args:
        data (dict): corpo da requisição
        keys_type (dict): dicionário contendo os atributos da requisição como chaves e seus respectivos tipos

    Raises:
        AttributeTypeError: erro levantado caso algum atributo não seja do tipo que deveria
    """

    for key, value in data.items():
        if type(value) is not keys_type[key]:
            raise AttributeTypeError(data, keys_type)


def save_changes(data):
    session = db.session
    session.add(data)
    session.commit()


@jwt_required()
def check_if_the_user_owner(model, id_to_check=""):
    user_id = get_jwt_identity()
    session: Session = db.session
    if model is Events:
        search = (
            session.query(model).filter_by(creator_id=user_id, id=id_to_check).first()
        )
    elif model is User:
        if id_to_check == user_id:
            search = session.query(model).filter_by(id=user_id).first()
        else:
            search = None
    elif model is Giveaway:
        search = (
            session.query(model)
            .select_from(Events)
            .join(Giveaway)
            .filter(Events.creator_id == user_id, Giveaway.id == id_to_check)
            .first()
        )
    elif model is Schedule:
        search = (
            session.query(model)
            .filter_by(user_id=user_id, event_id=id_to_check)
            .first()
        )

    else:
        search = session.query(model).filter_by(user_id=user_id, id=id_to_check).first()

    if not search:
        raise NotLoggedUserError


def check_id_validation(id: str, model: db.Model = None):
    if len(id) != 36:
        raise InvalidIdError(
            message={"error": f"The id {id} is not valid."}, status_code=400
        )
    if model is Schedule:
        search = model.query.filter_by(user_id=id).first()
    elif model:
        search = model.query.filter_by(id=id).first()

    if not search:
        raise InvalidIdError(message={"error": f"The id {id} is not in database."})


def incoming_values(data):
    values_data = [value for value in data.values()]

    if "" in values_data:
        return {"error": "Incoming value is empty."}


def check_if_keys_are_valid(data: dict, data_file, keys: list):
    for key in data.keys():
        if key not in keys:
            raise IncorrectKeys([key])

    for key in data_file.keys():
        if key not in keys:
            raise IncorrectKeys([key])

    if not "data" in data.keys() and not "file" in data_file.keys():
        raise MissingAttributeError(keys)


def is_string_similar(s1: str, s2: str, threshold: float = 0.8):
    return SequenceMatcher(a=s1, b=s2).ratio() > threshold


def similar_keys(data, valid_keys, not_used_keys):
    invalid_keys = [key for key in data.keys() if key not in valid_keys]

    error_keys = []
    for key in invalid_keys:
        for not_used in not_used_keys:
            similar = is_string_similar(key, not_used)
            if similar is True:
                error_keys.append(key)

    if error_keys:
        raise IncorrectKeys(error_keys)

@jwt_required()
def require_jwt():
    ...
