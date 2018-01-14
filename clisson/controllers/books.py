from flask import Blueprint, jsonify, request

mod_books = Blueprint('books', __name__, url_prefix='/api/v1.0')

@mod_books.route('/books.json', methods=['GET'])
def books():
    return jsonify([{'id': 1}, {'id': 2}])

@mod_books.route('/books/<int:id>.json', methods=['GET'])
def book(id):
    return jsonify({'id': 1})