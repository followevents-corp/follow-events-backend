from app.configs.database import db
from app.exceptions.request_data_exceptions import (AttributeTypeError,
                                                    MissingAttributeError)


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
