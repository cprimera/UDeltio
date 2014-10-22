from flask import Flask, request, Response, abort

from udeltio import app, db
from models import User
from oauth2.o_models import Client, Token

from os import urandom
from binascii import b2a_hex
import json
from datetime import datetime, timedelta


@app.route('/oauth2/access_token', methods=['POST'])
def access_token():
	client = Client.query.filter_by(client_id=request.json['client_id'], client_secret=request.json['client_secret']).first()
	user = User.query.filter_by(username=request.json['username']).first()
	if client and request.json['grant_type'] == 'password':
		token = Token.query.filter_by(client_id=client.client_id, user_id=user.id).first()
		if token and token.expires > datetime.utcnow():
			return Response(json.dumps({'access_token' : token.access_token}), mimetype='application/json')

		expire_time = datetime.utcnow() + timedelta(days=1)
		token = Token(
			access_token=b2a_hex(urandom(20)),
			token_type='password',
			expires=expire_time,
			client_id=client.client_id,
			user_id=user.id
		)
		db.session.add(token)
		db.session.commit()
		return Response(json.dumps({'access_token' : token.access_token}), mimetype='application/json')