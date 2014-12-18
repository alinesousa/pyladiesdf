# -*- coding: utf-8 -*-
import os

from pyladiesbsb import create_app


config_file = os.getenv(
    'APP_CONFIG_FILE', os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    'config/development.py')))

app = create_app(config_file)

app.run()
