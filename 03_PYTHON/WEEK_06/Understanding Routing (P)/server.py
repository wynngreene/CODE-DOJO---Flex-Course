from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# UNDERSTANDING ROUTING
# 01.localhost:5000/ - 
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello World!"  # Return the string 'Hello World!' as a response

# 02.localhost:5000/dojo - 
@app.route('/dojo')
def success():
    return "Dojo!"

# 03.localhost:5000/say/<name> - 
@app.route('/say/<string:name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print (name)
    return "Hi, " + name

# 04.localhost:5000/repeat/num/<name> - 
@app.route('/repeat/<int:num>/<string:phrase>') 
def repeatMe(phrase, num):
    return f"Yo, {phrase * num}!"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# app.run(debug=True, host="localhost", port=8000)
