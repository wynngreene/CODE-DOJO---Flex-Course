from flask import Flask, render_template, session, redirect
import random
app = Flask(__name__)    
app.secret_key = 'secret_safe.'
# START CAP


# 01 PAGE
@app.route('/')
def index():
    save_num = random.randint(1, 100)
    print(save_num)


    return render_template("index.html")

# @app.route('/increment')
# def increment():
#     session["visit"] += 1
#     return redirect ('/')

# @app.route('/reset')
# def reset():
#     session.clear()
#     return redirect ('/')


# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.