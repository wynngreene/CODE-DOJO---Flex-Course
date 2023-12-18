from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.recipe_Model import Recipe
from flask_app.models.user_Model import User

from flask import flash

######## BLEND ROUTES ########

# 01 ROUTES | 
@app.route("/dashboard_02")
def recipes_home():
    # if "user_id" not in session:
    #     return redirect("/")
    # user = User.get_by_id(session["user_id"])
    # print("I got my 01 LIST of", user)

    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : session["user_id"]
    }

    recipes = Recipe.get_all()
    print("I got my 02 LIST of", recipes)

    return render_template("home.html", user=User.get_by_id(data), recipes=recipes)

######## GET ROUTES ########

# 02 ROUTES | Render Pages Details PAge for One Recipe
@app.route("/recipes/<recipe_id>")
def recipe_details(recipe_id):
    print("In details PLEASE : ", recipe_id)
    
    recipe = Recipe.get_one_recipe_id(recipe_id)

    return render_template("recipe_detail.html", recipe=recipe)

# 03 ROUTES | Render Page with Create Form
@app.route("/recipes/new")
def create_page():
    print("In create route.")
    print(session["user_id"])
    user = session["user_id"]
    
    return render_template("create_recipe.html", user=user)

# 04 ROUTES | Render Page with Edit Form
@app.route("/recipes/edit/<recipe_id>")
def edit_page(recipe_id):
    print("In edit page: ", recipe_id)

    recipe = Recipe.get_one_recipe_id(recipe_id)
    # Need to get that recipe from the database
    # Pass recipe into template
    return render_template("edit_recipe.html", recipe=recipe)

#GET Action Routes:
# 05 ROUTES | Delete Route (GET request)
@app.route("/recipes/delete/<recipe_id>")
def delete_recipe(recipe_id):
    print("In delete page: ", recipe_id)
    # Call delete method
    recipe = Recipe.delete_by_recipe_id(recipe_id)
    
    return redirect("/dashboard_02")


######## POST ROUTES ########

# 06 ROUTES | CREATE (Process form)
@app.route("/recipes", methods=["POST"])
def create_recipe():
    print("What am I ADDING Here:", request.form)
    print(session)

    Recipe.save(request.form)
    return redirect("/dashboard_02")

# 07 ROUTES | UPDATE (Process form)
@app.route("/recipes/update", methods=["POST"])
def update_recipe():
    print("In update POST route:", request.form)
    return redirect("/recipes")
