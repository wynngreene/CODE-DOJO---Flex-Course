from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# START CAP


# 01 PAGE
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

# 02 PAGE
@app.route('/play/') 
def play():
    return render_template("play.html")

# 03 PAGE
@app.route('/play/<int:multiple_01>') 
def play_number(multiple_01):
    return render_template("play_num.html",multiple_02=multiple_01)

# 03 PAGE
@app.route('/play/<int:multiple_01>/<string:color_01>') 
def play_num_color(multiple_01, color_01):
    return render_template("play_num_color.html",multiple_02=multiple_01, color_02=color_01)


# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.