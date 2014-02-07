# -*- coding: utf-8 -*-

import os.path
from .parsers import DocumentParser

def get_content_path(filename):
    curr_dir = os.path.dirname(__file__)
    path_token_list = [curr_dir, '..', 'wiki', filename]
    return os.path.join(*path_token_list)

def read_content(filepath):
    if os.path.isfile(filepath) == False:
        raise OSError('no such file : ' + filepath)
    f = open(filepath)
    content = f.read()
    f.close()
    content = content.decode('utf-8')
    return content

def create_document(filename):
    parser = DocumentParser()
    raw = read_content(get_content_path(filename))
    doc = parser(raw)
    return doc
