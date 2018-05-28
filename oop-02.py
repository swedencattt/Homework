from abc import ABCMeta, abstractmethod
import os
import json
import pickle

class ParamHandler(metaclass=ABCMeta):
	def __init__(self, source):
		self.source = source
		self.params = {}

	def add_param(self, key, value):
		self.params[key] = value

	def gett_all_params(self):
		return self.params

	@abstractmethod
	def read(self):
		pass

	@abstractmethod
	def write(self):
		pass

	types = {}

	@classmethod
	def add_type(cls, name, klass):
		if not name:
			raise ParamHandlerException('Type must have a name!')
		if not issubclass(klass, ParamHandler):
			raise ParamHandlerException(
				'Class "{}" is not ParamHandler'.format(klass)
			)
		cls.types[name] = klass

	@classmethod
	def get_instance(cls, source, *args, **kwargs):
		_, ext = os.path.splitext(str(source).lower())
		ext = ext.lstrip('.')
		klass = cls.types.get(ext)

		if klass is None:
			raise ParamHandlerException(
				'Type "{}" not found'.format(ext)
			)
		return klass(source, *args, **kwargs)

class TextParamHandler(ParamHandler):
	def read(self):
		"""Чтение"""
	def write(self):
		"""Запись"""

class XmlParamHandler(ParamHandler):
	def read(self):
		"""Чтение"""
	def write(self):
		"""Запись"""

class JsonParamHandler(ParamHandler):
	def read(self):
		with open(self.source) as f:
			self.params = json.load(f)
	def write(self):
		with open(self.source, 'w') as f:
			json.dump(self.params, f)

class PickleParamHandler(ParamHandler):
	def read(self):
		with open(self.sourse, 'rb') as f:
 			self.params = pickle.load(f)
	def write(self):
		with open(self.source, 'wb') as f:
 			pickle.dump(self.params, f)


class ParamHandlerException(Exception):
	def __init__(self, message):
		"""Exceptions"""

ParamHandler.add_type('xml', XmlParamHandler)
config = ParamHandler.get_instance('./params.xml')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()

config.read()
print(config.gett_all_params())


ParamHandler.add_type('txt', TextParamHandler)
config = ParamHandler.get_instance('./params.txt')
config.read()

ParamHandler.add_type('json', JsonParamHandler)
config = ParamHandler.get_instance('./params.json')
config.add_param('key1', 'val1')
print(config.gett_all_params())
config.write()
config.read()

ParamHandler.add_type('pickle', PickleParamHandler)
config = ParamHandler.get_instance('./params.pickle')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.add_param('key4', 'val4')
config.add_param('key5', 'val5')
print(config.gett_all_params())
