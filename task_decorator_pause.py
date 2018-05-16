from functools import wraps
import time

def pause(sec):
	def decorator(func):
		def wrapper(*args, **kwargs):
			sleep = time.sleep(sec)
			result = func(*args, **kwargs)
			print('Функция "{}" выполняется с задержкой в {} секунды'.format(
				func.__name__, sec
			))
			return result
		return wrapper
	return decorator

