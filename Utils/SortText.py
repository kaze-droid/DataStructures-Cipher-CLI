"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from DataStructures.SortedList import Node, SortedList

class textNode(Node):
    def __init__(self, filename, shift, text):
        super().__init__()
        self.filename = filename
        self.shift = shift
        self.text = text

    # Check if two nodes are equal
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.shift == otherNode.shift
    
    # Checks if the node value of the other node is less than the node value of the current node
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'textNode' and 'NoneType'")
        
        # First check frequency
        if self.shift < otherNode.shift:
            return True
        else:
            return False
    
    def __str__(self):        
        return f"filenameNode({self.filename}, {self.shift}, {self.text})"

class SortText(SortedList):
    def __init__(self):
        super().__init__()
        self.__textFiles = SortedList()
        self.__textFiles.textfileToList = self.textfileToList

    # Define new method for self.__counter called toList() which converts either node.letter or node.freq to a list based on the parameter passed in
    def textfileToList(self, nodeType: str = "filename") -> [str]:
        listResult = []
        if nodeType not in ["filename", "shift", "text"]:
            raise ValueError("Parameter 'type' must be either 'filename', 'shift' or 'text'")
        else:
            cur = self.__textFiles.headNode
            while cur != None:
                if nodeType == "filename":
                    listResult.append(cur.filename)
                elif nodeType == "shift":
                    listResult.append(cur.shift)
                elif nodeType == "text":
                    listResult.append(cur.text)
                cur = cur.nextNode
        
        
        return listResult
    
    def addTextfile(self, filename, shift, text):
        # Print all attributes of self
        self.__textFiles.insert(textNode(filename, shift, text))

    def getTextfiles(self):
        return self.__textFiles
    
    def clearSortText(self):
        self.__textFiles = SortedList()
        self.__textFiles.textfileToList = self.textfileToList
    