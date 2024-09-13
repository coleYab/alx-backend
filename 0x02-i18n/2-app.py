#!/usr/bin/env python3
"""
simple babel configuration
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config:
    """
    a simple config class for bable
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE ="en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.loacleselector
def get_loacle() -> str:
    """ returns the message to get a loacale language
    """
    return request.accept_languages.best_match(['fr', 'en'])


@app.route("/")
def homepage() -> str:
    """
    simple template website
    """
    return render_template('1-index.html')

if __name__ == '__main__':
        app.run(port="5000", host="0.0.0.0", debug=True)
