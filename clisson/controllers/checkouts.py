from flask import Blueprint, jsonify, request
from clisson import app, mysql
from clisson.controllers.common import requires_auth

mod_checkouts = Blueprint('checkouts', __name__, url_prefix='/api/v1.0')

@mod_checkouts.route('/checkouts/<int:id>.json', methods=['GET'])
def checkouts(id): 
    cur = mysql.connection.cursor()
    real_id = int(id)
    cur.execute('''SELECT title, author, due_date FROM checkouts 
                   JOIN users on users.ID = checkouts.user_id 
                   JOIN books on books.ID = checkouts.book_id Where checkouts.user_id = {}'''.format(real_id))
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
        try:
            cur = mysql.connection.cursor() 
            cur.execute('''SELECT number_of_copies-COALESCE(SUM(book_id), 0) FROM books INNER 
                           JOIN checkouts ON books.id = checkouts.book_id WHERE books.id = %s''', (book_id,))
            availability = cur.fetchone()
            if availability[0] <= 0:
                return jsonify({'message': 'Cannot checkout this book at this time.', 'status': 400}), 400

            try:
                cur.execute('''INSERT INTO checkouts (user_id, book_id, checkout_date, due_date) 
                               VALUES (%s, %s, NOW(), NOW()+INTERVAL 2 week)''', (user_id, book_id,))
                checkout_id = cur.lastrowid
                mysql.connection.commit()
            except Exception as e:
                mysql.connection.rollback()
                return jsonify({'message': 'Cannot checkout this book at this time, '
                                           'unexpected database error.', 'status': 400}), 400

            cur.execute('''SELECT id, user_id, book_id FROM checkouts 
                           WHERE id = %s''', (checkout_id,))
            row = cur.fetchone()
            return jsonify({'id': row[0], 'user_id': row[1], 'book_id': row[2]})
        except Exception as e:
            return jsonify({'message': 'Unexpected error occured while '
                            'checking out book id {} for user id {}.'.format(book_id, user_id), 'status': 400}), 400
    else:
        return jsonify({'message': 'Invalid json format.', 'status': 400}), 400

@mod_checkouts.route('/checkin.json', methods=['POST'])
def checkin():
    info = request.get_json(force=True, silent=True)
    if info:
        checkout_id = info.get("checkout_id")
        try:
            cur = mysql.connection.cursor()

            cur.execute('''DELETE FROM checkouts WHERE id = %s''', (checkout_id,))
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            return jsonify({'message': 'Cannot checkin this book at this time, '
                                       'unexpected database error.', 'status': 400}), 400
        return jsonify({})
    else:
        return jsonify({'message': 'Invalid json format.', 'status': 400}), 400