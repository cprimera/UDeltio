from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


from udeltio import app, db

from datetime import datetime



class User(db.Model):
	"""
	User model. This supplements any data that would be retrieved from the
	university login system (Assuming this were actually being deployed on
	university servers as a university system).
	"""

	id = db.Column(db.Integer, primary_key=True)

	username = db.Column(db.String(40))

	first_name = db.Column(db.String(50))

	last_name = db.Column(db.String(50))

	email = db.Column(db.String(256))

	def __init__(self, username, first_name, last_name, email):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	def save(self, **kwargs):
		pass

	def __repr__(self):
		return '%s %s' % (self.first_name, self.last_name)



class Board(db.Model):
	"""
	Board model. This represents a discussion Board.
	"""

	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(50))

	public = db.Column(db.Boolean)

	def __init__(self, name, public):
		self.name = name
		self.public = public

	def save(self, **kwargs):
		pass

	def __repr__(self):
		return '%s' % self.name

	def get_subscribers(self, field):
		subscribers = Subscribers.query.filter_by(board=self.id).all()
		user_ids = [x.user for x in subscribers]
		return user_ids

	def get_tags(self, field):
		tags = AssignedTags.query.filter_by(board=self.id).all()
		tag_ids = [x.tag for x in tags]
		return tag_ids



class Post(db.Model):
	"""
	Post model. This represents a Post on a discussion board.
	"""

	id = db.Column(db.Integer, primary_key=True)

	user = db.Column(db.Integer, db.ForeignKey('user.id'))

	board = db.Column(db.Integer, db.ForeignKey('board.id'))

	creation_date = db.Column(db.DateTime)

	subject = db.Column(db.String(100))

	content = db.Column(db.Text)

	important = db.Column(db.Boolean)

	def __init__(self, user, board, subject, content, important):
		self.user = user
		self.board = board
		self.subject = subject
		self.content = content
		self.important = important
		self.creation_date = datetime.utcnow()

	def save(self, **kwargs):
		self.user = kwargs.get('user', self.user)
		self.board = kwargs.get('board', self.board)
		self.subject = kwargs.get('subject', self.subject)
		self.content = kwargs.get('content', self.content)
		self.important = kwargs.get('important', self.important)

	def __repr__(self):
		return '%s %s' % (User.query.filter_by(id=self.user).first().username, self.subject)



class Tag(db.Model):
	"""
	Tag model. This represents a Tag
	"""

	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(100))

	def __init__(self, name):
		self.name = name

	def save(self, **kwargs):
		pass

	def __repr__(self):
		return '%s' % self.name



class Subscribers(db.Model):
	"""
	Subscribers model. This links Users with Boards and gives them permissions on the Board
	"""

	id = db.Column(db.Integer, primary_key=True)

	board = db.Column(db.Integer, db.ForeignKey('board.id'))

	user = db.Column(db.Integer, db.ForeignKey('user.id'))

	read = db.Column(db.Boolean)

	write = db.Column(db.Boolean)

	admin = db.Column(db.Boolean)

	notify = db.Column(db.Boolean)

	favorite = db.Column(db.Boolean)

	def __init__(self, board, user, read, write, admin, notify, favorite):
		self.board = board
		self.user = user
		self.read = read
		self.write = write
		self.admin = admin
		self.notify = notify
		self.favorite = favorite

	def save(self, **kwargs):
		pass

	def __repr__(self):
		return '%s %s' % (self.user.username, self.board.name)



class AssignedTags(db.Model):
	"""
	AssignedTags model. This links Boards with Tags.
	"""

	id = db.Column(db.Integer, primary_key=True)

	board = db.Column(db.Integer, db.ForeignKey('board.id'))

	tag = db.Column(db.Integer, db.ForeignKey('tag.id'))

	def __init__(self, board, tag):
		self.board = board
		self.tag = tag

	def save(self, **kwargs):
		pass

	def __repr__(self):
		return '%s %s' % (self.board.name, self.tag.name)