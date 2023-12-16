from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask import flash
from flask_app.models.recipe_Model import Recipe
from flask_app.models.user_Model import User


######## GET ROUTES ########

# 01 ROUTES | 
@app.route("/recipes/home")
def recipes_home():
    if "user_id" not in session:
        print("Yo, you need to be logged in to see the dashboard")
        return redirect("/")

    user = User.get_by_id(session["user_id"])
    # TO DO
    # Get all the Recipes and send to the template.

    return render_template("home.html", user=user)

# 02 ROUTES | Render Pages Details PAge for One Recipe
@app.route("/recipes/<recipes_id>")
def recipe_details(recipes_id):
    print("In details: ", recipes_id)
    return render_template("recipe_detail.html")

# 03 ROUTES | Render Page with Create Form
@app.route("/recipes/new")
def create_page(recipes_id):
    print("In create route.")
    return render_template("create_recipe.html")

# 04 ROUTES | Render Page with Edit Form
@app.route("/recipes/edit/<recipes_id>")
def edit_page(recipes_id):
    print("In edit page: ", recipes_id)
    # Need to get that recipe from the database
    # Pass recipe into template
    return render_template("edit_recipe.html")

#GET Action Routes:
# 05 ROUTES | Delete Route (GET request)
@app.route("/recipes/delete/<recipes_id>")
def delete_recipe(recipes_id):
    print("In delete page: ", recipes_id)
    # Call delete method
    return redirect("/recipes")


######## POST ROUTES ########

# 06 ROUTES | CREATE (Process form)
@app.route("/recipes", method=["POST"])
def create_recipe():
    print("In the create process POST route:", request.form)
    return redirect("/recipes")

# 07 ROUTES | UPDATE (Process form)
@app.route("/recipes/update", method=["POST"])
def update_recipe():
    print("In update POST route:", request.form)
    return redirect("/recipes")
