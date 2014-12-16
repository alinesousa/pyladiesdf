import os
import sys
import unittest

from wtf.news_app import create_app

sys.path.append(os.path.abspath(__name__))


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(mode="development")

    def test_request_args(self):
        pass
