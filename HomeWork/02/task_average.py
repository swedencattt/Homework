def average(lst):
	def summa(lst):
		s = 0
		for x in lst:
			s += x
		return s
	return round((summa(lst)/len(lst)), 3)