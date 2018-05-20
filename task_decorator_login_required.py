import hashlib

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


lst = []
def login_required(func):
	def wrapper(*args, **kwargs):
		if func.__name__ in lst:
			return func(*args, **kwargs)
		
		with open('token.txt') as f:
					token = f.read()
		for i in range(3):
			username = input('Введите логин: ')
			password = input('Введите пароль: ')
			ok = make_token(username, password)
			if token == ok:
				lst.append(func.__name__)
				break
			else:
				return None
		return func			
	return wrapper

