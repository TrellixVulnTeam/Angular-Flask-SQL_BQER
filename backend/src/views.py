from .application import app
from flask import jsonify

@app.route("/")
def index():
    return jsonify("Hello World!")

from .controllers.home import *
