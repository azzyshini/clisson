from flask import Blueprint, jsonify, request
from clisson import app, mysql
from clisson.controllers.common import requires_auth

mod_checkouts = Blueprint('checkouts', __name__, url_prefix='/api/v1.0')

@mod_checkouts.route('/checkouts/<int:id>.json', methods=['GET'])
def checkouts(id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT title, author, due_date FROM checkouts JOIN users on users.ID = checkouts.user_id JOIN books on books.ID = checkouts.book_id Where checkouts.user_id = %d''', (id,))
    rv = cur.fetchall()
    checkouts = []
    for row in rv:
        checkouts.append({'title': row[0], 'author': row[1], 'due_date': row[2]})
    return jsonify(checkouts)

@mod_checkouts.route('/checkout.json', methods=['POST'])
def checkout(): 
    info = request.get_json(force=True, silent=True)
    if info:
        user_id = info.get("user_id")
        book_id = info.get("book_id")
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO checkouts (user_id, book_id, due_date) VALUES (%s, %s, NOW()+INTERVAL 2 week)''', (user_id, book_id,))
        cur.execute('''SELECT id, user_id, book_id FROM chekcouts WHERE user_id = %s AND book_id = %s''', (user_id, book_id,))
        row = cur.fetchone()
        return jsonify({'id': row[0], 'user_id': row[1], 'book_id': row[2] 'status': 200}), 200