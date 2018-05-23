'''
Курсы должны содержать информацию, текст, которые можно получить(или часть информации)
Учитель должен получать информацию из курса и передавать ее ученикам
Ученик должен принимать эту информацию и превращать ее в накопленные знания
'''
'''
Методы учеников - принимать информацию; накапливать ее; выполнять задания, данные учителем; получать за это оценки
Св-ва учеников - имя, возраст, пол, уже полученные знания(скиллы), успеваемость

Методы учителей - получение инфы из курса и передача ее ученикам; проверка успеваемости учеников(контроль)
Св-ва учителей - имя, возраст, пол, квалификация, опыт(знания, скиллы)

Методы курсов - уже содержит информацию
Св-ва курсов - направление(название); продолжительность; ранжирование по навыкам учеников(
начальный уровень, базовый, профф); результат - что дает на выходе курс
'''
'''
Взаимодействие:
К каждому курсу должен быть добавлен учитель, хотя ученики могут изучать курс самостоятельно
Учитель брет информацию из курсов и транслирует ее ученикам
Ученики получают информацию от учителя и откладывают ее в "знания"
Учитель дает задание ученикам и ждет от них результат.
Ученики выполняют задание, передают результат учителю, учитель ставит за них оценки


Была идея создать метакласс Курсы, и затем создавать класс для каждого курса в отдельности
(пока не понимаю для чего))
Как все это реализовать в коде пока тоже не совсем понятно, что-то не работает
'''


from abc import ABCMeta, abstractmethod

class Courses(object):
	def __init__(self, name_course, info):
		self.name_course = name_course
		self.info = info
		self.courses = {}

	def add_course(self):
		self.courses[key] = value

	def get_all_courses(self):
		return self.courses

	def add_teacher(self):
		"""Добавляет учителя к курсу"""

	def send_info(self, info):
		pass


class Teachers(object):
	def __init__(self, name, age, quality):
		self.name = name
		self.age = age
		self.quality = quality
		

	def get_text(self, text):
		"""Получет инфо из курса"""
		self.text = text

	def tell_text(self):
		"""Передает инфу"""
		return self.text


class Students(object):
	def __init__(self, name, age, skills):
		self.knowledge = []
		self.name = name
		self.age = age
		self.skills = skills

	def chose_course(self, course):
		pass

	def get_text(self, n):
		self.knowledge.append(n)


inform = Courses('Python', ['1+1=2', '2+2=4', '2*2=4'])
Alexey_Alexseevich = Teachers('Alexey_Alexseevich', '30', 'Python_Developer')
Ivan = Students('Ivan', '17', 'junior_python')
Alexey_Alexseevich.get_text(inform.send_info)
Ivan.get_text(Alexey_Alexseevich.tell_text())

print(Alexey_Alexseevich.name, Alexey_Alexseevich.age, Alexey_Alexseevich.quality)
print(Ivan.knowledge)


		