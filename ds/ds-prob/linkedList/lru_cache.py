class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LRUCache:
   	# @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.hashmap = {}
        self.head = None
        self.tail = None

    # @return an integer
    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            value = node.val
            self.removeNode(node)
            self.addToFront(node)
            return value
        return -1
    
    def removeNode(self, node):   
    	if node.next is None :
    		#remove last node 
    		node.prev.next = node.next
    		node.prev = None
    	else :
	        node.prev.next = node.next
	        node.next.prev = node.prev
    
    def addToFront(self, node):
       	if self.head is None :
       		self.head = node 
       		self.tail = node
       	else :
       		self.head.prev = node
       		node.next = self.head

       	self.head = node

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.removeNode(node)
            self.addToFront(node)
        else:
            if self.count == self.capacity:
                #Delete last node
                lastNode = self.tail
                lastKey = lastNode.key
                del self.hashmap[lastKey]
                self.removeNode(lastNode)
                #Add new node
                newNode = Node(key, value)
                self.hashmap[key] = newNode
                self.addToFront(newNode)
            else:
                newNode = Node(key, value)
                self.hashmap[key] = newNode
                self.addToFront(newNode)
                self.count += 1


    def print_cacahe(self) :
    	print("cacahe:")
    	for k,v in self.hashmap.items() :
    		print(k, v.val)


lru = LRUCache(5)
lru.set(3, 3)
lru.set(4, 4)
lru.set(5, 5)
lru.set(31, 33)
lru.set(41, 44)
lru.set(51, 55)

print(lru.head.val, lru.tail.val, lru.count, lru.capacity) 

curr = lru.head
while curr is not None :
	print(curr.val)
	curr = curr.next          
            
            
            
        

