class InvalidIdError(Exception):
    default_msg =  {"error": "Id not found in database."}
    
    def __init__(self, message: dict, status_code=404):
        self.response = message or self.default_msg
        self.status_code = status_code
        