from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_books = Blueprint('books', __name__, url_prefix='/api/v1.0')

@mod_books.route('/books.json', methods=['GET'])
def books():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, title, author_name FROM books''')
    rv = cur.fetchall()
    boooks = []
    for row in rv:
        boooks.append({'id' : row[0], 'title': row[1], 'author_name': row[2]})
    return jsonify(boooks)

@mod_books.route('/books/<int:book_id>.json', methods=['GET'])
def book(book_id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, title, author_name FROM books where id = book_id''')
    rone = cur.fetchone()
    return jsonify(rone)
