from flask import Flask

from app.commands.category_command import categories_cli


def init_app(app: Flask):
    app.cli.add_command(categories_cli())
