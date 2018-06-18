from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
	def __init__(self, *args, **kwargs):
		pass

	@abstractmethod
	def execute(self):
		pass



class Menu(metaclass=ABCMeta):
	def __init__(self):
		super().__init__()
		self.value = 0
		self.commands = {}

	def __iter__(self):
		return self

	def __next__(self):
		if self.value < len(self.commands):
			self.value += 1
			return list(self.commands.items())[self.value]
		else:
			raise StopIteration

	def add_command(self, name, klass):
		if not name:
			raise CommandException('Command must have a name!')
		if not issubclass(klass, Command):
			raise CommandException(
				'Class "{}" is not Command!'.format(klass)
			)
		self.commands[name] = klass

	def execute(self, name, *args, **kwargs):
		com = self.commands.get(name)

		if com is None:
			raise CommandException(
				'Command with name "{}" not found'.format(name)
			)
		return com(*args, **kwargs).execute()

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