from flask import render_template, redirect, session, request, flash
from flask_app import app
# from flask_app.models.user_Model import User
# from flask_bcrypt import Bcrypt        
# bcrypt = Bcrypt(app) 

# GET ROUTES
@app.route("/")
def index():
    return render_template("index.html")