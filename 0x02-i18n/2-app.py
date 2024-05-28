#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Create a Config class
class Config:
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
    # Determine the user's preferred language/locale based on the request context
    # For example, you might check the Accept-Language header or user preferences
    user_language = request.accept_languages.best_match(['en', 'fr'])
    return user_language

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
