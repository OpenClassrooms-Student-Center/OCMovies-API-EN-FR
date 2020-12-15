"""This module implements the views of the application. Each function handles
a HTTP request comme from the web browser of the visitor or any http client."""

from flask import render_template

from . import app


@app.route("/")
def index():
    """View handling the homepage of the website."""
    # Define context variables to be sent by the app to the template
    context = {
        'title': 'Mon site web',
        'page_name': 'Accueil',
        'visitor_name': 'Futur développeur Python',
        'message': (
            "L'objectif de ce projet est d'intéragir avec une API "
            "Rest et le front"
        ),
    }
    # Renders the index.html template from the templates folder
    return render_template("index.html", **context)