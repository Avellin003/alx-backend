#!/usr/bin/env python3
"""
flask babel task2
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):
    """
    a class Configures the languages to use
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Flask app
app = Flask(__name__)
# Config app
app.config.from_object(Config)
# Babel app
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    a function that determines the best
    match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """a function that renders a template"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
