#!/usr/bin/env python3
"""
this is a module that creates a flask app and also a babel object
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Config class for our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    a function that determines the best match with our
    supported languages and returns the best one
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """


    a definition that renders a template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
