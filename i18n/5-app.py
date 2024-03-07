#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict | None:
    """Retrieve an user from the param 'login_as'"""
    if (not request.args['login_as'] or
            int(request.args['login_as']) not in users):
        return None
    return users.get(int(request.args['login_as']))


@app.before_request
def before_request():
    """set user to g.user"""
    user = get_user()
    if user:
        g.user = user


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale"""
    if ('locale' in request.args and
            request.args['locale'] in app.config['LANGUAGES']):
        return request.args['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return index.html"""
    try:
        username = g.user["name"]
    except Exception:
        username = None
    return render_template("5-index.html", username=username)


if __name__ == '__main__':
    app.run(debug=True)
