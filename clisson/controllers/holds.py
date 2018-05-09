from flask import Blueprint, jsonify, request
from clisson import app, mysql
from clisson.controllers.common import requires_auth

mod_holds = Blueprint('holds', __name__, url_prefix='/api/v1.0')

@mod_holds.route('/holds/<int:id>.json', methods=['GET'])
def holds(id): 
    cur = mysql.connection.cursor()
    real_id = int(id)
    cur.execute('''SELECT holds.id, title, author_name FROM holds 
                   JOIN users on users.ID = holds.user_id 
                   JOIN books ON books.ID = holds.book_id WHERE holds.user_id = {}'''.format(real_id))
    rv = cur.fetchall()
    holds = []
    for row in rv:
        holds.append({'id' : row[0], 'title' : row[1], 'author': row[2]})
    return jsonify(holds)

@mod_holds.route('/hold.json', methods=['POST'])
def hold(): 
    info = request.get_json(force=True, silent=True)
    if info:
        user_id = info.get("user_id")
        book_id = info.get("book_id")
        print(str(user_id) + " and " + str(book_id))
        try:
            cur = mysql.connection.cursor()
            cur.execute('''SELECT COALESCE(SUM(user_id), 0) FROM holds WHERE user_id = %s''', (user_id,))
            number = cur.fetchone()

            if number[0] >= 50:
                return jsonify({'message': 'You have reached the limit to the number of '
                                           'holds you can have at one time.', 'status': 400}), 400
            cur.execute('''SELECT COALESCE(SUM(book_id), 0) FROM holds 
                           WHERE user_id = %s AND book_id = %s''', (user_id, book_id,))
            number = cur.fetchone()

            if number[0] >= 1:
                return jsonify({'message': 'You already have this book on hold.', 'status': 400}), 400

            try:
                cur.execute('''INSERT INTO holds (user_id, book_id) VALUES (%s, %s)''', (user_id, book_id,))
                mysql.connection.commit()
                holds_id = cur.lastrowid
            except Exception as e:
                raise e
                mysql.connection.rollback()
                return jsonify({'message': 'Unable to place a hold on this book, unepected database error.', 'status': 400}), 400

            cur.execute('''SELECT holds.id, first_name, last_name, title, author_name FROM holds 
                           JOIN users ON users.id = holds.user_id 
                           JOIN books ON books.id = holds.book_id 
                           WHERE holds.id = %s''', (holds_id,))
            row = cur.fetchone()
            return jsonify({'id': row[0], 'first_name': row[1], 'last_name': row[2], 'title': row[3], 'author': row[4]})
        except Exception as e:
            raise e
            return jsonify({'message': 'Unexpected error occured while '
                            'placing a hold on book id {} for user id {}.'.format(book_id, user_id), 'status': 400}), 400
    else: 
        return jsonify({'message': 'Invalid json format', 'status': 400}), 400 

@mod_holds.route('/unhold.json', methods=['POST'])
def checkin():
    info = request.get_json(force=True, silent=True)
    if info:
        hold_id = info.get("hold_id")
        try:
            cur = mysql.connection.cursor()
            cur.execute('''DELETE FROM holds WHERE id = %s''', (hold_id,))
            mysql.connection.commit()
        except Exception as e:
            raise e
            mysql.connection.rollback()
            return jsonify({'message': 'Cannot unhold this book at this time, '
                                       'unexpected database error.', 'status': 400}), 400
        return jsonify({})
    else:
        return jsonify({'message': 'Invalid json format.', 'status': 400}), 400