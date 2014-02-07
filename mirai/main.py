# -*- coding: utf-8 -*-

import flask as fl

app = fl.Flask(__name__)


@app.route('/')
def view_index():
    return fl.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
