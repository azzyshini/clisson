from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_holds = Blueprint('users', __name__, url_prefix='/api/v1.0')

@mod_holds.route('/holds/<int:id>.json', methods=['GET'])
def holds(id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT title, author FROM holds JOIN users on users.ID = holds.user_id JOIN books on books.ID = holds.book_id Where holds.user_id = %d''', (id,))
    rv = cur.fetchall()
    holds = []
    for row in rv:
        holds.append({'title' : row[0], 'author': row[1]})
    return jsonify(holds)