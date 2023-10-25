from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'secret_safe.'

#Global Stuff 


# 01 PAGE 
@app.route('/')                           
def index():
    print(session.get("gold"))
    print(session.get("activity"))
    
    return render_template('index.html')

# 02 PAGE
@app.route('/process_money', methods=["POST"])          
def process_money():
    
    if request.form["building"] == "farm":
        session["gold"] += 20
        session["activity"] += "<ul><li>WAHT</li></ul>"
        
        print("my gold from farm!")
        print(session.get("gold"))
        
        
    elif request.form["building"] == "cave":
        print("my gold from cave!")
        session["gold"] += 10
        print(session.get("gold"))
        
    elif request.form["building"] == "house":
        print("my gold from house!")
        session["gold"] += 5
        print(session.get("gold"))
                
    elif request.form["building"] == "casino":
        print("my gold from casino!")
        session["gold"] -= 50
        print(session.get("gold"))
                
    else:
        print("my gold is changing!")
    
    return redirect ('/') 

# END CAP
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.