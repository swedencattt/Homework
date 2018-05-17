import random
import string


def password_generator(n):
		while 1:	
			password = ''.join(random.sample(
				string.ascii_letters + string.digits + string.punctuation, n
			))
			yield password
	
	

