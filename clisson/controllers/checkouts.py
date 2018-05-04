from flask import Blueprint, jsonify, request
from clisson import app, mysql
from clisson.controllers.common import requires_auth

mod_checkouts = Blueprint('checkouts', __name__, url_prefix='/api/v1.0')

@mod_checkouts.route('/checkouts/<int:id>.json', methods=['GET'])
def checkouts(id): 
    cur = mysql.connection.cursor()
    real_id = int(id)
    cur.execute('''SELECT checkouts.id, title, author_name, due_date FROM checkouts 
                   JOIN users on users.ID = checkouts.user_id 
                   JOIN books on books.ID = checkouts.book_id Where checkouts.user_id = {}'''.format(real_id))
    rv = cur.fetchall()
    checkouts = []
    for row in rv:
        checkouts.append({'id': row[0], 'title': row[1], 'author': row[2], 'due_date': row[3]})
    return jsonify(checkouts)

@mod_checkouts.route('/checkout.json', methods=['POST'])
def checkout():
    info = request.get_json(force=True, silent=True)
    if info:
        user_id = int(info.get("user_id"))
        book_id = int(info.get("book_id")) 
        print(user_id + " and " + book_id)
        try:
            cur = mysql.connection.cursor() 
            cur.execute('''SELECT number_of_copies-count(book_id) FROM books INNER 
                           JOIN checkouts ON books.id = checkouts.book_id WHERE books.id = {}'''.format(book_id))
            availability = cur.fetchone()
            if availability[0] <= 0:
                return jsonify({'message': 'Cannot checkout this book at this time.', 'status': 400}), 400
            cur.execute('''SELECT number_of_copies-COALESCE(SUM(book_id), 0) FROM books INNER 
                           JOIN holds ON books.id = holds.book_id WHERE books.id = {}'''.format(book_id))
            try:
                cur.execute('''INSERT INTO checkouts (user_id, book_id, checkout_date, due_date) 
                               VALUES ({}, {}, NOW(), NOW()+INTERVAL 2 week)'''.format(user_id, book_id))
                checkout_id = cur.lastrowid
                mysql.connection.commit()
            except Exception as e: 
                raise e
                mysql.connection.rollback()
                return jsonify({'message': 'Cannot checkout this book at this time, '
                                           'unexpected database error.', 'status': 400}), 400
            cur.execute('''SELECT id, user_id, book_id FROM checkouts 
                           WHERE id = {}'''.format(checkout_id))
            row = cur.fetchone() 
            return jsonify({'id': row[0], 'user_id': row[1], 'book_id': row[2]})
        except Exception as e:
            raise e
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