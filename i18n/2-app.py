#!/usr/bin/env python3
"""Flask app with locale selection powered by Babel."""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Application configuration for Babel."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale():
    """Return the best match between supported languages and the request."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index():
    """Render localized landing page."""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
