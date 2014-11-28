from flask import Flask, request, Response, abort, session, Blueprint
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_, or_, not_
from flask.ext.mail import Message

from udeltio import app, db, mail

from models import *
from serializers import *
from oauth2.utils import *

import json


router = Blueprint('apiRouter', __name__)

@router.route('/me', methods=['GET'])
@oauth_required
def current_user():
	user = user_from_oauth()
	if request.method == 'GET':
		return Response(UserSerializer().serialize(user), mimetype='application/json')

@router.route('/me/favourites', methods=['GET'])
@oauth_required
def current_user_favourites():
	user = user_from_oauth()
	if request.method == 'GET':
		perms = Subscribers.query.filter_by(user=user.id, favorite=True).all()
		boards = []
		for p in perms:
			boards.append(Board.query.filter_by(id=p.board).first())
		return Response(BoardSerializer().serialize(boards, many=True), mimetype='application/json')

@router.route('/me/notify', methods=['GET'])
@oauth_required
def current_user_notify():
	user = user_from_oauth()
	if request.method == 'GET':
		perms = Subscribers.query.filter_by(user=user.id, notify=True).all()
		boards = []
		for p in perms:
			boards.append(Board.query.filter_by(id=p.board).first())
		return Response(BoardSerializer().serialize(boards, many=True), mimetype='application/json')


@router.route('/posts', methods=['GET', 'POST'])
@oauth_required
def posts_collection():
	user = user_from_oauth()
	if request.method == 'GET':
		return Response(PostSerializer().serialize(Post.query.all(), many=True), mimetype='application/json')
	elif request.method == 'POST':
		request.json['user'] = user.id
		post = Post(**(request.json))
		db.session.add(post)
		db.session.commit()
		subscribers = Subscribers.query.filter_by(board=post.board, notify=True).all()
		with mail.connect() as conn:
			for subscriber in subscribers:
				if subscriber.user == user.id:
					continue
				message = user.username + " posted a new message.\n\n" + post.content
				subject = Board.query.filter_by(id=post.board).first_or_404().name + ": " + post.subject
				msg = Message(recipients=[User.query.filter_by(id=subscriber.user).first_or_404().email],
						body = message,
						subject = subject,
						sender=("Udeltio", "***REMOVED***"))
				conn.send(msg)
		return Response(PostSerializer().serialize(post), status=201, mimetype='application/json')

