class Node :
	def __init__(self, d) :
		self.data= d
		self.left = None
		self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.right.left = Node(5)
root.right.right = Node(6)

root.left.left = Node(7)
root.left.right = Node(8)


def preOrder(node) :
	if not node :
		return 

	print(node.data)
	preOrder(node.left)
	preOrder(node.right)


preOrder(root)

from collections import deque

def printBFS(root) :
	if root is None :
		return 

	queue = []
	queue.append(root)

	while(len(queue) > 0) :
		item = queue.pop(0)

		print(item.data)

		if item.left : 
			queue.append(item.left)
		if item.right :
			queue.append(item.right)

print("BFS")
printBFS(root)






