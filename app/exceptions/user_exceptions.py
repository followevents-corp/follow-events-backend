class EmailFormatError(Exception):
    def __init__(self, message="Provide a valid email", status_code=400):
        self.message = message
        self.status_code = status_code

