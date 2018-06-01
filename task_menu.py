# Что-то мне подсказывает, что реализация неверная(

from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
	def __init__(self, *args, **kwargs):
		pass

	@abstractmethod
	def execute(self):
		pass



class Menu(object):
	def __init__(self, limit):
		self.limit = limit
		self.counter = 0

	commands = {}
	def add_command(cls, name, klass):
		if not name:
			raise CommandException('Command must have a name!')
		if not issubclass(klass, Command):
			raise CommandException(
				'Class "{}" is not Command'.format(klass)
			)
		cls.commands[name] = klass

	def execute(cls, name, *args, **kwargs):
		klass = cls.commands.get(name)

		if klass is None:
			raise CommandException(
				'Command with name "{}" not found'.format(name)
			)
		return klass(*args, **kwargs)

	def __iter__(self):
		return self

	def __next__(self):
		if self.counter < self.limit:
			self.counter += 1
			return 1
		else:
			StopIteration

class CommandException(Exception):
	def __init__(self, message):
		"""Exception"""

class ShowCommand(Command):
	def __init__(self, task_id):
		pass
	def execute(self):
		pass

class ListCommand(Command):
	def __init__(self):
		pass
	def execute(self):
		pass

'''
menu = Menu(3)
menu.add_command('show', ShowCommand)
menu.add_command('list', ListCommand)
menu.execute('show', 1)
menu.execute('list')
menu.execute('unknown')
for item in menu:
	print(item)

for name, command in menu:
	print(name, command)
'''