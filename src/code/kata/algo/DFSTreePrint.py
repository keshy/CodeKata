__author__ = 'shankar'

class Node:

    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None

    def addNode(self, value):
        inserting = Node(value)
        inserting.item = value
        if value < self.item:
            if self.left is not None:
                self.left.addNode(value)
            else:
                self.left = inserting
        else:
            if self.right is not None:
                self.right.addNode(value)
            else:
                self.right = inserting


def printNode(root):
    if root is None:
        return

    print ("%s" % root.item)
    printNode(root.left)
    printNode(root.right)



def createTree():
    root = Node(10)
    root.addNode(12)
    root.addNode(7)
    root.addNode(13)
    return root

if __name__ == "__main__":
    root = createTree()
    printNode(root)



