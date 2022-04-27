from app.configs.database import db
from app.exceptions.invalid_id_exception import InvalidIdError


def check_id_validation(id: str, model: db.Model = None):
    if len(id) != 36:
        raise InvalidIdError(
            message={"error": f"The id {id} is not valid."}, status_code=400
        )

    if model:
        search = model.query.filter_by(id=id).first()
        if not search:
            raise InvalidIdError(message={"error": f"The id {id} is not in database."})
