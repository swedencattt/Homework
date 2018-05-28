from abc import ABCMeta, abstractmethod
import re
from time import strptime
from datetime import datetime

class Validator(metaclass=ABCMeta):
	names = {}
	
	@abstractmethod
	def validate(self, value):
		if value:
			return True
		else:
			return False

	@classmethod
	def add_type(cls, name, klass):
		if not name:
			raise ValidatorException('Validator must have a name!')
		if not issubclass(klass, Validator):
			raise ValidatorException(
				'Class "{}" is not Validator'.format(klass)
			)
		cls.names[name] = klass

	@classmethod
	def get_instance(cls, name, *args, **kwargs):
		klass = cls.names.get(name)

		if klass is None:
			raise ValidatorException(
				'Validator with name "{}" not found'.format(name)
			)
		return klass()
	

class EMailValidator(Validator):
	name = 'email'
	def validate(self,  value):
		match = re.search(r'[\w.-]+@[\w.-]+.\w+', value)
		if match:
			return True
		else:
			return False
		
	
class DateTimeValidator(Validator):
	name = 'datetime'
	def validate(self, value):	
		for format in ['%Y-%m-%d', '%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S',
					   '%d.%m.%Y', '%d.%m.%Y %H:%M', '%d.%m.%Y %H:%M:%S',
					   '%d/%m/%Y', '%d/%m/%Y %H:%M', '%d/%m/%Y %H:%M:%S',
		]:
			try:
				result = datetime.strptime(value, format)
				return True
			except:
				pass

class ValidatorException(Exception):
	def __init__(self, message):
		"""Exceptions"""


Validator.add_type('email', EMailValidator)
validator = Validator.get_instance('email')
print(validator.validate('info@itmo-it.org'))
print(validator.validate('unknown'))

Validator.add_type('datetime', DateTimeValidator)
validator = Validator.get_instance('datetime')
print(validator.validate('2017-9-11'))
print(validator.validate('1.9.2017'))
print(validator.validate('01/09/2017 12:00'))
print(validator.validate('0'))