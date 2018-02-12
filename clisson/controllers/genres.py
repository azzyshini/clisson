import io
from flask import Blueprint, jsonify, request, send_file
from clisson import app, mysql

mod_genres = Blueprint('genres', __name__, url_prefix='/api/v1.0')

@mod_genres.route('/genres/<int:book_id>.json', methods=['GET'])
def book(book_id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT genre_type FROM book_genre JOIN genre 
                   ON genre.id = book_genre.genre_id  where book_genre.book_id = %s''', (book_id,))
    rows = cur.fetchall()
    if not rows:
        message = "Book with id {} not found".format(book_id)
        return jsonify({'message': message, 'status': 404}), 404
    genre_list = []
    for row in rows:
        genre_list.append({'genre': row[0]})
    return jsonify(genre_list)