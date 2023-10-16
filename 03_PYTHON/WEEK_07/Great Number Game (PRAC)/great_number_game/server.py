from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)    
app.secret_key = 'secret_safe.'
# START CAP


# 01 PAGE
@app.route('/')
def index():
    if "save_num" not in session:
        session["save_num"] = random.randint(1, 100)
    # print(session["save_num"])
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    session["guess_num"] = int(request.form["guess_num"])
    return redirect ('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')


# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.