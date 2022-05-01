from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.category_exceptions import CategoryTypeError
from app.models.categories_model import Categories

def create_categories(categories_names: list):
    session: Session = db.session

    categories_to_add = list()

    for category in categories_names:

        if type(category) is not str or not category:
            raise CategoryTypeError(categories_names)

        created_category = (
            session.query(Categories).filter_by(name=category).first()
        )

        if created_category:
            categories_to_add.append(Categories(name=category))

    session.add_all(categories_to_add)
    session.commit()
