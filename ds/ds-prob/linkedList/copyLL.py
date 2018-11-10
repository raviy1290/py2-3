class Node(object) :
	def __init__(self, data) :
		self.data = data
		self.next = None

def printLL(head) :
	while head is not None :
		print(head.data)
		head = head.next

def copyLL(head) :

	new_curr = new_head = None
	curr = head

	new_head = Node(curr.data)
	new_curr = new_head

	curr = curr.next
	
	while curr is not None :
		new_curr.next = Node(curr.data)
		new_curr = new_curr.next
		curr = curr.next

	return new_head


head = Node(1)

current = head
for i in range(2, 10) :
	current.next = Node(i)
	current = current.next

new = copyLL(head)

printLL(new)

print( id(head) )
print( id(new) )





