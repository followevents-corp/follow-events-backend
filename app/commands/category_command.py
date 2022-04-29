from flask.cli import AppGroup
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.categories_model import Categories


def categories_cli():
    category_group = AppGroup("categories", help="Create default categories")

    @category_group.command("create_default")
    def create_categories():
        session: Session = db.session
        categories = ["games", "music", "live", "talks", "e-sports"]

        default_categories = [
            Categories(name=category) for category in categories
        ]

        session.add_all(default_categories)
        session.commit()

    return category_group
