def incoming_values(data):
    values_data = [value for value in data.values()]
    error_values = ['']

    if values_data in error_values:
        return {'error': 'Incoming value is empty.'}

    type_values = [value for value in values_data if type(value) != str]

    if type_values:
        return {'error': 'Incoming value is not a str type.'}