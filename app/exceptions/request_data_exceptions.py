class MissingAttributeError(Exception):
    def __init__(self, missing_keys: list, status_code=400):
        self.response = {"missing_keys": missing_keys}
        self.status_code = status_code
