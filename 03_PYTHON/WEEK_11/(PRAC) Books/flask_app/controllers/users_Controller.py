from flask import render_template, redirect, request
from flask_app import app
#from flask_app.models.cookie_order_Model import Cookie_order

# GET ROUTES
@app.route("/")

@app.route("/user")
def index():
    print("In the index route")
    return render_template("index.html")

@app.route("/user/new")
def new_page():
    print("In the new page route")
    return render_template("new_order.html")

@app.route("/user/edit/<order_id>")
def edit_page(order_id):
    print("In the edit page route with id", order_id)
    return render_template("edit.html")


# POST (ACTION) ROUTES
@app.route("/cookies/create", methods=["POST"])
def create_user():
    print("In create POST route")
    return redirect("/cookies/new")

@app.route("/cookies/update", methods=["POST"])
def update_user():
    print("In update POST route")
    return redirect(f"/cookies/edit/{request.form['id']}")