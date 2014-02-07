# -*- coding: utf-8 -*-

import unittest
from mirai.parsers import DocumentParser, Document

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

ATTR_DICT = {u'key' : u'value',
            u'title' : u'subtitle'}


class DocumentParserTest(unittest.TestCase):
    def test_parse_attr_line(self):
        parser = DocumentParser()

        line = u'simple: this-is-value'
        expected = {u'simple' : u'this-is-value'}
        self.assertEqual(expected, parser.parse_attr_line(line))

        line = u'with-space  :  this is value    '
        expected = {u'with-space' : u'this is value' }
        self.assertEqual(expected, parser.parse_attr_line(line))

        line = u'key : 유니코드 값'
        expected = {u'key' : u'유니코드 값'}
        self.assertEqual(expected, parser.parse_attr_line(line))

        line = u'this is not attr line'
        self.assertEqual(None, parser.parse_attr_line(line))

    def test_parse_attr_line_if_url(self):
        u'''
        url의 경우 ':'가 들어간다. :가 들어간다고 전부 속성이 아닌 예이다.
        key를 영어문자로만 한정해서 문제를 해결
        '''
        parser = DocumentParser()
        line = u'[이건희, 또는 반기문 UN사무총장](http://isplus.joins.com/article/244/13681244.html) 님이신가요?'
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

        self.assertEqual(ATTR_DICT, parser.parse_attr_doc(ATTR_TEXT))

    def test_call(self):
        parser = DocumentParser()
        document = parser(RAW_TEXT)
        self.assertEqual(document.attr_dict, ATTR_DICT)
        self.assertEqual(document.content, CONTENT_TEXT)

class DocumentTest(unittest.TestCase):
    def test_create(self):
        content = 'ctx'
        attr_dict = {'foo':'bar'}

        document = Document(content, attr_dict)
        self.assertEqual(content, document.content)
        self.assertEqual(attr_dict, document.attr_dict)

        document = Document(content)
        self.assertEqual({}, document.attr_dict)

    def test_get_attr(self):
        document = Document('', {'foo':'bar'})
        self.assertEqual('bar', document.get_attr('foo'))
        self.assertEqual('', document.get_attr('not-exist'))

    def test_getattr(self):
        document = Document('content', {'foo':'bar'})
        self.assertEqual('content', document.content)
        self.assertEqual('bar', document.foo)
        self.assertEqual('', document.not_exist)

    def test_html(self):
        content = 'ctx'
        document = Document(content, {})
        expected = '<p>ctx</p>'
        self.assertEqual(expected, document.html)
