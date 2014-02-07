# -*- coding: utf-8 -*-

import flask as fl
from .helpers import create_document

app = fl.Flask(__name__)

@app.route('/')
def view_index():
    doc_list = [create_document('old_1.md'),
                create_document('old_2.md')]

    return fl.render_template('index.html',
                              doc_list=doc_list)

