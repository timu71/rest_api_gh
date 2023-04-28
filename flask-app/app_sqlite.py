from flask import Flask, redirect, jsonify, request
import os
import json
import sqlite3
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')





def get_books_db_all():
    conn = sqlite3.connect('database/test.db')
    cursor = conn.execute("SELECT * from books")
    books = []

    for row in cursor:  

        book = {'ID' : row[0], 'title' : row[1], 'year_written' : row[2], 'author' : row[3]}

        books.append(book)
    print(len(books))
    return books
def get_book_db_by_id(id):
    conn = sqlite3.connect('database/test.db')
    cursor = conn.execute("SELECT * from books where id = %s" % id)
    books = []

    for row in cursor:  

        book = {'ID' : row[0], 'title' : row[1], 'year_written' : row[2], 'author' : row[3]}
        books.append(book)
    return books


user1 = {"username" : "timu", "password" : "dontknow" }
user2 = {"username" : "timu2", "password" : "dontknow2" }
users = []
users.append(user1)
users.append(user2)
@app.route('/', methods = ['GET'])
def hello_world():
    # print(json.dumps(get_books_db_all(conn)) )
    if request.method == 'GET':
        return "Hello World"
    else:
        return json.dumps(users)
@app.route('/books', methods = ['GET'])
def books_all():
    # print(json.dumps(get_books_db_all(conn)) )
    if request.method == 'GET':
        return json.dumps(get_books_db_all()) 
        # return redirect(os.environ.get("REDIRECT_TO", "https://www.digitalocean.com"), code=301)
    else:
        return json.dumps(users)
@app.route('/books/<int:id>')
def books_by_id(id):
    # print(json.dumps(get_books_db_all(conn)) )
    if request.method == 'GET':
        print(get_book_db_by_id(id))
        return get_book_db_by_id(id)

    else:
        return json.dumps(users)
    # if request.method == "GET":
    # return json.dumps(get_books_db_all(conn))
    # elif request.method == "POST":
        
    #     return jsonify(users[id])
        

    # return redirect(os.environ.get("REDIRECT_TO", "https://www.digitalocean.com"), code=301)
    # return redirect(os.environ.get("REDIRECT_TO", "https://www.digitalocean.com"), code=301)
# @app.route(/book/<int:id>)
# def book_id(id):

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # print(json.dumps(get_books_db_all(conn)))
