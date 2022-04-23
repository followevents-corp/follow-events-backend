from app.exceptions.request_data_exceptions import MissingAttributeError


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
