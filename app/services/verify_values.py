def incoming_values(data):
    values_data = [value for value in data.values()]

    if "" in values_data:
        return {"error": "Incoming value is empty."}
