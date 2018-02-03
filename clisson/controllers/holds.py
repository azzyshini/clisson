from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_holds = Blueprint('holds', __name__, url_prefix='/api/v1.0')

@mod_holds.route('/holds/<int:id>.json', methods=['GET'])
def holds(id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT title, author FROM holds JOIN users on users.ID = holds.user_id JOIN books on books.ID = holds.book_id Where holds.user_id = %d''', (id,))
    rv = cur.fetchall()
    holds = []
    for row in rv:
        holds.append({'title' : row[0], 'author': row[1]})
    return jsonify(holds)

@mod_holds.route('/hold.json', methods=['POST'])
@requires_auth
def hold(): 
	info = request.get_json(force=True, silent=True)
	if info:
		user_id = info.get("user_id")
		book_id = info.get("book_id")
    	cur = mysql.connection.cursor()
    	cur.execute('''INSERT INTO checkouts (user_id, book_id) VALUES (%s, %s)''', (user_id, book_id,))
    	cur.execute('''SELECT first_name, last_name, title, author FROM holds JOIN users ON users.id = holds.user_id JOIN books ON books.id = holds.book_id WHERE user_id = %s AND book_id = %s''', (user_id, book_id,))
    	rv = cur.fetchone()
    	return jsonify({'first_name': row[0], 'last_name': row[1], 'title': row[2], 'author': row[3]})