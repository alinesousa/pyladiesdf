# -*- coding: utf-8 -*-
import dataset

from flask import current_app


def get_table(tablename):
    db = dataset.connect(current_app.config['DATABASE_URI'])
    return db[tablename]
