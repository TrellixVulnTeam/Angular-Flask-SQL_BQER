#!/usr/bin/python3.7
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from src.main import application as application
application.secret_key = 'anything you wish'

