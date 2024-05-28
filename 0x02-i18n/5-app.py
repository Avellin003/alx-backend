#!/usr/bin/env python3
"""flask babel task5"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    a function that returns a user dictionary or
    None if the ID cannot be
    """
    identity = request.args.get('login_as', None)
    if identity is not None and int(identity) in users.keys():
        return users.get(int(identity))
    return None


@app.before_request
def before_request():
    """function that finds a user and sets it as a global"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    a function that determines the best
    match with our supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """function that renders a template
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