@router.route('/posts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@oauth_required
def posts(id):
	if request.method == 'GET':
		post = Post.query.filter_by(id=id).first_or_404()
		return Response(PostSerializer().serialize(post), mimetype='application/json')
	elif request.method == 'PUT':
		post = Post.query.filter_by(id=id).first_or_404()
		post.save(**(request.json))
		db.session.commit()
		return Response(PostSerializer().serialize(post), mimetype='application/json')
	elif request.method == 'DELETE':
		post = Post.query.filter_by(id=id).first_or_404()
		db.session.delete(post)
		db.session.commit()
		return Response(status=204)




@router.route('/boards', methods=['GET', 'POST'])
@oauth_required
def boards_collection():
	if request.method == 'GET':
		return Response(BoardSerializer().serialize(Board.query.all(), many=True), mimetype='application/json')
	elif request.method == 'POST':
		board = Board(**(request.json))
		db.session.add(board)
		try:
			db.session.commit()
			board = Board.query.filter_by(name=request.json.get("name", None)).first_or_404()
			subscriber = Subscribers(board=board.id, user=user_from_oauth().id, read=False, write=False, admin=True, notify=False, favorite=True)
			db.session.add(subscriber)
			db.session.commit()
		except IntegrityError:
			db.session.rollback()
			abort(409)
		return Response(BoardSerializer().serialize(board), status=201, mimetype='application/json')

@router.route('/boards/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@oauth_required
def boards(id):
	if request.method == 'GET':
		board = Board.query.filter_by(id=id).first_or_404()
		return Response(BoardSerializer().serialize(board), mimetype='application/json')
	elif request.method == 'PUT':
		board = Board.query.filter_by(id=id).first_or_404()
		board.save(**(request.json))
		db.session.commit()
		return Response(BoardSerializer().serialize(board), mimetype='application/json')
	elif request.method == 'DELETE':
		board = Board.query.filter_by(id=id).first_or_404()
		posts = Post.query.filter_by(board=board.id).all()
		for p in posts:
			db.session.delete(p)
		subscribers = Subscribers.query.filter_by(board=id).all()
		for s in subscribers:
			db.session.delete(s)
		db.session.commit()

		assigned_tags = AssignedTags.query.filter_by(board=id).all()
		for a in assigned_tags:
			db.session.delete(a)
		db.session.commit()

		db.session.delete(board)
		db.session.commit()
		return Response(status=204)

@router.route('/boards/<int:id>/posts', methods=['GET'])
@oauth_required
def boards_posts(id):
	if request.method == 'GET':
		board = Board.query.filter_by(id=id).first_or_404()
		posts = Post.query.filter_by(board=board.id).all()
		return Response(PostSerializer().serialize(posts, many=True), mimetype='application/json')

@router.route('/boards/<int:id>/favourite', methods=['GET', 'POST', 'DELETE'])
@oauth_required
def boards_favorite(id):
	if request.method == 'GET':
		subscriber = Subscribers.query.filter_by(board=id, user=user_from_oauth().id).first()
		isFavorite = False
		if subscriber is not None:
			isFavorite = subscriber.favorite
		return Response(json.dumps({'favourite': isFavorite}), mimetype='application/json')
	elif request.method == 'POST':
		subscriber = Subscribers.query.filter_by(board=id, user=user_from_oauth().id).first()
		if subscriber is not None:
			subscriber.favorite = True
			db.session.commit()
		else:
			subscriber = Subscribers(board=id, user=user_from_oauth().id, read=False, write=False, admin=False, notify=False, favorite=True)
			db.session.add(subscriber)
			db.session.commit()
		return Response(json.dumps({'favourite': True}), status=201, mimetype='application/json')
	elif request.method == 'DELETE':
		subscriber = Subscribers.query.filter_by(board=id, user=user_from_oauth().id).first()
		if subscriber is not None:
			subscriber.favorite = False
			db.session.commit()
		return Response(status=204)

@router.route('/boards/<int:id>/users', methods=['GET', 'POST'])
@oauth_required
def boards_users(id):
	if request.method == 'GET':
		subscribers = Subscribers.query.filter_by(board=id).all()
		return Response(PermissionsSerializer().serialize(subscribers, many=True), mimetype='application/json')
	elif request.method == 'POST':
		subscriber = Subscribers.query.filter_by(board=id, user=User.query.filter_by(username=request.json['username']).first_or_404().id).first()
		if subscriber is not None:
			abort(409)
		request.json['board'] = id
		request.json['user'] = User.query.filter_by(username=request.json['username']).first_or_404().id
		request.json['notify'] = False
		request.json['favorite'] = False
		del request.json['username']
		subscriber = Subscribers(**(request.json))
		db.session.add(subscriber)
		db.session.commit()
		return Response(PermissionsSerializer().serialize(subscriber), status=201, mimetype='application/json')

@router.route('/boards/<int:id>/users/<int:userid>', methods=['GET', 'PUT', 'DELETE'])
@oauth_required
def boards_users_id(id, userid):
	if request.method == 'GET':
		subscriber = Subscribers.query.filter_by(board=id, user=userid).first_or_404()
		return Response(PermissionsSerializer().serialize(subscriber), mimetype='application/json')
	elif request.method == 'PUT':
		subscriber = Subscribers.query.filter_by(board=id, user=userid).first_or_404()
		subscriber.save(**(request.json))
		db.session.commit()
		return Response(PermissionsSerializer().serialize(subscriber), mimetype='application/json')
	elif request.method == 'DELETE':
		subscriber = Subscribers.query.filter_by(board=id, user=userid).first_or_404()
		db.session.delete(subscriber)
		db.session.commit()
		return Response(status=204)


@router.route('/boards/<int:id>/notify', methods=['GET', 'POST', 'DELETE'])
@oauth_required
def boards_notify(id):
	if request.method == 'GET':
		subscriber = Subscribers.query.filter_by(board=id, user=user_from_oauth().id).first()
		isNotify = False
		if subscriber is not None:
			isNotify = subscriber.notify
		return Response(json.dumps({'notify': isNotify}), mimetype='application/json')
	elif request.method == 'POST':
		subscriber = Subscribers.query.filter_by(board=id, user=user_from_oauth().id).first()
		if subscriber is not None:
			subscriber.notify = True
			db.session.commit()
		else:
			subscriber = Subscribers(board=id, user=user_from_oauth().id, read=False, write=False, admin=False, notify=True, favorite=False)
			db.session.add(subscriber)
			db.session.commit()
		return Response(json.dumps({'notify': True}), status=201, mimetype='application/json')
	elif request.method == 'DELETE':
		subscriber = Subscribers.query.filter_by(board=id, user=user_from_oauth().id).first()
		if subscriber is not None:
			subscriber.notify = False
			db.session.commit()
		return Response(status=204)


@router.route('/boards/<int:id>/tags', methods=['GET', 'POST'])
@oauth_required
def boards_tags(id):
	if request.method == 'GET':
		assigned_tags = AssignedTags.query.filter_by(board=id).all()
		tags = []
		for t in assigned_tags:
			tags.append(Tag.query.filter_by(id=t.tag).first_or_404())
		return Response(TagSerializer().serialize(tags, many=True), mimetype='application/json')
	elif request.method == 'POST':
		tag = Tag(**(request.json))
		db.session.add(tag)
		try:
			db.session.commit()
		except IntegrityError:
			db.session.rollback()
		tag = Tag.query.filter_by(name=request.json.get('name', None)).first()
		assigned_tag = AssignedTags(board=id, tag=tag.id)
		db.session.add(assigned_tag)
		db.session.commit()
		return Response(TagSerializer().serialize(tag), status=201, mimetype='application/json')


@router.route('/boards/<int:id>/tags/<int:tagid>', methods=['GET', 'DELETE'])
@oauth_required
def boards_tags_id(id, tagid):
	if request.method == 'GET':
		assigned_tag = AssignedTags.query.filter_by(board=id, tag=tagid).first_or_404()
		tag = Tag.query.filter_by(id=assigned_tag.tag).first_or_404()
		return Response(TagSerializer().serialize(tag), mimetype='application/json')
	elif request.method == 'DELETE':
		assigned_tag = AssignedTags.query.filter_by(board=id, tag=tagid).first_or_404()
		db.session.delete(assigned_tag)
		db.session.commit()
		return Response(status=204)


@router.route('/users', methods=['GET', 'POST'])
@oauth_required
def users_collection():
	if request.method == 'GET':
		return Response(UserSerializer().serialize(User.query.all(), many=True), mimetype='application/json')
	elif request.method == 'POST':
		user = User(**(request.json))
		db.session.add(user)
		db.session.commit()
		return Response(UserSerializer().serialize(user), status=201, mimetype='application/json')

@router.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@oauth_required
def users(id):
	if request.method == 'GET':
		user = User.query.filter_by(id=id).first_or_404()
		return Response(UserSerializer().serialize(user), mimetype='application/json')
	elif request.method == 'PUT':
		user = User.query.filter_by(id=id).first_or_404()
		user.save(**(request.json))
		db.session.commit()
		return Response(UserSerializer().serialize(user), mimetype='application/json')
	elif request.method == 'DELETE':
		user = User.query.filter_by(id=id).first_or_404()
		db.session.delete(user)
		db.session.commit()
		return Response(status=204)

@router.route('/users/<int:id>/posts', methods=['GET'])
@oauth_required
def users_posts(id):
	if request.method == 'GET':
		user = User.query.filter_by(id=id).first_or_404()
		posts = Post.query.filter_by(user=user.id).all()
		return Response(PostSerializer().serialize(posts, many=True), mimetype='application/json')




@router.route('/tags', methods=['GET', 'POST'])
@oauth_required
def tags_collection():
	if request.method == 'GET':
		return Response(TagSerializer().serialize(Tag.query.all(), many=True), mimetype='application/json')
	elif request.method == 'POST':
		tag = Tag(**(request.json))
		db.session.add(tag)
		db.session.commit()
		return Response(TagSerializer().serialize(tag), status=201, mimetype='application/json')

@router.route('/tags/<int:id>', methods=['GET', 'DELETE'])
@oauth_required
def tags(id):
	if request.method == 'GET':
		tag = Tag.query.filter_by(id=id).first_or_404()
		return Response(TagSerializer().serialize(tag), mimetype='application/json')
	elif request.method == 'DELETE':
		tag = Tag.query.filter_by(id=id).first_or_404()
		db.session.delete(tag)
		db.session.commit()
		return Response(status=204)


@router.route('/search/<term>', methods=['GET'])
@oauth_required
def search(term):
	if request.method == 'GET':
		boards = Board.query.filter(Board.name.like('%' + str(term) + '%')).all()
		tags = Tag.query.filter(Tag.name.like('%' + str(term) + '%')).all()
		bs = []
		for t in tags:
			assigned = AssignedTags.query.filter_by(tag=t.id).all()
			for a in assigned:
				b = Board.query.filter_by(id=a.board).first()
				bs.append(b)
		bs.extend(list(boards))
		return Response(BoardSerializer().serialize(bs, many=True), mimetype='application/json')


app.register_blueprint(router, url_prefix='/api/v1.0')
