class Node :
	def __init__(self, d) :
		self.data = d
		self.next = None


class LinkedList :
	def __init__(self) :
		self.head = None

	def push(self, val) :
		node = Node(val)
		if self.head == None :
			self.head = node
			return

		curr = self.head

		while curr.next != None :
			curr = curr.next

		curr.next = node

	def printLinkedList(self) :
		curr = self.head

		while curr.next is not None :
			print(curr.data, end="->")
			curr = curr.next
		print(curr.data)
		print()

	def delete(self, index) :

		i=0
		prev = None
		current = self.head 

		while i < index :
			prev, current = current, current.next
			i+=1
		prev.next = current.next
		current = None


	def reverse(self) :
 		prev = None
 		current = self.head
 		while(current is not None):
 			next = current.next
 			current.next = prev
 			prev = current
 			current = next
 		self.head = prev


ll = LinkedList()
ll.push(1)
ll.push(11)
ll.push(111)
ll.push(1111)
ll.push(11111)
ll.push(111111)

ll.printLinkedList()
ll.reverse()
ll.printLinkedList()

