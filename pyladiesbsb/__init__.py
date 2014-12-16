# -*- coding: utf-8 -*-
from flask import Flask
from .views.site import site


app = Flask(__name__)

app.config.from_object('config.default')

app.config.from_envvar('APP_CONFIG_FILE')

app.register_blueprint(site)