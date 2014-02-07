# -*- coding: utf-8 -*-

import unittest
from mirai.parsers import DocumentParser

RAW_TEXT = u'''
key: value
title: subtitle

여기부터 내용이 시작합니다

title: 무시속성
'''

ATTR_TEXT = u'''key: value
title: subtitle'''

CONTENT_TEXT = u'''여기부터 내용이 시작합니다

title: 무시속성'''


class DocumentParserTest(unittest.TestCase):
    def test_parse_attr_line(self):
        parser = DocumentParser()

        line = u'simple: this-is-value'
        expected = {u'simple' : u'this-is-value'}
        self.assertEqual(expected, parser.parse_attr_line(line))

        line = u'with-space  :  this is value    '
        expected = {u'with-space' : u'this is value' }
        self.assertEqual(expected, parser.parse_attr_line(line))

        line = u'한글 : 유니코드 값'
        expected = {u'한글' : u'유니코드 값'}
        self.assertEqual(expected, parser.parse_attr_line(line))

        line = u'this is not attr line'
        self.assertEqual(None, parser.parse_attr_line(line))

    def test_split_doc(self):
        parser = DocumentParser()
        attr_doc, content_doc = parser.split_doc(RAW_TEXT)
        self.assertEqual(ATTR_TEXT, attr_doc)
        self.assertEqual(CONTENT_TEXT, content_doc)

    def test_parse_attr_doc(self):
        parser = DocumentParser()

        line = u'simple: this-is-value'
        expected = {u'simple' : u'this-is-value'}
        self.assertEqual(expected, parser.parse_attr_doc(line))

        expected = {u'key' : u'value',
                    u'title' : u'subtitle'}
        self.assertEqual(expected, parser.parse_attr_doc(ATTR_TEXT))

