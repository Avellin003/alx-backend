#!/usr/bin/env python3
"""task 2"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """class that configures the languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# create an instance of the Flask class
app = Flask(__name__)
# set the configuration of the app
app.config.from_object(Config)
# create an instance of the Babel class
babel = Babel(app)


@babel.localeselector
def get_locale():
    """a function that gets the prefered language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """definition of the index route"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
