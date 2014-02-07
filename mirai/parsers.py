# -*- coding: utf-8 -*-

import markdown
import re

class Document(object):
    def __init__(self, content, attr_dict=None):
        if attr_dict == None:
            attr_dict = u''

        self.content = content
        self.attr_dict = attr_dict

class DocumentParser(object):
    ATTR_LINE_PROG = re.compile('^(.+):(.+)$')

    def parse(self, raw):
        pass

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
