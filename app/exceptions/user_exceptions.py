class EmailFormatError(Exception):
    def __init__(self):
        self.message = "Provide a valid email"
