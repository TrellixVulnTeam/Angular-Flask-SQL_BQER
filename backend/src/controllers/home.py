from flask import  jsonify, request, Blueprint
from ..application import app
bp = Blueprint('api', __name__,
                        template_folder='templates')

@bp.route('/')
def index():
	return jsonify("Welcome to the Home Controller")

@bp.route('/test')
def test():
	return jsonify("holii :)")

app.register_blueprint(bp, url_prefix='/home')
