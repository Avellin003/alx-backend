#!/usr/bin/env python3
"""flask babel task3"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


# Create a Config class
class Config(object):
    # Define available languages
    LANGUAGES = ["en", "fr"]

    # Set Babel's default locale and timezone
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config as config for your Flask app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale from user request"""
    languages = app.config['LANGUAGES']
    user_language = request.accept_languages.best_match(languages)
    return user_language


@app.route('/')
def index() -> str:
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
