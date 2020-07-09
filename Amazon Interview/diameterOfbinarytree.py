class Node():
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None
def height(node):
    if node is None:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)
    return 1+lheight+rheight

def diameter(node):
    if node is None:
        return 0
    ldiameter = diameter(node.left)
    rdiameter = diameter(node.right)
    height1 = height(node)
    return max(height1,max(ldiameter,rdiameter))

root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left =Node(10)
root.right.right =Node(50)
height1 =height(root)
diameter = diameter(root)
print(diameter)
print(height1)