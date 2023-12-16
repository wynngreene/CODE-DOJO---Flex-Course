from flask import render_template, redirect, session, request, flash
from flask_app import app
# from flask_app.models.user_Model import User
# from flask_bcrypt import Bcrypt        
# bcrypt = Bcrypt(app) 

# 00 ROUTES
@app.route("/")
def index():
    return render_template("index.html")

# 01 ROUTES
@app.route("/recipes")
def dashboard():
    return render_template("home.html")

# 02 ROUTES
@app.route("/recipes/new")
def new_recipe():
    return render_template("create_recipe.html")

# 03 ROUTES
@app.route("/recipes/2")
def detail_recipe():
    return render_template("recipe_detail.html")

# 04 ROUTES
@app.route("/recipes/edit")
def edit_recipe():
    return render_template("edit_recipe.html")

# 05 ROUTES
@app.route("/recipes/edit")
def delete_recipe():
    return redirect("/recipes")