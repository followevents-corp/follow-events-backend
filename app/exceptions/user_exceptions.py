class EmailFormatError(Exception):
    def __init__(self, message="Provide a valid email", status_code=400):
        self.message = message
        self.status_code = status_code

class NotLoggedUserError(Exception):
    def __init__(self, response={"error": "Unauthorized"}, status_code=401):
        self.response = response
        self.status_code = status_code

class NameFormatError(Exception):
    def __init__(self, response={"error": "Provide a valid Name."}, status_code=400):
        self.response = response
        self.status_code = status_code