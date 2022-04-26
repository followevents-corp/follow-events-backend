from app.exceptions.request_data_exceptions import (AttributeTypeError,
                                                    MissingAttributeError)
from app.configs.database import db

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
    new_data = data.copy()

    for key in data.keys():
        if key in mandatory_keys:
            mandatory_keys.remove(key)
        else:
            new_data.pop(key)

    if mandatory_keys:
        raise MissingAttributeError(mandatory_keys)

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


session = db.session

def save_changes(data):
    session.add(data)
    session.commit()