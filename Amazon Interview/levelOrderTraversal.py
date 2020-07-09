class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left =None


def height(node):

    if node is None:
        return 0

    lheight = height(node.left)
    rheight = height(node.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)

    # Print nodes at a given level


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

root =Node(20)
root.left = Node(10)
root.left.left =Node(5)
root.right = Node(30)
h = height(root)
print(printLevelOrder(root))
print(h)
