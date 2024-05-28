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
    # Check if the request has a 'locale' argument
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # If not, resort to the previous default behavior
    user_language = request.accept_languages.best_match(app.config['LANGUAGES'])
    return user_language

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
