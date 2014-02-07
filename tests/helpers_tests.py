# -*- coding: utf-8 -*-

import os
import unittest
from mirai import helpers

class get_content_path_Test(unittest.TestCase):
    def test_run(self):
        filepath = helpers.get_content_path('sample.md')
        self.assertEqual(True, os.path.isfile(filepath))
