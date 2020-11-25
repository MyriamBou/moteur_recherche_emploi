from flask import Flask   #First we imported the Flask class
app = Flask(__name__)     #Next we create an instance of this class.

@app.route('/')           #use the route() decorator to tell Flask what URL should trigger our function
def hello_world():
    return 'Hello, World!'

 #The function is given a name which is also used to generate URLs for that particular function, 
 #and returns the message we want to display in the user’s browser.
    
    #lignes de commandes: export flask_app=hello.py
    #flask run