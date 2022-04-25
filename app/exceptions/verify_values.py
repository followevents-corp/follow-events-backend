def incoming_values(data):
    values_data = [value for value in data.values()]
    error_values = ['']

    if values_data in error_values:
        return {'error': 'Incoming value is empty.'}