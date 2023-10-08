from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# START CAP


# 00 PAGE
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    
    users_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template("index.html",student_users = users_info)  # Return the string 'Hello World!' as a response


# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.