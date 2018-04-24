def bubble_sort(lst):       		  
	for x in range(0, len(lst) - 1):
				# перебор элементов, от нуля до индекса последнего элемента
		for i in range(0, len(lst) - 1 - x):
			if lst[i] > lst[i + 1]: 
				# если элемент, стоящий слева больше,
				# происходит следующее:
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
				# элементы меняются местами
	return(lst) # возвращает значение

