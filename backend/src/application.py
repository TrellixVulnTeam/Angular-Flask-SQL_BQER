from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

