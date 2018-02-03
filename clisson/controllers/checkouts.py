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
@requires_auth
def checkout(): 
	info = request.get_json(force=True, silent=True)
	error = none
	if info:
		user_id = info.get("user_id")
		book_id = info.get("book_id")
    	cur = mysql.connection.cursor()
    	cur.execute('''INSERT INTO checkouts (user_id, book_id, due_date) VALUES (%s, %s, NOW()+INTERVAL 2 week)''', (user_id, book_id,))
    	cur.execute('''SELECT first_name, last_name, title, author, due_date FROM chekcouts JOIN users ON users.id = checkouts.user_id JOIN books ON books.id = checkouts.book_id WHERE user_id = %s AND book_id = %s''', (user_id, book_id,))
    	rv = cur.fetchone()
    	return jsonify({'first_name': row[0], 'last_name': row[1], 'title': row[2], 'author': row[3], 'due_date': row[4]})
