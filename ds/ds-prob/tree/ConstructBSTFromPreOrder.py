
class Node :
	def __init__(self, d) :
		self.data= d
		self.left = None
		self.right = None

def preOrder(node) :
	if not node :
		return 
	print(node.data)
	preOrder(node.left)
	preOrder(node.right)

def constructBSTUtil(pre, low, high, size, pre_index) :
	print(pre, low, high, size, pre_index)
	if( pre_index >= size or low > high ) :
		return None

	root = Node(pre[pre_index])
	#incrementPreIndex()

	if low==high :
		return root

	for i in range(low, high+1) :
		if pre[i] > root.data :
			break

	preOrder(root)
	root.left = constructBSTUtil(pre, pre_index+1, i-1, size, pre_index+1)
	root.right = constructBSTUtil(pre, i, high, size, i)
	return root

def constructBST(pre) :
	constructBSTUtil(pre, 0, len(pre)-1, len(pre), 0)

pre = [10, 5, 1, 7, 40, 50]
root = constructBST(pre)
print(root)
preOrder(root)