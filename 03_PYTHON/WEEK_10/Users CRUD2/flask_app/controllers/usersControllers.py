from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User

@app.route("/")
def index():
    theUsers = User.get_all()
    return render_template("index.html", all_users=theUsers)

# @app.route("/user/<int:user_id>")
# def view_user(user_id):
#     theUser = User.get_one(user_id)
#     return render_template()

# @app.route('/user/new')
# def new_user():
#     return render_template("new_user.html")

# @app.route('/user/create',methods=['POST'])
# def create():
#     print(request.form)
#     User.save(request.form)
#    return redirect('/users')