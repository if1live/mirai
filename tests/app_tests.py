# -*- coding: utf-8 -*-

import unittest
from mirai.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_run(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200)
