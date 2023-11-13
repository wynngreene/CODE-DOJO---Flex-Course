from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojoModel, ninjaModel

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html", dojos = dojoModel.Dojo.get_all())

@app.route("/create/ninja", methods=["POST"])
def create_ninja():
    ninjaModel.Ninja.save(request.form)
    return redirect("/")