# -*- coding: utf-8 -*-

import unittest
from mirai import helpers

class DummyTest(unittest.TestCase):
    def test_run(self):
        self.assertEqual(helpers.foo(), 1)
