from flask import Flask

import json

from functools import wraps

from datetime import datetime


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

				if isinstance(value, datetime):
					value = value.isoformat() + 'Z'
					str_val = '"' + value + '"'

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