from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# START CAP


# 00 PAGE
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

# 01 PAGE
@app.route('/<int:multiple_01>/') 
def checker_x(multiple_01):
    return render_template("checker_x.html",x_number=multiple_01)

# 02 PAGE
@app.route('/<int:multiple_01>/<int:multiple_02>') 
def checker_x_y(multiple_01, multiple_02):
    return render_template("checker_x_y.html",x_number=multiple_01, y_number=multiple_02)

# 03 PAGE
@app.route('/<int:multiple_01>/<int:multiple_02>/<string:color_01>') 
def checker_x_y_a(multiple_01,multiple_02, color_01):
    return render_template("checker_x_y_a.html",x_number=multiple_01, y_number=multiple_02, a_color=color_01)

# 04 PAGE
@app.route('/<int:multiple_01>/int:multiple_02>/<string:color_01>/<string:color_02>') 
def checker_x_y_a_b(multiple_01,multiple_02, color_01, color_02):
    return render_template("checker_x_y_a_b.html",x_number=multiple_01, y_number=multiple_02, a_color=color_01, b_color=color_02)

# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.