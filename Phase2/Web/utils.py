from flask import Flask

import json


class ApiRouter():

	def __init__(self, app=None, api_version="", base_url="/api"):
		self.api_version = api_version if api_version != None else ""
		self.base_url = base_url if base_url != None else ""
		if app is not None:
			self.app = app
			self.init_app(app)
		else:
			self.app = None

	def init_app(self, app):
		self.app = app

	def route(self, route, **options):
		self.api_version =  '/' + self.api_version.replace('/', '')
		self.base_url = '/' + self.base_url.replace('/', '')
		route = '/' + (route if route[0] != '/' else route[1:])

		r = self.base_url + (self.api_version if self.api_version != '/' else '') + route

		def decorated_function(f):
			endpoint = options.pop('endpoint', None)
			self.app.add_url_rule(r, endpoint, f, **options)
			return f
		return decorated_function



class BaseSerializer(object):
	fields = []
	model = None

	def __init__(self):
		super(BaseSerializer, self).__init__()

	def serialize(self, obj, many=False):
		out = ""
		if many:
			out += "["
			if len(obj) > 0:
				for o in obj[:-1]:
					out += self._serialize(o) + ", "
				else:
					out += self._serialize(obj[-1])
			out += "]"
		else:
			out += self._serialize(obj)
		return out

	def _serialize(self, obj):
		out = "{"
		if obj != None and len(self.fields) > 0:
			for field in self.fields:
				try:
					func = self.__getattribute__(field)
					if isinstance(func, BaseSerializer):
						value = obj.__getattribute__(field)
						value = func.model.query.filter_by(id=value).first()
						value = func.serialize(value)
					else:
						value = obj.__getattribute__(func)(field)
				except AttributeError, e:
					try:
						value = obj.__getattribute__(field)
					except AttributeError, e:
						raise e

				if isinstance(value, str):
					str_val = value
				else:
					str_val = str(value)
					str_val = str_val.replace('\r', '\\r')
					str_val = str_val.replace('\n', '\\n')
					str_val = '"' + str_val + '"'

				if isinstance(value, list):
					value = list(value)

				try:
					if not isinstance(value, str):
						str_val = json.dumps(value)
				except TypeError, e:
					if isinstance(value, list):
						new_val = []
						for v in value:
							if isinstance(v, db.Model):
								new_val.append(v.id)
							else:
								new_val.append(v)
						str_val = json.dumps(new_val)

				if field == self.fields[-1]:
					out += '"' + field + '":' + str_val
				else:
					out += '"' + field + '":' + str_val + ', '

		out += "}"
		return out

	def load(self, string):
		d = json.loads(string)
		return model(**d)