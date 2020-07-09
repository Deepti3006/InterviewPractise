class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

root = Node(20)
root.left = Node(10)
root.left.left = Node(5)
root.right = Node(30)
root.right.right = Node(40)
h=height(root)
print(h)

