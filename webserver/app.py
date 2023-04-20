import sys
import os

from flask import Flask
from webserver.views import views


def setup():
    """
    Main orchestrating setup method
    """
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')
    return app

