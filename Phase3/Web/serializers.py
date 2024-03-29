from models import *
from utils import BaseSerializer



class UserSerializer(BaseSerializer):
	fields = ['id', 'username', 'first_name', 'last_name', 'email']
	model = User

class BoardSerializer(BaseSerializer):
	fields = ['id', 'name', 'public', 'subscribers', 'tags']
	model = Board

	subscribers = 'get_subscribers'
	tags = 'get_tags'

class PostSerializer(BaseSerializer):
	fields = ['id', 'user', 'board', 'creation_date', 'subject', 'content', 'important', 'offensive']
	model = Post

class TagSerializer(BaseSerializer):
	fields = ['id', 'name']
	model = Tag

class SubscribersSerializer(BaseSerializer):
	fields = ['id', 'user', 'board', 'read', 'write', 'admin', 'notify', 'favorite']
	model = Subscribers

class PermissionsSerializer(BaseSerializer):
	fields = ['id', 'username', 'read', 'write', 'admin']
	model = Subscribers

	id = 'get_user_id'
	username = 'get_username'

class AssignedTagsSerializer(BaseSerializer):
	fields = ['id', 'board', 'tag']
	model = AssignedTags
