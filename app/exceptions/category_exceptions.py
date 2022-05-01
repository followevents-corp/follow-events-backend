class CategoryTypeError(Exception):
    def __init__(self, categories: list, status_code=400):
        self.response = {"error": self.verify_category(categories)}
        self.status_code = status_code

    def verify_category(self, categories: list):
        output = dict()

        for category in categories:
            if type(category) is not str or not category:
                output.update({f"category {category}": "must be a valid string"})

        return output
