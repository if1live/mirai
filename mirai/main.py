# -*- coding: utf-8 -*-

import os
import flask as fl
from flask_frozen import Freezer
from .helpers import create_document

app = fl.Flask(__name__)
output_path = os.path.join(os.path.dirname(__file__), '..', 'build')
app.config.update(FREEZER_DESTINATION=output_path)

freezer = Freezer(app)

@app.route('/')
def view_index():
    jumbotron = create_document('jumbotron.md')
    doc_filelist = ['movie.md',
                    'news.md',
                    'game.md',
                    'contribute.md']
    doc_list = [create_document(x) for x in doc_filelist]

    title = u'안전한 사전심의를 위한 모임'

    return fl.render_template('index.html',
                              title=title,
                              jumbotron=jumbotron,
                              doc_list=doc_list,)

