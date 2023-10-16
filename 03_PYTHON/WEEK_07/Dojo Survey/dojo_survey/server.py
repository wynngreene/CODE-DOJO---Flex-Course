from flask import Flask, render_template, session, redirect, request # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret_safe.'
# START CAP


# 01 PAGE
@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session["fullname"] = request.form["fullname"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect ('/results')

@app.route('/results')
def results():
    return render_template("results.html")


# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.