from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.cookie_order_Model import Cookie_order


# GET ROUTES
@app.route("/")
def index():
    print("skip me")
    return redirect("/cookies")

@app.route("/cookies")
def cookies():
    # dojos = Dojo.get_all()
    print("In the index route")
    return render_template("index.html")

@app.route("/cookies/new")
def new_page():
    print("In the new page route")
    return render_template("new_order.html")

@app.route("/cookies/edit/<order_id>")
def edit_page(order_id):
    print("In the edit page route with id", order_id)
    return render_template("edit_order.html")

# POST (ACTION) ROUTES
@app.route("/cookies/create", methods=["POST"])
def create_order():
    print("In create POST route")
    print(request.form)
    Cookie_order.save()
    return redirect("/cookies")

@app.route("/cookies/update", methods=["POST"])
def update_order():
    print("In update POST route")
    print(request.form)
    return redirect("/cookies")