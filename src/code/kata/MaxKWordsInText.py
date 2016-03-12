__author__ = 'shankar'
import operator

import heapq
import datetime

class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class MinHeap:


    def __init__(self, root, max_size, current_size=0):
        self.max_size = max_size
        self.root = root
        self.current_size = current_size


    def add(self, item):
        if not self.root and not self.root.item:
            return None

        # check if number of items in this node is less than size
        newNode = Node(item)
        if self.current_size > self.max_size:
            # replace root with the new node
            newNode.left = self.root.left
            newNode.right = self.root.right
            self._rebalanceTree()
        else:
            # find the right place to insert in the binary tree
            leafNode = self._getLeafNodeForItem(item)
            if not leafNode:
                if leafNode.left is not None:
                    leafNode.left = newNode
                elif leafNode.right is not None:
                    leafNode.right = newNode
            else:
                # this becomes the root node
                self.root = newNode

    def _rebalanceTree(self):
        min = self.root.item[1]

        def getMinFromChildren(root, minValue=0):
            if root is None:
                return minValue

            if root.left.item[1] < minValue:
                minValue = root.left.item[1]
                getMinFromChildren(root.left, minValue)
            elif root.right.item[1] < minValue:
                minValue = root.right.item[1]
                getMinFromChildren(root.right, minValue)


        pass

    def _getLeafNodeForItem(self, item):
        if self.root is None:
            return None
        k, v = item
        temp = self.root
        while temp is not None and temp.left is not None or temp.right is not None:
            if v < temp.left.item[1]:
                temp = temp.left
            else:
                temp = temp.right
        return temp




class TopNList:

    def __init__(self, size):
        self.size = size
        self.itemList = []
        self.minValue = None

    def add(self, item):
        # this is insertion sort on a fixed size list
        if not self.itemList:
            self.itemList.append(item)
            self.minValue = item
        else:
            if len(self.itemList) < self.size:
                self.itemList.append(item)
            else:
                # get min value of the existing list
                minIndex = 0
                i = 0
                while i< len(self.itemList):
                    if self.itemList[minIndex][1] > self.itemList[i][1]:
                        minIndex = i
                    i += 1
                keys = [x[0] for x in self.itemList]
                k = 0
                isUpdate = False
                while k < len(keys):
                    if keys[k] == item[0]:
                        self.itemList[k] = item
                        isUpdate = True
                    k += 1


                # check if new item is more than this minimum
                if not isUpdate and item[1] > self.itemList[minIndex][1]:
                    self.itemList[minIndex] = item


    def display(self):
        print ("Printing the top %s values " % self.size)
        for k,v in self.itemList:
            print ("%s = %s" % (k,v))
        return





def getNMostFrequentlyOccuringWords(n, file):

    f = open(file, "r")
    wordCount = {}
    topN = TopNList(n)

    text = f.read()
    words = text.split()

    for word in words:
            if word in wordCount:
                wordCount[word] = wordCount.get(word) + 1
            else:
                # add word into map
                wordCount[word] = 1
            topN.add((word, wordCount[word]))

    start = datetime.datetime.now()
    # sort dictionary by value
    sortedDict = sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)
    end = datetime.datetime.now()
    print ("Took %s seconds for using quicksort library" % (end - start).total_seconds())
    print sortedDict[:n]

    print topN.display()


if __name__ == "__main__":

    # topN = TopNList(12)
    # input = [('a',4),('b',6),('c', 7), ('d', 8) , ('e',9), ('f', 10), ('g', 11),('h',4),('i', 1),('j', 2)]
    # for x in input:
    #     topN.add(x)
    # topN.display() [('the', 23407), ('I', 19540), ('and', 18358), ('to', 15682), ('of', 15649), ('a', 12586), ('my', 10825), ('in', 9633), ('you', 9129), ('is', 7874)]

    print ("Top %s frequent words in file = %s " % (10, getNMostFrequentlyOccuringWords(10, "../resource/test_file")))

