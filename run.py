# -*- coding: utf-8 -*-
import os


os.environ.setdefault('APP_CONFIG_FILE',
                      os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   'config/development.py')))

from pyladiesbsb import app


app.run()
