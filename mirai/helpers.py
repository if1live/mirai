# -*- coding: utf-8 -*-

import os.path

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
    return content
