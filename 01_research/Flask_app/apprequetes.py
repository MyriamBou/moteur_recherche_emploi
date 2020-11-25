#Une application client-serveur pour permettre de faire des requetes à la BDD. 
#créer une page permettant de faire une recherche textuelle sur l'ensemble des documents récupérés
#et de retourner la liste des 10 premiers documents les plus pertinents.
import json
import pymongo
from flask import flask, request, render_template #First we imported the Flask class
app = Flask(__name__)     #Next we create an instance of this class.

client = MongoClient("localhost", 27017)
db = client["data-mangodb"]
CollectionMaongodb1 = db["CollectionMaongodb1"]

@app.route('/')          #use the route() decorator to tell Flask what URL should trigger our function
def Search():
    return 'Résultat de recherche'

 #The function is given a name which is also used to generate URLs for that particular function, 
 #and returns the message we want to display in the user’s browser.
    
    #lignes de commandes: 
    # export FLASK_ENV=development
    # export FLASK_APP=apprequetes.py
    #flask run