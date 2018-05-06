import os.path as Path
import sqlite3


SQL_SELECT_ALL = '''
	SELECT 
		id, name, description, date_to_complete, status, created
	FROM
		tasks
'''
SQL_SELECT_ALL_ACTIVE ='''
	SELECT * FROM tasks WHERE status='active'
'''

SQL_SELECT_ALL_COMPLETE = '''
	SELECT * FROM tasks WHERE status='complete'
'''
SQL_INSERT_TASK = 'INSERT INTO tasks(name, description, date_to_complete, status) VALUES(?, ?, ?, ?)'
SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'
SQL_UPDATE_NAME = '''
	UPDATE tasks SET name=? WHERE id=?
'''
SQL_UPDATE_DESCRIPTION = '''
	UPDATE tasks SET description=? WHERE id=?
'''
SQL_UPDATE_DATE = '''
	UPDATE tasks SET date_to_complete=? WHERE id=?
'''
SQL_COMPLETE_TASK = '''
	UPDATE tasks SET status=? WHERE id=?
'''
SQL_DELETE_TASK = '''
	DELETE FROM tasks WHERE id=?
'''
SQL_UPDATE_TASK_RETURN = '''
	UPDATE tasks SET status=? WHERE id=?
'''



def connect(db_name=None):
	"""Выполняет подключение к БД"""
	if db_name is None:
		db_name = ':memory:'
	conn = sqlite3.connect(db_name)
	return conn


def initialize(conn):
	"""Инициализирует структуру БД"""
	script_path = Path.join(Path.dirname(__file__), 'schema.sql')
	with conn, open(script_path) as f:
		conn.executescript(f.read())


def show_tasks(conn):
	"""Показывает все задания"""
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL)
		result = cursor.fetchall()
		print(result)

def show_tasks_active(conn):
	"""Показывает все активные задачи"""
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL_ACTIVE)
		result = cursor.fetchall()
		print(result)

def show_tasks_complete(conn):
	"""Показывает все завершенные задачи"""
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL_COMPLETE)
		result = cursor.fetchall()
		print(result)




def add_task(conn, name, description, date_to_complete, status):
	"""Добавляет новую задачу"""
	with conn:
		cursor = conn.execute(SQL_INSERT_TASK, (name, description, date_to_complete, status))
		pk = cursor.lastrowid
		cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
		return cursor.fetchone()
	


def edit_name_of_task(conn, id, name):
	"""Редактирует имя задачи"""
	with conn:
		cursor = conn.execute(SQL_UPDATE_NAME, (name, id))
		return cursor.fetchone()

def edit_description_of_task(conn, id, description):
	"""Редактирует опсание задачи"""
	with conn:
		cursor = conn.execute(SQL_UPDATE_DESCRIPTION, (description, id))
		return cursor.fetchone()

def edit_date_of_task(conn, id, date_to_complete):
	"""Редактирует опсание задачи"""
	with conn:
		cursor = conn.execute(SQL_UPDATE_DATE , (date_to_complete, id))
		return cursor.fetchone()



def complete_task(conn, id, status):
	"""Завершает задачу"""
	with conn:
		cursor = conn.execute(SQL_COMPLETE_TASK, (status, id))
		return cursor.fetchone()


def delete_task(conn, id):
	with conn:
		cursor = conn.execute(SQL_DELETE_TASK, (id))
		pk = cursor.lastrowid
		cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
		return cursor.fetchone()

def return_task(conn, id, status):
	with conn:
		cursor = conn.execute(SQL_UPDATE_TASK_RETURN, (status,id))
		return cursor.fetchone()