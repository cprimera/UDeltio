#!/usr/bin/env python2.7
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
# from settings import DATABASE

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE['ENGINE'] + '://' + DATABASE['USER'] + ':' + DATABASE['PASSWORD'] + '@' + DATABASE['HOST'] + '/' + DATABASE['NAME']
db = SQLAlchemy(app)

if __name__ == '__main__':
	# from models import *
	from views import *
	app.debug = True
	app.secret_key = '***REMOVED***'
	app.run(host='0.0.0.0', port=80)