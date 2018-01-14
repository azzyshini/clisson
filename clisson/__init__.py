from flask import Flask

app = Flask(__name__)

from clisson.controllers import *

# Register blueprints
app.register_blueprint(mod_books)