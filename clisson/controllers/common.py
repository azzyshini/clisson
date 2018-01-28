from functools import wraps
from flask import request, jsonify
from clisson import mysql


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, email, first_name, last_name FROM users Where username = %s AND password = %s''', (username, password,))
    row = cur.fetchone()
    if row: 
        return True
    else:
        return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    message = "You do not have security access for this. Please log in."
    return jsonify({'message': message, 'status': 403}), 403
    
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated