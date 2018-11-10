class Node:
	def __init__(self, val):
		self.val = v
		self.prev = None
		self.next = None

class LRUCache :

	def __init__(self, cap):
		self.capacity = cap
		self.map = {}
		Node head = None
		Node end = None

	def remove(self, n):
		if n.prev != None :
			n.prev.next = n.next
		else :
			self.head = n.next

		if n.next != None :
			n.next.prev = n.prev
		else :
			self.end = n.prev
		self.capacity -= 1 

	def setHead(self, n) :

		n.next = self.head
		n.prev = None
		if self.head != None
			self.head.prev = n

		self.head = n
		self.capacity += 1 


	def getKey(self, k) :
		if self.map.has_key(k) :
			node = self.map[k]

			self.remove(node)
			self.setHead(node)
			return node.val
		return -1

	def setKey(self, k, v) :
		if self.map.has_key(k) :
			old_node = self.map[k]
			old_node.val = v
			self.remove(old_node)
			self.setHead(old_node)
		else :
			new_node = Node(v)
			if size(self.map) < self.capacity :
				self.sethead(new_node)
			else :
				self.remove(self.end)
				self.sethead(new_node)

			self.map.put(k, new_node)