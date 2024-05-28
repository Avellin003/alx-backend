#!/usr/bin/env python3
"""task 2"""
from flask import Flask, render_template, request
from flask_babel import Babel


# Create a Config class
class Config(object):
    """Define available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the Babel object
app = Flask(__name__)
# Use Config as config for your Flask app
app.config.from_object(Config)
# Instantiate the Babel object
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    a function that determines the best match with our supported languages.
    """
    user_language = request.accept_languages.best_match(['en', 'fr'])
    return user_language


@app.route('/', strict_slashes=False)
def index() -> str:
    """defining the index route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
