print('''Ежедневник. Выберите действие:

	1. Вывести список задач
	2. Добавить задачу
	3. Отредактировать задачу
	4. Завершить задачу
	5. Начать задачу сначала
	6. Выход 
'''	)

def task_list():
	print('Все задачи')
tk = task_list

def add_task():
	print('Добавьте задачу')
ad = add_task

def edit_task():
	print('Измените задачу')
et = edit_task

def complete_task():
	print('Завершение задачи')
ct = complete_task

def run_task_again():
	print('Повторить задачу')
rt = run_task_again

def exit():
	print('Выход')



while True:	
	number = input('Введите число: ')
	if number == '1':
		tk()
	elif number == '2':
		ad()
	elif number == '3':
		et()
	elif number == '4':
		ct()
	elif number == '5':
		rt()
	elif number == '6':
		exit()
		break
