class Node(object) :
	def __init__(self, data) :
		self.data = data
		self.next = None

def printLL(head) :
	while head is not None :
		print(head.data)
		head = head.next

def printLastKth(head, K) :
	curr1 = head
	curr2 = head

	k = 0
	while curr1 is not None :
		k+=1
		curr1 = curr1.next
		if k > K :
			curr2 = curr2.next

	print(curr2.data)


head = Node(1)

current = head
for i in range(2, 100) :
	current.next = Node(i)
	current = current.next

printLastKth(head, 99)






