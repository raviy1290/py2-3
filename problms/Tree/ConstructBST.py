class Node :
	def __init__(self, d) :
		self.data= d
		self.left = None
		self.right = None

def getPreIndex():
	return constructTreeUtil.preIndex
def incrementPreIndex():
	constructTreeUtil.preIndex += 1

def constructTreeUtil(pre, low, high, size) :

	print(pre, low, high, size, getPreIndex())

	if( getPreIndex() >= size or low > high ) :
		return None

	root = Node(pre[getPreIndex()])
	incrementPreIndex()

	if low==high :
		return root

	for i in range(low, high+1) :
		if pre[i] > root.data :
			break

	preOrder(root)

	root.left = constructTreeUtil(pre, getPreIndex(), i-1, size)
	root.right = constructTreeUtil(pre, i, high, size)
	return root

def constructBST(pre) :
	size = len(pre) 
	constructTreeUtil.preIndex = 0
	return constructTreeUtil(pre, 0, size-1, size)

def preOrder(node) :
	if not node :
		return 

	print(node.data)
	preOrder(node.left)
	preOrder(node.right)



pre = [10, 5, 1, 7, 40, 50]
root = constructBST(pre)

preOrder(root)










