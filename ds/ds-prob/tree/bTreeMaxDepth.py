class Node () :
	def __init__(self, d) :
		self.data = d
		self.left = None
		self.right = None

root = Node(1)
root.left = Node(2)
root.left.left = Node(22)
root.left.right = Node(222)

root.right = Node(3)
root.right.right = Node(33)
root.right.right.right = Node(333)
root.right.right.right.right = Node(3333)

def printInorder(node) :
	if node is None :
		return
	print(node.data)
	printInorder(node.left)
	printInorder(node.right)

printInorder(root)


def maxDepth(node, depth) :
	if node is None :
		return (None, depth)
	elif(node.left is None and node.right is None) :
		return (node.data, depth+1)
	else :
		if node.left is None :
			return maxDepth(node.right, depth+1) 
		elif node.right is None :
			return maxDepth(node.left, depth+1) 

		return max(maxDepth(node.left, depth+1) , maxDepth(node.right, depth+1))


print(maxDepth(root, 0))