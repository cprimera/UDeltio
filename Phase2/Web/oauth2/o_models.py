from udeltio import db



class Client(db.Model):

	name = db.Column(db.String(40))

	description = db.Column(db.Text())

	client_id = db.Column(db.String(40), primary_key=True)

	client_secret = db.Column(db.String(55), unique=True, index=True, nullable=False)

	is_confidential = db.Column(db.Boolean)


class Token(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	client_id = db.Column(db.String(40), db.ForeignKey('client.client_id'), nullable=False)
	client = db.relationship('Client')

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User')

	token_type = db.Column(db.String(40))

	access_token = db.Column(db.String(255), unique=True)

	expires = db.Column(db.DateTime)