def is_palindrome(s):
	s = str(s)
	s = s.replace(' ', '')
    if s == s[::-1]:
    	return True
    else:
    	return False