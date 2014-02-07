# -*- coding: utf-8 -*-

import flask as fl
from .helpers import create_document

app = fl.Flask(__name__)

@app.route('/')
def view_index():
    jumbotron = create_document('jumbotron.md')
    doc_filelist = ['movie.md',
                    'news.md',
                    'childbirth.md',
                    'game.md',
                    'contribute.md',
                    'footnote.md']
    doc_list = [create_document(x) for x in doc_filelist]

    title = u'안전한 사전심의를 위한 모임'

    return fl.render_template('index.html',
                              title=title,
                              jumbotron=jumbotron,
                              doc_list=doc_list,)

