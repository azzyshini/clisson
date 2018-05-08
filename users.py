from flask import Blueprint, jsonify, request
from clisson import app, mysql
from clisson.controllers.common import requires_auth

mod_users = Blueprint('users', __name__, url_prefix='/api/v1.0')

@mod_users.route('/users/<string:username>.json', methods=['GET'])
def user_by_name(username): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, email, first_name, last_name, user_type_id FROM users WHERE username = %s''', (username,))
    row = cur.fetchone()
    if not row:
        message = "User with username {} not found".format(username)
        return jsonify({'message': message, 'status': 404}), 404
    return jsonify({'id': row[0], 'email': row[1], 'first_name': row[2], 'last_name': row[3], 'user_type_id': row[4]})

@mod_users.route('/usersbyid/<int:user_id>.json', methods=['GET'])
def user_by_id(user_id): 
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, email, first_name, last_name, user_type_id FROM users WHERE username = %s''', (user_id,))
    row = cur.fetchone()
    if not row:
        message = "User with id {} not found".format(user_id)
        return jsonify({'message': message, 'status': 404}), 404
    return jsonify({'id': row[0], 'email': row[1], 'first_name': row[2], 'last_name': row[3], 'user_type_id': row[4]})