from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user_Model import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

# GET ROUTES
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    
    if not User.validate_register(request.form):
        return redirect("/")
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)
    session["user.id"] = id

    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    pass


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : session["user_id"]
    }
    return render_template("dashboard.html", user=User.get_by_id(data))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")