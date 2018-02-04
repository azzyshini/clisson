from flask import Blueprint, jsonify, request
from clisson import app, mysql
from clisson.controllers.common import requires_auth

mod_holds = Blueprint('holds', __name__, url_prefix='/api/v1.0')

@mod_holds.route('/holds/<int:id>.json', methods=['GET'])
def holds(id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT title, author FROM holds JOIN users on users.ID = holds.user_id JOIN books ON books.ID = holds.book_id WHERE holds.user_id = %d''', (id,))
    rv = cur.fetchall()
    holds = []
    for row in rv:
        holds.append({'title' : row[0], 'author': row[1]})
    return jsonify(holds)

@mod_holds.route('/hold.json', methods=['POST'])
def hold(): 
    info = request.get_json(force=True, silent=True)
    if info:
        user_id = info.get("user_id")
        book_id = info.get("book_id")
        cur = mysql.connection.cursor()
        cur.execute('''SELECT COALESCE(SUM(user_id), 0) FROM holds WHERE user_id = %s''', (user_id,))
        number = cur.fetchone()
        if number[0] >= 50:
            return jsonify({'message': 'You have reached the limit to the number of holds you can have at one time.', 'status': 400}), 400
        cur.execute('''SELECT COALESCE(SUM(book_id), 0) FROM holds WHERE user_id = %s''', (user_id,))
        number = cur.fetchone()
        if number[0] >= 1:
            return jsonify({'message': 'You already have this book on hold.', 'status': 400}), 400
        cur.execute('''INSERT INTO holds (user_id, book_id) VALUES (%s, %s)''', (user_id, book_id,))
        cur.execute('''SELECT holds.id, first_name, last_name, title, author_name FROM holds 
                       JOIN users ON users.id = holds.user_id 
                       JOIN books ON books.id = holds.book_id 
                       WHERE user_id = %s AND book_id = %s''', (user_id, book_id,))
        row = cur.fetchone()
        return jsonify({'id': row[0], 'first_name': row[1], 'last_name': row[2], 'title': row[3], 'author': row[4]})