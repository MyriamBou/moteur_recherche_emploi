import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM data-mangodb').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)



def get_db_connection():
    conn = sqlite3.connect('data-mangodb')
    conn.row_factory = sqlite3.Row
    return conn

    #lignes de commandes: 
    # export FLASK_ENV=development
    # export FLASK_APP=test.py
    #flask run

    #client = MongoClient("localhost", 27017)
    #db = client["data-mangodb"]
    #CollectionMaongodb1 = db["CollectionMaongodb1"]