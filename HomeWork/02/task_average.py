def average(lst):
	def summa(lst):    #сумма
		s = 0
		for x in lst:
			s += x
		return s
	return round((summa(lst)/len(lst)), 3)