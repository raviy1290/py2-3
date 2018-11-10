class Node :
	def __init__(self, data) :
		self.data = data 
		self.next = None
		self.prev = None

class DLL :
	def __init__(self) :
		self.head = None
		self.tail = None

	def add(self, data) :
		new_node = Node(data)

		if self.head is None :
			self.head = new_node
			self.tail = new_node
		else :

			new_node.next = self.head
			self.head.prev = new_node

			self.head = new_node

	def deleteAtEnd(self) :
		second_last = self.tail.prev
		second_last.next = None

		self.tail = second_last
			

dll = DLL()
dll.add(1)
dll.add(2)
dll.add(3)

print(dll.head.data)
print(dll.tail.data)
dll.deleteAtEnd()
print(dll.tail.data)

