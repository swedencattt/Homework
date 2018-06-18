class LinkedList(object):
	def __init__(self, *args, **kwargs):
		self.first = None
		self.last = None
		self.length = 0

	def add(self, value):
		self.length+=1
		if self.first == None:
			self.last = self.first = Node(value, None)
		else:
			self.last.next = self.last = Node(value, None)

	def insert(self, index, value):
		if self.first == None:
			self.last = self.first = Node(value, None)
			return
		if index == 0:
			self.first = Node(value, self.first)
		curr = self.first
		count = 0
		while curr != None:
			count += 1
			if count == index:
				curr.next = Node(value, curr.next)
				if curr.next.next == None:
					self.last = curr.next
				break
			curr = curr.next


	def get(self, index):
		pass

	def remove(self, value):
		pass

	def remove_at(self, index):
		pass

	def clear(self):
		self.__init__()

	def contains(self, value):
		pass

	def len(self):
		length = 0
		if self.first != None:
			current = self.first
			while current.next != None:
				current = current.next
				length += 1
		return length+1

	def is_empty(self):
		if self.first == None:
			return True

	def __next__(self):
		pass
		
	def __iter__(self):
		pass



