from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_users = Blueprint('users', __name__, url_prefix='/api/v1.0')

@mod_users.route('/user/<string:username>.json', methods=['GET'])
def user_by_name(username): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, email, first_name, last_name FROM users Where username = %s''', (username,))
    rv = cur.fetchone()
    return jsonify({'id': row[0], 'email': row[1], 'first_name': row[2], 'last_name': row[3]})

@mod_users.route('/user/<int:user_id>.json', methods=['GET'])
def user_by_id(user_id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, email, first_name, last_name FROM users Where id = %d''', (user_id,))
    rv = cur.fetchone()
    return jsonify({'id': row[0], 'email': row[1], 'first_name': row[2], 'last_name': row[3]})