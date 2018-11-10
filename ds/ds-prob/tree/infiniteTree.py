import random

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def generate():
    v = random.randint(1, 100)
    root = Node(v)

    if random.random() < 0.5:
        root.left = generate()
    if random.random() < 0.5:
        root.right = generate()

    return root


def preOrder(node) :
    if not node :
        return 
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

root = generate()
preOrder(root)
