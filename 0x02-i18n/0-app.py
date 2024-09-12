#!/usr/bin/env python3
# initial code for python3 in my world
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def get_home_page():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000")
