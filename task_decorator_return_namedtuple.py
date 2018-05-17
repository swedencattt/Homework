from collections import namedtuple

def return_namedtuple(*names):
	def decorator(func):
		def wrapper(*args, **kwargs):
			result = func(*args, **kwargs)
			if isinstance(result, tuple):
				named_tuple = namedtuple('namedtuple', list(names))
			return named_tuple(*result)
		return wrapper
	return decorator

