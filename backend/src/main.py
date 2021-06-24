from .application import app as application

from flask import render_template, request, redirect, make_response, jsonify

from .views import *

if __name__ == '__main__':
    application.run()
