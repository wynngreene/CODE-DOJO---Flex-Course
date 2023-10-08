from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# START CAP


# 01 PAGE
@app.route('/')
def index():
    return render_template("index.html")

# # 02 PAGE
# @app.route('/<int:x_number>/<int:y_number>/<string:color_sqr_01/<string:color_sqr_02>')        
# def checkers(x_number, y_number, color_sqr_01, color_sqr_02):
#     return render_template("checkers.html",x_number=x_number, y_number=y_number, color_sqr_01=color_sqr_01, color_sqr_02=color_sqr_02)


# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.