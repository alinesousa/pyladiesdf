# -*- coding: utf-8 -*-
from os import path as _path


_project_root = _path.abspath(_path.dirname(_path.dirname(__file__)))

MEDIA_ROOT = _path.join(_project_root, 'media_files/')
DATABASE_URI = 'sqlite:///{0}'.format(_path.join(_project_root, 'pyladiesbsb.db'))
DEBUG = True
