#!/usr/bin/env python3
""" App entry point
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Config class for Flask app
    """
    LANGUAGES = ["en", "fr"]


config = Config()


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def index():
    """ index route
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
