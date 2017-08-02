from flask import Flask, render_template, request, redirect
from database import SqliteConn


app = Flask(__name__)

db = SqliteConn(db_file='flask-simple-example.db')
db.connect_to_db()


def lookup_user(db, first_name, last_name):
    query = 'SELECT * FROM users WHERE first_name=? AND last_name=?'
    params = (first_name, last_name)
    return db.first(query, params)


def all_users(db):
    query = 'SELECT * FROM users'
    return db.all(query, ())


def create_user(db, first_name, last_name):
    query = 'INSERT INTO users (first_name, last_name) VALUES (?, ?)'
    params = (first_name, last_name)
    db.update(query, params)


@app.route("/", methods=['GET'])
def index():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    user = None
    if first_name and last_name:
        user = lookup_user(db, first_name, last_name)
    users = all_users(db)
    return render_template('index.html', user=user, users=users)


@app.route("/users/add", methods=['POST'])
def add_user():
    # Test on command line with:
    # curl -vk -X POST --data "first_name=Jessamyn" "http://127.0.0.1:5000/users"
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user = lookup_user(db, first_name, last_name)
    if not user and first_name and last_name:
        create_user(db, first_name, last_name)
    return redirect('/')