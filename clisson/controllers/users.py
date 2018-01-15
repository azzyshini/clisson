from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_users = Blueprint('users', __name__, url_prefix='/api/v1.0')

@mod_users.route('/users.json', methods=['GET'])
def users(): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, email, first_name, last_name FROM users ORDER BY id DESC''')
    rv = cur.fetchall()
    people = []
    for row in rv:
        people.append({'id' : row[0], 'email': row[1], 'first_name': row[2], 'last_name' : row[3]})
    return jsonify(people)