import os

from flask import Flask
from .auth import auth


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth.bp)

    return app