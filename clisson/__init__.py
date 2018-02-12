import os
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

clisson_env = os.getenv('CLISSON_ENV', 'Dev') + 'Config'
app.config.from_object('clisson.config.' + clisson_env)

from clisson.controllers import *

# Register blueprints
app.register_blueprint(mod_books)
app.register_blueprint(mod_users)
app.register_blueprint(mod_checkouts)
app.register_blueprint(mod_holds)
app.register_blueprint(mod_auth)
app.register_blueprint(mod_genre)