from datetime import datetime, timedelta, date

def counter():
	today = datetime.now()
	new_year = datetime(today.year + 1, 1, 1, 0, 0, 0)
	delta = new_year - today
	days = delta.days
	hours = int(delta.seconds//3600)
	minutes = int((delta.seconds % 3600) // 60)

	if days % 10 == 1 and days not in range(10, 21):
		day = 'день'
	elif days % 10 in range(2, 5) and not in range(10, 21):
		day = 'дня'
	else:
		day = 'дней'


	if hours % 10 == 1 and hours % 10 != 11:
		hour = 'час'
	elif hours % 10 in range(2, 5) and hours not in range(10, 21):
		hour = 'часа'
	else:
		hour = 'часов'


	if minutes % 10 == 1 and minutes % 10 != 11:
		minute = 'минута'
	elif minutes % 10 in range(2, 5) and not in range(10,21):
		minute = 'минуты'
	else:
		minute = 'минут'

	print(days, day, hours, hour, minutes, minute)