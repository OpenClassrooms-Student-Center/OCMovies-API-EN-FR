"""This module is part of the JustStreamIt project and initializes the 
Flask application."""

from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)

from . import views