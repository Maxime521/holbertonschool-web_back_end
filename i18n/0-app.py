#!/usr/bin/env python3
"""Minimal Flask app for basic i18n project tasks."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Render the base welcome page."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
