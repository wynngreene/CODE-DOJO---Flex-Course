from flask import render_template, redirect, request
from flask_app import app
# from flask_app.models.dojoModel import Dojo

@app.route("/")
def index():
    return redirect("/cookies")

@app.route("/cookies")
def cookies():
    # dojos = Dojo.get_all()
    return render_template("index.html")

@app.route("/cookies/new")
def new_cookies():
    return render_template("new_order.html")

@app.route("/cookies/edit")
def edit_cookies():
    return render_template("edit_order.html")