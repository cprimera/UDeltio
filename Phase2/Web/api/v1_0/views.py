from flask import Flask, request, Response, abort, session

from udeltio import app, db

from models import *
from serializers import *
from utils import ApiRouter
from oauth2.utils import *

router = ApiRouter(app, api_version='v1.0')



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
		db.session.commit()
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