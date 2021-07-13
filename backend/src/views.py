from .application import app
from flask import jsonify
from .database import con

@app.route("/")
def index():
    return jsonify("Hello World!")

@app.route("/sql")
def sqlTest():
    validConnection = bool(con and con.connection.is_valid)
    #   SQL Example
    # rs = con.execute('SELECT * from testTable')
    # for row in rs:
    #     rowItem = row["col1"]
    return jsonify(validConnection)

from .controllers.home import *