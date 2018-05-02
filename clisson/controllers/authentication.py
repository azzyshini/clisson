from flask import Blueprint, jsonify, request
from clisson import app, mysql

mod_auth = Blueprint('auth', __name__, url_prefix='/api/v1.0')

@mod_auth.route('/auth/login.json', methods=['POST'])
def auth(): 
    creds = request.get_json(force=True, silent=True)
    error = None
    #method is only post, so the next line will always be true
    if request.method == "POST":
        if creds:
            username = creds.get("username")
            password = creds.get("password")
            cur = mysql.connection.cursor()
            cur.execute('''SELECT id, email, first_name, last_name, user_type_id FROM users Where username = %s AND password = %s''', (username, password,))
            row = cur.fetchone()
            if row: 
                return jsonify({'id': row[0], 'email': row[1], 'first_name': row[2], 'last_name': row[3], 'user_type_id':row[4], 'authenticated': True})
            else:
                error = 'Invalid username or password. Please try again.'
        else:
            error = 'Invalid username or password. Please try again.'
    return jsonify({'message': error, 'status': 401}), 401