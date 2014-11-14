#!/usr/bin/env python2

from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from flask.ext.mail import Mail
from settings import DATABASE

import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE['ENGINE'] + '://' + DATABASE['USER'] + ':' + DATABASE['PASSWORD'] + '@' + DATABASE['HOST'] + '/' + DATABASE['NAME']

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '***REMOVED***'
app.config['MAIL_PASSWORD'] = '***REMOVED***'

db = SQLAlchemy(app)
cors = CORS(app, headers=['Allow', 'Authorization', 'Content-Type'])

mail = Mail(app)

if __name__ == '__main__':
	from models import *
	from views import *
	app.debug = True
	app.secret_key = '***REMOVED***'

	port = 80
	if len(sys.argv) > 1:
		port = int(sys.argv[1])

	app.run(host='0.0.0.0', port=port)
