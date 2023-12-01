"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None
    
class SortedList:
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode, reverse=False):
        self.length += 1

        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return
        
        # Check if it is going to be new head
        if not reverse:
            if newNode < self.headNode:
                self.__appendToHead(newNode)
                return
        else:
            if newNode > self.headNode:
                self.__appendToHead(newNode)
                return
        
        # Check it is going to be inserted between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode

        while rightNode != None:
            if not reverse:
                if newNode < rightNode:
                    leftNode.nextNode = newNode
                    newNode.nextNode = rightNode
                    return
            else:
                if newNode > rightNode:
                    leftNode.nextNode = newNode
                    newNode.nextNode = rightNode
                    return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        # Once we reach here it must be added at the tail
        leftNode.nextNode = newNode

    def __str__(self):
        # We start at the head
        output =""
        node= self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += (',' + node.__str__())
            node= node.nextNode
        return output