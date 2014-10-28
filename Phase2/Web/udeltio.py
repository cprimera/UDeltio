#!/usr/bin/env python2

from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from settings import DATABASE

import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE['ENGINE'] + '://' + DATABASE['USER'] + ':' + DATABASE['PASSWORD'] + '@' + DATABASE['HOST'] + '/' + DATABASE['NAME']
db = SQLAlchemy(app)

if __name__ == '__main__':
	from models import *
	from views import *
	app.debug = True
	app.secret_key = '***REMOVED***'

	port = 80
	if len(sys.argv) > 1:
		port = int(sys.argv[1])

	app.run(host='0.0.0.0', port=port)
