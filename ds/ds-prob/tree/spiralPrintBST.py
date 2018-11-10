

class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.nextRight = None


class BT:
    
    def __init__(self):
        self.root = None
        self.nodeDict = {}
        self.visited = False
        self.firstNode = False

    def addNode(self, parent, child, direction):
        if child not in self.nodeDict:
            childNode = Node(child)
            self.nodeDict[child] = childNode
        else:
            childNode = self.nodeDict[child]

        if parent not in self.nodeDict:
            parentNode = Node(parent)
            self.nodeDict[parent] = parentNode
        else:
            parentNode = self.nodeDict[parent]

        if direction == 'L':
            parentNode.left = childNode
        else:
            parentNode.right = childNode

        if not self.root:
            self.root = parentNode

    def getLevelSpiral(self):
        # Write your function HERE
        # Return the level Spiral as described
        result = []
        if self.root is None :
            return result
        
        storeLeftoRight = False
        queue = []
        reverseQueue = []
        
        queue.append(self.root)
        
        lenOfQueue = len(queue)
            
        while len(queue) > 0 :
            currentSizeOfQueue = len(queue)

            while currentSizeOfQueue :
                item = queue.pop(0)
                
                if storeLeftoRight == False :
                    reverseQueue.append(item)
                else :    
                    result.append(item.data)
                
                if item.left :
                    queue.append(item.left)
                if item.right :
                    queue.append(item.right)
                    
                currentSizeOfQueue -= 1
                
            if storeLeftoRight == False :
                while len(reverseQueue) > 0 :
                    ritem = reverseQueue.pop()
                    result.append(ritem.data)
                
            storeLeftoRight = not storeLeftoRight
        
        return result


n = int(input())
edges = input().strip().split()

bt = BT()

for i in range(0, n * 3, 3):
    parent = edges[i]
    child = edges[i + 1]
    direction = edges[i + 2]
    bt.addNode(parent, child, direction)

levelSpiral = bt.getLevelSpiral()
resultString = ''
for i in levelSpiral:
    resultString = resultString + i + " "
print(resultString.strip())
