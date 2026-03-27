#!/usr/bin/env python3
"""Basic Flask app for i18n project.

Exposes a single '/' route rendering templates/3-index.html with Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
import flask_babel


class Config:
    """Application configuration for Babel."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale():
    """Return the best matching locale based on the request headers."""
    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


babel.init_app(app, locale_selector=get_locale)


def gettext(message_id: str) -> str:
    """Return the localized string for the given message identifier."""
    return flask_babel.gettext(message_id)


@app.route("/", methods=["GET"])
def index():
    """Render localized landing page."""
    return render_template(
        "3-index.html",
        locale=get_locale(),
        gettext=gettext,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
