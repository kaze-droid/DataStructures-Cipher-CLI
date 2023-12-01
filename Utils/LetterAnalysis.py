"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from DataStructures.SortedList import Node, SortedList
import string

class freqNode(Node):
    def __init__(self, letter, freq, sum_of_letters):
        super().__init__()
        self.letter = letter.upper()
        self.freq = freq
        self.percentage = self.calculatePercentage(freq, sum_of_letters)
    
    def calculatePercentage(self, freq, total_sum):
        return freq/total_sum*100

    # Check if two nodes are equal
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.letter == otherNode.letter and self.freq == otherNode.freq
    
    # Checks if the node value of the other node is less than the node value of the current node
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'freqNode' and 'NoneType'")
        
        # First check frequency
        if self.freq < otherNode.freq:
            return True
        elif self.freq > otherNode.freq:
            return False
        else:
            # If frequency is the same, compare alphabetically
            return self.letter > otherNode.letter
    
    def __str__(self):        
        return f"freqNode({self.letter}, {self.freq}, {self.percentage}%)"


class LetterAnalysis(SortedList):
    def __init__(self):
        super().__init__()
        self.__sum_of_letters = -1
        self.__counter = SortedList()
        self.__counter.counterToList = self.counterToList

    # Define new method for self.__counter called toList() which converts either node.letter or node.freq to a list based on the parameter passed in
    def counterToList(self, nodeType: str = "letter") -> [str]:
        listResult = []
        if nodeType not in ["letter", "freq", "percentage"]:
            raise ValueError("Parameter 'type' must be either 'letter', 'freq' or 'percentage'")
        else:
            cur = self.__counter.headNode
            while cur != None:
                if nodeType == "letter":
                    listResult.append(cur.letter)
                elif nodeType == "freq":
                    listResult.append(cur.freq)
                elif nodeType == "percentage":
                    listResult.append(cur.percentage)
                cur = cur.nextNode
        
        return listResult
    
    def getSumOfLetters(self):
        return self.__sum_of_letters

    def getCounter(self):
        return self.__counter

    def insertCounter(self, letter: str, freq: int, reverse: bool = False):
        sumOfLetters = self.getSumOfLetters()
        self.__counter.insert(freqNode(letter, freq, sumOfLetters), reverse=reverse)
    
    # Analyse the frequency of each letter and store it in a SortedList
    def analyseFreq(self, text: str):
        # Using a dictionary to temporarily store the frequency of each letter
        counterDict = {letter: 0 for letter in string.ascii_uppercase}
        for letter in text:
            if letter.isalpha() == True:
                counterDict[letter.upper()] += 1
        
        # Calculate the total number of letters
        self.__sum_of_letters = sum(counterDict.values())

        # Populate the counter by shifting the data from the dictionary to the SortedList
        for letter, freq in counterDict.items():
            self.insertCounter(letter, freq, reverse=True)

    # Used to reformat the plot from a list of lists to a list of strings
    def reformatPlot(self, plot: [[str]]):
        # Transpose the Plot
        plot = list(map(list, zip(*plot)))
        # Reverse the Plot
        plot = plot[::-1]
        # Add the border
        for line in plot[:-1]:
            line.append('|')

        return ["".join(line) for line in plot]

    def numericalStatistics(self, plot: [str], letterList: [str], percentageList: [int]):
        line = 0

        top5 = ["TOP 6 FREQ", "----------"]
        # Get top 5 letters
        for letter, percentage in zip(letterList[:6], percentageList[:6]):
            top5.append(f"{letter} - {percentage:.2f}%")

        for letter in string.ascii_uppercase:
            index = letterList.index(letter)
            percentage = f"{percentageList[index]:.2f}"
            plot[line] += f"{letter} - {percentage}%{(5-len(percentage))*' '}"

            # Check if letter is between K and Q
            if ord(letter) >= ord('K') and ord(letter) <= ord('R'):
                plot[line] += f"\t{top5[ord(letter)-ord('K')]}"

            line+=1
        
        return plot
    
    # Build each column upwards from the bottom
    def buildColumn(self, letter: ("None | str"), percentage: ("None | int") = None):
        if letter == None:
            res = f" _{' '*26}"
        else:
            num_stars = round(percentage/100 * 26)
            res = f"{letter}_{'*'*num_stars}{' '*(26-num_stars)}"
        
        return res

    # Export the findings to a file for use in option 4
    def exportFindings(self, exportFile):
        text = ""
        with open(exportFile, 'w') as f:
            for letter in string.ascii_uppercase:
                index = self.getList("letter").index(letter)
                percentage = self.getList("percentage")[index]
                text+= f"{letter},{percentage:.2f}\n"
            # Remove the last newline character
            f.write(text[:-1])
