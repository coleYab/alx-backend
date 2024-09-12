#!/usr/bin/env python3
"""
a simple flask setup for my program
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def get_home_page():
    """
    routing home page for index html
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000")
