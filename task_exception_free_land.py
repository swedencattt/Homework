def get_free_land(a, b):
	s = a[0]
	s = s * 100
	aspect_ratio = a[1]
	width_beds = b[0]
	lenght_beds = b[1]
	s_beds = width_beds * lenght_beds
	if s == 0:
		raise ValueError("Не задана площадь участка")
	if width_beds == 0 or lenght_beds == 0:
		raise ValueError("Не задана площадь грядки")
	if s_beds > s:
		raise ValueError("Размер грядки больше размера участка")
	return s % s_beds
	