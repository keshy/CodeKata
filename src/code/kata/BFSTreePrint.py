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


def printNode(queue):
    if queue is None or len(queue) == 0:
        return
    # instantiate queue for every level
    q = []
    for root in queue:
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
    print ' '.join([str(k.item) for k in q])
    return printNode(q)


def createTree():
    root = Node(10)
    root.addNode(12)
    root.addNode(7)
    root.addNode(13)
    return root

if __name__ == "__main__":
    root = createTree()
    print ("%s" % root.item)
    printNode([root])



