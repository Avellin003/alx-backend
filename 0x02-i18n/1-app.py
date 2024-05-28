#!/usr/bin/env python3
"""task 1"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)


# Create a Config class
class Config:
    """Define available languages"""
    LANGUAGES = ["en", "fr"]

    # Set Babel's default locale and timezone
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config as config for your Flask app
app.config.from_object(Config)


# Initialize the Babel object with the Flask app
@app.route('/')
def index() -> str:
    """index"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
