class Node :
	def __init__(self, data) :
		self.data = data 
		self.next = None

class LL :
	def __init__(self) :
		self.head = None
		self.tail = None

	def addAtEnd(self, data) :
		new_node = Node(data)

		if self.head is None :
			self.head = new_node
			self.tail = new_node
		else :
			curr = self.head

			while curr.next is not None :
				curr = curr.next

			curr.next = new_node

	def add(self, data) :
		new_node = Node(data)

		if self.head is None :
			self.head = new_node
			self.tail = new_node
		else :
			new_node.next = self.head
			self.head = new_node

	def deleteAtEnd(self) :

		prev = curr = self.head
		while curr.next is not None :
			prev = curr
			curr = curr.next

		self.tail = prev
		self.tail.next = None

	def printLL(self) :
		curr = self.head
		while curr is not None :
			print(curr.data, end='-')
			curr = curr.next
		print()





ll = LL()
ll.add(1)
ll.add(2)
ll.add(3)

ll.printLL()
ll.deleteAtEnd()
ll.printLL()
ll.deleteAtEnd()
ll.printLL()
