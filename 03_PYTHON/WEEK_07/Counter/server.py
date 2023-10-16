from flask import Flask, render_template, session, redirect # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret_safe.'
# START CAP


# 01 PAGE
@app.route('/')          
def index():

    if "visit" in session:
        session["visit"] = session.get("visit") + 1
        print("key exists!")
    else:
        session["visit"] = 1
        print("key 'visit' does NOT exist.")

    return render_template("index.html")

@app.route('/increment')
def increment():
    session["visit"] += 1
    return redirect ('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')

# 02 PAGE
# @app.route('/destroy_session')          
# def destroy_session():
#     return render_template("index.html")  

# # 03 PAGE
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')

# # 04 PAGE
# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.