def  get_quadrant_number(x, y): 
	if x == 0 and y == 0:
		raise ValueError
	choises = {
		(1, 1): 1,
	 	(-1, 1): 2,
		(-1, -1): 3,
	 	(1, -1): 4,
	}
	return choises.get((x, y), 'default')
