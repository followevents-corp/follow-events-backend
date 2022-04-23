class MissingAttributeError(Exception):
    def __init__(self, missing_keys: list):
        self.missing_keys = missing_keys
