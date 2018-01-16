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
app.register_blueprint(mod_user_types)
app.register_blueprint(mod_genre)
app.register_blueprint(mod_book_genre)
app.register_blueprint(mod_checkouts)
app.register_blueprint(mod_holds)
