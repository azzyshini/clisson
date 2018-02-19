import io
from flask import Blueprint, jsonify, request, send_file
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
    cur.execute('''SELECT title, author_name,number_of_copies-COALESCE(SUM(book_id), 0) AS availability FROM books 
                   JOIN checkouts ON books.id = checkouts.book_id  where books.id = %s''', (book_id,))
    row = cur.fetchone()
    if not row:
        message = "Book with id {} not found".format(book_id)
        return jsonify({'message': message, 'status': 404}), 404
    avail = int(row[2])
    return jsonify({'title': row[0], 'author_name': row[1], 'availability': avail})

@mod_books.route('/books/cover/<int:book_id>', methods=['GET'])
def book_cover(book_id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT book_cover, book_cover_mimetype FROM books WHERE id = %s''', (new_id,))
    row = cur.fetchone()
    if row:
        cover = row[0]
        mimetype = row[1]
        if cover:
            return send_file(io.BytesIO(cover), attachment_filename='book_cover_{}'.format(book_id), mimetype=mimetype)
    message = "Book cover with id {} not found".format(book_id)
    return message, 404

@mod_books.route('/books/search.json', methods=['GET'])
def book_search():
    cur = mysql.connection.cursor()
    search = request.args.get('search')
    cur.execute("""SELECT id, title, author_name FROM books 
                   WHERE title LIKE concat('%%',%s,'%%')""", (search,))
    rows = cur.fetchall()
    results = []
    if not rows:
        message = "No search results found".format(search)
        return jsonify({'message': message, 'status': 200}), 200
    for row in rows:
        results.append({'id' : row[0], 'title': row[1], 'author_name': row[2]})
    return jsonify(results)