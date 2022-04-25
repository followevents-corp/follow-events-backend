class MissingAttributeError(Exception):
    def __init__(self, missing_keys: list, status_code=400):
        self.response = {"missing_keys": missing_keys}
        self.status_code = status_code


class AttributeTypeError(Exception):
    def __init__(self, key, type, status_code=400):
        if type is str:
            self.type = "string"
        elif type is int:
            self.type = "integer"
        elif type is float:
            self.type = "decimal"
        elif type is bool:
            self.type = "boolean"
        elif type is list:
            self.type = "list"
        else:
            self.type = "update types"

        self.message = f"{key} must be a {self.type}"
        self.status_code = status_code


from app.exceptions.request_data_exceptions import AttributeTypeError
