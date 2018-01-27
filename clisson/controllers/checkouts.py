from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_checkouts = Blueprint('checkouts', __name__, url_prefix='/api/v1.0')

@mod_checkouts.route('/checkouts/<int:id>.json', methods=['GET'])
def checkouts(id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT title, author, due_date FROM checkouts JOIN users on users.ID = checkouts.user_id JOIN books on books.ID = checkouts.book_id Where checkouts.user_id = %d''', (id,))
    rv = cur.fetchall()
    checkouts = []
    for row in rv:
        checkouts.append({'title' : row[0], 'author': row[1], 'due_date': row[2]})
    return jsonify(checkouts)