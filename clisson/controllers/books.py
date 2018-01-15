from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_books = Blueprint('books', __name__, url_prefix='/api/v1.0')

@mod_books.route('/books.json', methods=['GET'])
def books():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM books''')
    rv = cur.fetchall()
    return str(rv)

@mod_books.route('/books/<int:book_id>.json', methods=['GET'])
def book(book_id):
    return jsonify({'id': book_id})
