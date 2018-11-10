class Node :
	def __init__(self, d) :
		self.data= d
		self.left = None
		self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(8)

root.right.left = Node(6)
root.right.right = Node(7)

root.right.right.left = Node(9)
root.right.right.left.right = Node(11)


def preOrder(node) :
	if not node :
		return 

	print(node.data)
	preOrder(node.left)
	preOrder(node.right)


preOrder(root)


def printLeftView(root) :
	print("printLeftView")
	q = []
	q.append(root)

	while len(q) > 0 :
		q_len = len(q)

		i = 0
		while i < q_len :
			item = q.pop(0)
			if i == 0 :
				print(item.data)
			i+=1
			if item.left is not None :
				q.append(item.left)
			if item.right is not None :
				q.append(item.right)


printLeftView(root)