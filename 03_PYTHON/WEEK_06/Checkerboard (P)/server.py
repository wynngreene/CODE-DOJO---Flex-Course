from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# START CAP


# 00 PAGE
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", x_row=8, y_col=8, color_01="red", color_02="blue")  # Return the string 'Hello World!' as a response

# 01 PAGE
@app.route('/<int:x>/') 
def checker_x(x):
    return render_template("index.html", x_row=x, y_col=8, color_01="red", color_02="blue")

# 02 PAGE
@app.route('/<int:x>/<int:y>')
def checker_x_y(x, y):
    return render_template("index.html",x_row=x, y_col=y, color_01="red", color_02="blue")

# 03 PAGE
@app.route('/<int:x>/<int:y>/<string:color_01>') 
def checker_x_y_a(x,y, first):
    return render_template("index.html",x_row=x, y_col=y, color_01=first, color_02="blue")

# 04 PAGE
@app.route('/<int:x>/int:y>/<string:color_01>/<string:color_02>') 
def checker_x_y_a_b(x,y, first, second):
    return render_template("index.html",x_row=x, y_col=y, color_01=first, color_02=second)

# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.