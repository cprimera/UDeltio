from flask import request, abort, session
from sqlalchemy import or_, and_, not_

from functools import wraps

from udeltio import app
from models import User
from oauth2.o_models import Token

from datetime import datetime

def oauth_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'Authorization' in request.headers:
			token = request.headers['Authorization'][7:]
			t = Token.query.filter(and_(Token.expires > datetime.utcnow(), Token.access_token == token)).first()
			if t:
				return f(*args, **kwargs)
			else:
				abort(401)
		else:
			abort(401)
	return decorated_function

def user_from_oauth():
	if 'Authorization' in request.headers:
		token = request.headers['Authorization'][7:]
		t = Token.query.filter(and_(Token.expires > datetime.utcnow(), Token.access_token == token)).first()
		if t:
			return t.user
	return None