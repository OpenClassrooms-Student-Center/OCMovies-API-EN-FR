#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)



### Les variables à afficher dans le Front

messageBienvenue = "Futur développeur Python"
objectif = "L'objectif de ce projet est d'intéragir avec une API Rest et le front"


### Les variables à afficher dans le Front

@app.route("/")
def index():
    return render_template("index.html", texte = messageBienvenue, message = objectif )

if __name__ == "__main__":
    app.run(debug=True)
