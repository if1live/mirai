# -*- coding: utf-8 -*-

import os
import unittest
from mirai import helpers

class get_content_path_Test(unittest.TestCase):
    def test_run(self):
        filepath = helpers.get_content_path('sample.md')
        self.assertEqual(True, os.path.isfile(filepath))

class read_content_Test(unittest.TestCase):
    def test_run(self):
        filepath = helpers.get_content_path('testdata.md')
        self.assertEqual(True, os.path.isfile(filepath))

        actual = helpers.read_content(filepath)
        expected = 'key: test-data\nfor test'
        self.assertEqual(expected, actual)

class create_document_Test(unittest.TestCase):
    def test_run(self):
        helpers.create_document('testdata.md')

