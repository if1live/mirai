# -*- coding: utf-8 -*-

import markdown
import re

class Document(object):
    def __init__(self, content, attr_dict=None):
        if attr_dict == None:
            attr_dict = {}

        self.content = content
        self.attr_dict = attr_dict

    @property
    def html(self):
        return markdown.markdown(self.content, ['footnotes'])

    def __getattr__(self, key):
        return self.get_attr(key)

    def get_attr(self, key):
        u'''
        문서에 추가 명시한 속성 얻기
        속성의 경우는 기본값=''으로 줘서 없는 속성에 접근해도 죽지 않도록했다.
        '''
        return self.attr_dict.get(key, u'')

class DocumentParser(object):
    ATTR_LINE_PROG = re.compile('^([a-zA-Z\-_]+)\s*:(.+)$')

    def __call__(self, raw):
        attr_doc, content_doc = self.split_doc(raw)
        attr_dict = self.parse_attr_doc(attr_doc)
        return Document(content_doc, attr_dict)

    def split_doc(self, raw):
        line_list = raw.splitlines()

        attr_line_list = []
        content_line_list = []

        content_occur = False
        for line in line_list:
            # content 시작이후는 전부 content
            if content_occur:
                content_line_list.append(line)
                continue

            if len(line.strip()) == 0:
                continue

            m = self.ATTR_LINE_PROG.match(line)
            if m:
                attr_line_list.append(line)
            else:
                content_line_list.append(line)
                content_occur = True

        attr_doc = u'\n'.join(attr_line_list)
        content_doc = u'\n'.join(content_line_list)
        return attr_doc, content_doc

    def parse_attr_line(self, line):
        m = self.ATTR_LINE_PROG.match(line)
        if not m:
            return None

        key, value = m.groups()
        key = key.strip()
        value = value.strip()
        return {key : value}

    def parse_attr_doc(self, content):
        line_list = content.splitlines()
        data_list = []
        for line in line_list:
            attr = self.parse_attr_line(line)
            data_list += list(attr.items())
        return dict(data_list)
