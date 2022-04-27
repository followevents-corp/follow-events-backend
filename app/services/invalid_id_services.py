from app.exceptions.invalid_id_exception import InvalidIdError
from app.configs.database import db

def check_id_validation(id: str, model: db.Model):
    if len(id) != 36:
        raise InvalidIdError(
            message={"error": f"The id {id} is not valid."}, status_code=400)

    search = model.query.filter_by(id=id).first()
    
    if not search:
        raise InvalidIdError(
            message={"error": f"The id {id} is not in database."})
    