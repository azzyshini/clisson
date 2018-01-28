from functools import wraps
from flask import request, Response
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
    return Response('Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated