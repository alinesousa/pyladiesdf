# -*- coding: utf-8 -*-
from flask import Flask

from .views.site import site


def create_app(config_file):

    app = Flask(__name__)

    app.config.from_object('config.default')

    app.config.from_pyfile(config_file)

    app.register_blueprint(site)

    return app
