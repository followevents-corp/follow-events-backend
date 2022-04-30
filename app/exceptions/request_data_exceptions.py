class MissingAttributeError(Exception):
    def __init__(self, missing_keys: list, status_code=400):
        self.response = {"missing_keys": missing_keys}
        self.status_code = status_code


class AttributeTypeError(Exception):
    name_types = {
        str: "string",
        int: "integer",
        float: "decimal",
        bool: "boolean",
        list: "list",
    }

    def __init__(self, data, types, status_code=400):
        self.response = {"error": self.verify_keys(data, types)}
        self.status_code = status_code

    def verify_keys(self, data, types):
        output = {
            key: f"must be a {self.name_types[types[key]]}"
            for key, value in data.items()
            if type(value) is not types[key]
        }

        return output


class FileTypeError(Exception):
    def __init__(self, message="Invalid file", status_code=415):
        self.message = message
        self.response = {"error": self.message}
        self.status_code = status_code


class InvalidLink(Exception):
    def __init__(self, message="This link violates the platform rules", status_code = 400):
        self.message = message
        self.response = {"error": self.message}
        self.status_code = status_code
