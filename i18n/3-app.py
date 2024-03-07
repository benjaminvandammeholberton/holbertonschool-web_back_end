#!/usr/bin/env python3
""" App entry point
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale() -> str:
    """
    This function is invoked for each request
    to select a language translation to use for that request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


gettext("Welcome to Holberton")
gettext("Hello world!")


@app.route("/")
def index():
    """ index route
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
