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

@app.route("/ninja/edit/<ninja_id>")
def edit_ninja(ninja_id):
    print("in the edit for ninja_id", ninja_id)
    return render_template("edit.html")


@app.route("/ninja/delete/<ninja_id>/<dojo_id>")
def delete_ninja(ninja_id):
    print("deleting ninja with id:", ninja_id)
    return redirect(f"/dojos/{dojo_id}")


@app.route("/ninja/update", methods=["POST"])
def update_ninja():
    # ninjaModel.Ninja.save(request.form)
    print("In update to ninja with update:", request.form)
    return redirect(f"dojo/{request.form["dojo_id"]}")
