from flask import Flask, render_template, request, redirect
from database import SqliteConn


app = Flask(__name__)


def lookup_user(db, first_name):
    query = 'SELECT * FROM users WHERE first_name=?'
    params = (first_name,)
    return db.fetchone(query, params)


def create_user(db, first_name):
    query = 'INSERT INTO users (first_name) VALUES (?)'
    params = (first_name,)
    db.update(query, params)


@app.route("/", methods=['GET'])
def index():
    first_name = 'Jessamyn'
    db = SqliteConn(db_file='flask-simple-example.db')
    db.connect_to_db()
    user = lookup_user(db, first_name)
    return render_template('index.html', user=user)


@app.route("/users/add", methods=['POST'])
def add_user():
    # Test on command line with:
    # curl -vk -X POST --data "first_name=Jessamyn" "http://127.0.0.1:5000/users"
    db = SqliteConn(db_file='flask-simple-example.db')
    db.connect_to_db()
    first_name = request.form['first_name']
    user = lookup_user(db, first_name)
    if not user:
        create_user(db, first_name)
    return redirect('/')