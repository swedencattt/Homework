import sys 

from day_planner import storage

get_connection = lambda: storage.connect('day_planner.sqlite')



def action_list_task():
	"""Вывести список задач"""
	print('''
1. Вывести все активные задачи
2. Вывести завершенные задачи
3. Вывести все задачи
m. Вернуться в главное меню
''')

def action_active_list():
	"""Показывает все активные задачи"""
	with get_connection() as conn:
		print = storage.show_tasks_active(conn)


def action_complete_list():
	"""Показывает все завершенные задачи"""
	with get_connection() as conn:
		print = storage.show_tasks_complete(conn)

def action_list():
	with get_connection() as conn:
		print = storage.show_tasks(conn)

def action_status():
	"""Показывает список задач"""
	action_list_task()

	actions_list = {
		'1': action_active_list,
		'2': action_complete_list,
		'3': action_list,
		'm': main,
	}

	while True:
		cmd = input('\nВведите команду: ', )
		actionst = actions_list.get(cmd)
		if actionst:
			actionst()
		else:
			print('Неизвестная команда')




def action_add():
	"""Добавить задачу"""
	name = input('\nВведите название задачи: ', )
	description = input('\nОпишите задачу: ', )
	date_to_complete = input('\nВведите дату выполнения задачи: ', )
	status = "active"
	with get_connection() as conn:
		print = storage.add_task(conn, name, description, date_to_complete, status)





def action_edit_menu():
	"""Показать меню"""
	print('''
1. Изменить название задачи
2. Изменить описание задачи
3. Изменить дату выполнения задачи
m. Вернуться в главное меню
''')

def action_edit_name():		
	id = input('\nВведите номер задачи, которую необходимо отредактировать: ', )
	name = input('\nИзмените название задачи: ', )
	with get_connection() as conn:
		print = storage.edit_name_of_task(conn, id, name)
	action_edit()
def action_edit_description():
	id = input('\nВведите номер задачи, которую необходимо отредактировать: ', )
	description = input('\nИзмените описание задачи: ', )
	with get_connection() as conn:
		print = storage.edit_description_of_task(conn, id, description)
	action_edit()
def action_edit_date():
	id = input('\nВведите номер задачи, которую необходимо отредактировать: ', )
	date_to_complete = input('\nИзмените дату выполнения задачи: ', )
	with get_connection() as conn:
		print = storage.edit_date_of_task(conn, id, date_to_complete)
	action_edit()


def action_edit():
	"""Отредактировать задачу"""

	action_edit_menu()

	actions_edit = {
		'1': action_edit_name,
		'2': action_edit_description,
		'3': action_edit_date,
		'm': main,
	}

	while True:
		cmd = input('\nВведите команду: ')
		action_ed = actions_edit.get(cmd)
		if action_ed:
			action_ed()
		else:
			print('Неизвестная команда')





def action_complete():
	"""Завершить задачу"""
	id = input('\nВведите номер завершаемой задачи: ', )
	status = "complete"
	with get_connection() as conn:
		print = storage.complete_task(conn, id, status)

def action_delete():
	id = input('\nВведите номер удаляемой задачи: ', )
	with get_connection() as conn:
		print = storage.delete_task(conn, id)

def action_run_again():
	"""Начать задачу сначала"""
	id = input('\nВведите номер задачи, котрую необходимо повторить: ', )
	status = 'active'
	with get_connection() as conn:
		print = storage.return_task(conn, id, status)




def action_show_menu():
	"""Показать меню"""
	print('''

	1. Вывести список задач
	2. Добавить задачу
	3. Отредактировать задачу
	4. Завершить задачу
	5. Начать задачу сначала
	6. Удалить задачу
	m. Показать меню
	7. Выход 
''')
	

def action_exit():
	"""Выйти"""
	sys.exit(0)


def main():
	with get_connection() as conn:
		storage.initialize(conn)
		
	action_show_menu()

	actions = {
		'1': action_status,
		'2': action_add,
		'3': action_edit,
		'4': action_complete,
		'5': action_run_again,
		'6': action_delete,
		'm': main,
		'7': action_exit
	}

	while True:
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		if action:
			action()
		else:
			print('Неизвестная команда')

