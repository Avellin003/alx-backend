#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime
from flask_babel import format_datetime


app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

def get_user():
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    # Check if a user is logged in and their preferred locale is supported
    if g.user is not None and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check if the request has a 'locale' argument
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # If not, resort to the previous default behavior
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    # Check if a user is logged in and their preferred timezone is valid
    if g.user is not None:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass

    # Check if the request has a 'timezone' argument and it's valid
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # If not, resort to the default timezone
    return 'UTC'
@app.route('/')
def index():
    current_time = datetime.utcnow()
    formatted_time = format_datetime(current_time)
    return render_template('index.html', current_time=formatted_time)

if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)