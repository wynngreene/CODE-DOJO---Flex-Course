from flask import render_template, redirect, session, request, flash
from flask_app import app
# from flask_app.models.user_Model import User
# from flask_bcrypt import Bcrypt        
# bcrypt = Bcrypt(app) 

######## POST ROUTES ########

# 00 ROUTES | Register
@app.route("/")
def register():
    pass
    return render_template("index.html")
    return redirect("index.html")


# 01 ROUTES | Login
@app.route("/")
def login():
    pass
    return render_template("index.html")
    return redirect("index.html")
